from cpunk_mongo.db import DataBase

from app.models.project_abandonment import ProjectAbandonment
from app.models.project_postulations import ProjectPostulations


class ProjectAbandonmentRepository(DataBase):
    COLLECTION_NAME = "project_abandonment"

    def __init__(self, url, db_name):
        if db_name == "test":
            import mongomock

            self.db = mongomock.MongoClient().db
        else:
            super().__init__(url, db_name)

    def get(self, pid=None, pa_id=None, tid=None):
        filters = {}
        if pid is not None:
            filters["pid"] = pid

        if pa_id is not None:
            filters["pa_id"] = pa_id

        if tid is not None:
            filters["tid"] = tid

        return self.filter(
            self.COLLECTION_NAME, filters, output_model=ProjectAbandonment
        )

    def insert(self, project_postulation: ProjectPostulations):
        return self.save(self.COLLECTION_NAME, project_postulation)

    @staticmethod
    def create_repository(url, database_name):
        return ProjectAbandonmentRepository(url, database_name)

    def reset(self):
        self.delete_all(self.COLLECTION_NAME)
