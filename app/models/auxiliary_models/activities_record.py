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
            Actions.FINISHED: "El proyecto ha finalizado",
            Actions.CREATED: "El proyecto se creo",
            Actions.CANCELLED: "El proyecto fue cancelado",
            Actions.ABANDONED: "El equipo asignado abandono el proyecto",
            Actions.TEAM_ASSIGNED: "El proyecto tiene equipo asignado",
        }
        return titles[self.action]
