import uuid
from datetime import datetime
from json import loads
from typing import Optional

from pydantic import BaseModel

from app.models.currency import Currency
from app.models.states import States


class ProjectPostulations(BaseModel):
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

    def to_json(self):
        return loads(self.json(exclude_defaults=True))

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

    @staticmethod
    def get_ppid():
        myuuid = uuid.uuid4()
        return str(myuuid)

    def complete(self):
        self.ppid = ProjectPostulations.get_ppid()
        self.state = States.PENDING
        local = datetime.now()
        self.created_date = local.strftime("%d-%m-%Y:%H:%M:%S")
        self.updated_date = local.strftime("%d-%m-%Y:%H:%M:%S")
