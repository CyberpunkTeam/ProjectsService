from datetime import datetime
from typing import Optional

from app.models.auxiliary_models.request_states import RequestStates
from app.models.custom_base_model import CustomBaseModel


class ProjectFinishedRequests(CustomBaseModel):
    pfr_id: Optional[str] = ""
    pid: str
    tid: str
    state: Optional[RequestStates]
    created_date: Optional[str] = ""
    updated_date: Optional[str] = ""

    @staticmethod
    def get_schema():
        return {
            "pfr_id": str,
            "tid": str,
            "pid": str,
            "state": str,
            "created_date": str,
            "updated_date": str,
        }

    def complete(self):
        self.pfr_id = ProjectFinishedRequests.get_id()
        self.state = RequestStates.PENDING
        local = datetime.now()
        self.created_date = local.strftime("%d-%m-%Y:%H:%M:%S")
        self.updated_date = local.strftime("%d-%m-%Y:%H:%M:%S")
