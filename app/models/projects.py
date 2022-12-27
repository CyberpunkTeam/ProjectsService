import uuid
from datetime import datetime
from json import loads
from typing import Optional, List

from pydantic import BaseModel


class Projects(BaseModel):
    pid: Optional[str] = None
    name: str
    idioms: List[str]
    description: str
    technologies: List[str]
    creator_uid: str
    created_date: Optional[str] = ""
    updated_date: Optional[str] = ""

    def to_json(self):
        return loads(self.json(exclude_defaults=True))

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
        }

    @staticmethod
    def get_pid():
        myuuid = uuid.uuid4()
        return str(myuuid)

    def complete(self):
        self.pid = Projects.get_pid()
        local = datetime.now()
        self.created_date = local.strftime("%d-%m-%Y:%H:%M:%S")
