from enum import Enum


class ProjectStates(str, Enum):
    CANCELLED = "CANCELLED"
    FINISHED = "FINISHED"
    PENDING = "PENDING"
    WIP = "WIP"
    FINISH_REQUEST = "FINISH_REQUEST"
    ABANDONS_REQUEST = "ABANDONS_REQUEST"
