from enum import Enum

from app.models.auxiliary_models.project_states import ProjectStates


class Actions(str, Enum):
    CREATED = "CREATED"
    TEAM_ASSIGNED = "TEAM_ASSIGNED"
    CANCELLED = "CANCELLED"
    FINISHED = "FINISHED"
    ABANDONED = "ABANDONED"
    FINISH_REQUEST = "FINISH_REQUEST"
    ABANDONS_REQUEST = "ABANDONS_REQUEST"
