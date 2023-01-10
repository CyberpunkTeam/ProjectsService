from datetime import datetime
from typing import Optional, List

from app.models.custom_base_model import CustomBaseModel
from app.models.auxiliary_models.project_states import ProjectStates


class Projects(CustomBaseModel):
    pid: Optional[str] = None
    name: str
    idioms: List[str]
    description: str
    technologies: List[str]
    creator_uid: str
    state: Optional[ProjectStates] = None
    created_date: Optional[str] = ""
    updated_date: Optional[str] = ""
    team_assigned: Optional[str] = None

    @staticmethod
    def get_schema():
        return {
            "pid": str,
            "name": str,
            "idioms": list,
            "description": str,
            "technologies": list,
            "creator_uid": str,
            "created_date": str,
            "updated_date": str,
            "state": str,
            "team_assigned": str,
        }

    def complete(self):
        self.state = ProjectStates.PENDING
        self.pid = Projects.get_id()
        local = datetime.now()
        self.created_date = local.strftime("%d-%m-%Y:%H:%M:%S")
        self.updated_date = local.strftime("%d-%m-%Y:%H:%M:%S")
