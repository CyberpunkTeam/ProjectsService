from datetime import datetime
from typing import Optional, List

from app.models.auxiliary_models.request_states import RequestStates
from app.models.custom_base_model import CustomBaseModel


class ProjectAbandonsRequests(CustomBaseModel):
    par_id: Optional[str] = ""
    pid: str
    tid: str
    reasons: List[str]
    state: Optional[RequestStates] = None
    created_date: Optional[str] = ""
    updated_date: Optional[str] = ""

    @staticmethod
    def get_schema():
        return {
            "par_id": str,
            "tid": str,
            "pid": str,
            "reasons": list,
            "state": str,
            "created_date": str,
            "updated_date": str,
        }

    def complete(self):
        self.par_id = ProjectAbandonsRequests.get_id()
        self.state = RequestStates.PENDING
        local = datetime.now()
        self.created_date = local.strftime("%d-%m-%Y:%H:%M:%S")
        self.updated_date = local.strftime("%d-%m-%Y:%H:%M:%S")
