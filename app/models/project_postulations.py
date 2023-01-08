from datetime import datetime
from typing import Optional

from app.models.auxiliary_models.currency import Currency
from app.models.custom_base_model import CustomBaseModel
from app.models.auxiliary_models.states import States


class ProjectPostulations(CustomBaseModel):
    ppid: Optional[str] = None
    tid: str
    pid: str
    project_owner_uid: Optional[str]
    estimated_budget: int
    currency: Currency
    proposal_description: str
    state: Optional[States]
    created_date: Optional[str] = ""
    updated_date: Optional[str] = ""

    @staticmethod
    def get_schema():
        return {
            "ppid": str,
            "tid": str,
            "pid": str,
            "project_owner_uid": str,
            "estimated_budget": str,
            "currency": str,
            "proposal_description": str,
            "state": str,
            "created_date": str,
            "updated_date": str,
        }

    def complete(self):
        self.ppid = ProjectPostulations.get_id()
        self.state = States.PENDING
        local = datetime.now()
        self.created_date = local.strftime("%d-%m-%Y:%H:%M:%S")
        self.updated_date = local.strftime("%d-%m-%Y:%H:%M:%S")
