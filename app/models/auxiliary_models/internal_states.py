from enum import Enum


class InternalStates(str, Enum):
    BLOCKED = "BLOCKED"
    ACTIVE = "ACTIVE"
