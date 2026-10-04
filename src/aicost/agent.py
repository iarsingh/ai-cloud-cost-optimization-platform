TOOLS = ["inventory", "recommend"]
WRITES = ("delete disk", "apply",)


class InputError(ValueError):
    pass


def run(goal, payload):
    if not isinstance(goal, str) or not goal.strip():
        raise InputError("goal is empty")
    if any(word in goal.lower() for word in WRITES):
        return {"refused": True, "reason": "This agent only reads or plans. It does not write.", "tools": [], "wrote": False, "applied": False}
    result = [d["id"] for d in payload.get("disks") or [] if not d.get("attached") and float(d.get("size_gb", 0)) >= 100]
    return {"refused": False, "tools": TOOLS, "idle_disks": result, "wrote": False, "applied": False}
