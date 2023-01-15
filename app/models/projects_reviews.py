from datetime import datetime
from typing import Optional

from app.models.custom_base_model import CustomBaseModel


class ProjectsReviews(CustomBaseModel):
    pid: str
    tid: str
    created_date: Optional[str] = ""
    rating: int

    @staticmethod
    def get_schema():
        return {
            "pid": str,
            "tid": str,
            "created_date": str,
            "rating": int,
        }

    def complete(self):
        local = datetime.now()
        created_date = local.strftime("%d-%m-%Y:%H:%M:%S")
        self.created_date = created_date
