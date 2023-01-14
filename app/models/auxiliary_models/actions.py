from enum import Enum


class Actions(str, Enum):
    CREATED = "CREATED"
    TEAM_ASSIGNED = "TEAM_ASSIGNED"
    CANCELLED = "CANCELLED"
    FINISHED = "FINISHED"
    ABANDONED = "ABANDONED"
