from datetime import datetime
from typing import Optional, List
from app.models.auxiliary_models.activities_record import ActivitiesRecord
from app.models.auxiliary_models.currency import Currency
from app.models.auxiliary_models.description import Description
from app.models.auxiliary_models.internal_states import InternalStates
from app.models.auxiliary_models.technologies import Technologies
from app.models.auxiliary_models.unit_duration import UnitDuration
from app.models.custom_base_model import CustomBaseModel
from app.models.auxiliary_models.project_states import ProjectStates


class Projects(CustomBaseModel):
    pid: Optional[str] = None
    name: str
    idioms: List[str]
    description: Optional[Description]
    technologies: Optional[Technologies]
    creator_uid: str
    state: Optional[ProjectStates] = None
    created_date: Optional[str] = ""
    updated_date: Optional[str] = ""
    team_assigned: Optional[str] = None
    activities_record: Optional[List[ActivitiesRecord]] = []
    tentative_budget: Optional[float]
    budget_currency: Optional[Currency]
    tentative_duration: Optional[int]
    unit_duration: Optional[UnitDuration]
    project_type: Optional[str]
    internal_state: Optional[InternalStates]

    @staticmethod
    def get_schema():
        return {
            "pid": str,
            "name": str,
            "idioms": list,
            "description": dict,
            "technologies": dict,
            "creator_uid": str,
            "created_date": str,
            "updated_date": str,
            "state": str,
            "team_assigned": str,
            "activities_record": list,
            "tentative_budget": float,
            "budget_currency": str,
            "tentative_duration": int,
            "unit_duration": str,
            "project_type": str,
            "internal_state": str,
        }

    def complete(self):
        self.state = ProjectStates.PENDING
        self.pid = Projects.get_id()
        local = datetime.now()
        created_date = local.strftime("%d-%m-%Y:%H:%M:%S")
        self.created_date = created_date
        self.updated_date = created_date
        self.internal_state = InternalStates.ACTIVE
