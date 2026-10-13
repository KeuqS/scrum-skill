"""Generate a private, dependency-free HTML report from explicit Scrum records."""
import argparse
import datetime as dt
import json
import math
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]


def number(value, name, signed=False):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError(f"{name} must be a finite number")
    if not signed and value < 0:
        raise ValueError(f"{name} must not be negative")
    return value


def text(value, name):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} must be nonempty text")


def dates(record):
    for key in ("start_date", "end_date"):
        if key in record:
            value = record[key]
            if not isinstance(value, str) or dt.date.fromisoformat(value).isoformat() != value:
                raise ValueError(f"{key} must use YYYY-MM-DD")
    if record.get("start_date") and record.get("end_date") and record["start_date"] > record["end_date"]:
        raise ValueError("end_date precedes start_date")


def validate(data):
    if not isinstance(data, dict) or type(data.get("schema_version")) is not int or data.get("schema_version") != 1:
        raise ValueError("Expected schema_version 1")
    project = data["project"]
    if not isinstance(project, dict):
        raise ValueError("project must be an object")
    text(project["name"], "project.name")
    text(project["goal"], "project.goal")
    if project["data_kind"] not in ("synthetic", "project"):
        raise ValueError("data_kind must be synthetic or project")
    counted = set()
    previous_snapshot = None
    previous_completed = None
    for group in ("backlog", "sprints"):
        if not isinstance(data[group], list):
            raise ValueError(f"{group} must be a list")
        ids = set()
        for item in data[group]:
            if not isinstance(item, dict):
                raise ValueError(f"{group} entries must be objects")
            text(item["id"], "id")
            if item["id"] in ids:
                raise ValueError("Duplicate ID")
            ids.add(item["id"])
            if group == "backlog":
                text(item["title"], "title")
                if item["points"] is not None:
                    number(item["points"], "points")
                if item["status"] not in ("backlog", "in_progress", "done") or type(item["dod_met"]) is not bool:
                    raise ValueError("Invalid backlog status/DoD")
                if item["status"] == "done" and not item["dod_met"]:
                    raise ValueError("Done requires DoD")
            else:
                text(item["label"], "label")
                if item["state"] not in ("planned", "active", "completed"):
                    raise ValueError("Invalid Sprint state")
                dates(item)
                if "snapshot" in item:
                    snap = item["snapshot"]
                    if not isinstance(snap, dict):
                        raise ValueError("snapshot must be an object")
                    for key in ("scope_points", "completed_points", "unestimated_count"):
                        number(snap[key], key)
                    if type(snap["unestimated_count"]) is not int:
                        raise ValueError("unestimated_count must be an integer")
                    if snap["completed_points"] > snap["scope_points"]:
                        raise ValueError("Cumulative completion exceeds cumulative scope")
                    if previous_completed is not None and snap["completed_points"] < previous_completed:
                        raise ValueError("Cumulative completed points must not decrease; record rework separately")
                    previous_completed = snap["completed_points"]
                if "scope_changes" in item:
                    if not isinstance(item["scope_changes"], dict):
                        raise ValueError("scope_changes must be an object")
                    for key in ("added_points", "removed_points", "reestimated_delta"):
                        number(item["scope_changes"][key], key, signed=key == "reestimated_delta")
                    if previous_snapshot is not None and "snapshot" in item:
                        change = item["scope_changes"]
                        expected = previous_snapshot["scope_points"] + change["added_points"] - change["removed_points"] + change["reestimated_delta"]
                        if not math.isclose(expected, item["snapshot"]["scope_points"], abs_tol=1e-8):
                            raise ValueError("Scope changes do not reconcile with consecutive snapshots")
                if "velocity_items" in item:
                    if item["state"] != "completed" or not isinstance(item["velocity_items"], list):
                        raise ValueError("Frozen velocity records require a completed Sprint")
                    local = set()
                    for done in item["velocity_items"]:
                        if not isinstance(done, dict):
                            raise ValueError("velocity entries must be objects")
                        text(done["id"], "velocity item id")
                        number(done["points"], "velocity points")
                        if type(done["dod_met"]) is not bool:
                            raise ValueError("dod_met must be boolean")
                        if done["id"] in local or (done["dod_met"] and done["id"] in counted):
                            raise ValueError("Duplicate completed velocity item")
                        local.add(done["id"])
                        if done["dod_met"]:
                            counted.add(done["id"])
                if not isinstance(item.get("timeline", []), list):
                    raise ValueError("timeline must be a list")
                for entry in item.get("timeline", []):
                    if not isinstance(entry, dict):
                        raise ValueError("timeline entries must be objects")
                    text(entry["title"], "timeline title")
                    if entry["kind"] not in ("actual", "forecast"):
                        raise ValueError("Invalid timeline kind")
                    dates(entry)
                previous_snapshot = item.get("snapshot")
    return data


def metrics(data):
    validate(data)
    items = data["backlog"]
    history = []
    for sprint in data["sprints"]:
        snap = sprint.get("snapshot")
        history.append({
            "label": sprint["label"], "state": sprint["state"],
            "scope": snap["scope_points"] if snap else None,
            "completed": snap["completed_points"] if snap else None,
            "remaining": snap["scope_points"] - snap["completed_points"] if snap else None,
            "unestimated": snap["unestimated_count"] if snap else None,
            "velocity": sum(x["points"] for x in sprint["velocity_items"] if x["dod_met"])
            if "velocity_items" in sprint else None,
            "changes": sprint.get("scope_changes"),
        })
    return {"known_points": sum(x["points"] for x in items if x["points"] is not None),
            "unestimated": sum(x["points"] is None for x in items),
            "done_points": sum(x["points"] for x in items if x["points"] is not None and x["status"] == "done" and x["dod_met"]),
            "history": history}


def render(data):
    payload = json.dumps({"data": data, "metrics": metrics(data)}, ensure_ascii=True, allow_nan=False)
    # JSON is text in a script element: prevent HTML parser termination/XSS.
    payload = payload.replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
    return (BASE / "assets/dashboard.html").read_text(encoding="utf-8").replace("__DATA_JSON__", payload)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--input", type=Path)
    source.add_argument("--demo", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        path = BASE / "assets/demo.json" if args.demo else args.input
        data = json.loads(path.read_text(encoding="utf-8"))
        html = render(data)
        if args.output.exists():
            raise ValueError("Output exists; choose a new filename")
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("x", encoding="utf-8", newline="\n") as out:
            out.write(html)
    except (ValueError, KeyError, TypeError, OSError) as error:
        parser.exit(2, f"Dashboard not generated: {error}\n")
    print(f"Created {args.output.resolve()} (embedded data stays local unless shared)")


if __name__ == "__main__":
    main()
