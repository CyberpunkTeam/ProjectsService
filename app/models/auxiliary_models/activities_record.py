from datetime import datetime
from typing import Optional

from app.models.auxiliary_models.actions import Actions
from app.models.custom_base_model import CustomBaseModel


class ActivitiesRecord(CustomBaseModel):
    description: Optional[str] = ""
    created_date: Optional[str] = ""
    action: Actions
    pid: str

    @staticmethod
    def get_schema():
        return {"pid": str, "description": str, "created_date": str, "action": str}

    def complete(self):
        local = datetime.now()
        self.created_date = local.strftime("%d-%m-%Y:%H:%M:%S")
        self.description = self._get_description()

    def _get_description(self):
        titles = {
            Actions.FINISHED: "Project finished",
            Actions.CREATED: "Project created",
            Actions.CANCELLED: "Project cancelled",
            Actions.ABANDONED: "Team assigned abandoned the project",
            Actions.TEAM_ASSIGNED: "Project has team assigned",
            Actions.FINISH_REQUEST: "Project finish request sent",
            Actions.ABANDONS_REQUEST: "Project abandon request sent",
        }
        return titles[self.action]
