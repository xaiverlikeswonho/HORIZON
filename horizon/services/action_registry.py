from dataclasses import dataclass

@dataclass(frozen=True)
class Action:
    action_id: str
    name: str
    category: str
    interface: str
    status: str = "planned"

# Stage 1 sample manifest. The complete roadmap will expand this to 500 entries per interface.
STAGE1_ACTIONS = [
    Action("SL-001", "horizon status", "Core", "slash", "implemented"),
    Action("PX-001", "ping", "Core", "prefix", "implemented"),
    Action("PX-002", "help", "Core", "prefix", "implemented"),
    Action("PX-003", "prefix", "Configuration", "prefix", "implemented"),
]

def count_actions(actions=STAGE1_ACTIONS):
    return {key: sum(a.interface == key for a in actions) for key in ("slash", "prefix")}
