from cpunk_mongo.db import DataBase

from app.models.project_abandons_requests import ProjectAbandonsRequests
from app.models.project_postulations import ProjectPostulations


class ProjectAbandonsRequestsRepository(DataBase):
    COLLECTION_NAME = "project_abandons_requests"

    def __init__(self, url, db_name):
        if db_name == "test":
            import mongomock

            self.db = mongomock.MongoClient().db
        else:
            super().__init__(url, db_name)

    def get(self, pid=None, par_id=None, tid=None):
        filters = {}
        if pid is not None:
            filters["pid"] = pid

        if par_id is not None:
            filters["par_id"] = par_id

        if tid is not None:
            filters["tid"] = tid

        return self.filter(
            self.COLLECTION_NAME, filters, output_model=ProjectAbandonsRequests
        )

    def insert(self, project_postulation: ProjectPostulations):
        return self.save(self.COLLECTION_NAME, project_postulation)

    @staticmethod
    def create_repository(url, database_name):
        return ProjectAbandonsRequestsRepository(url, database_name)

    def reset(self):
        self.delete_all(self.COLLECTION_NAME)

    def put(self, project_abandons_request_update):
        return self.update(
            self.COLLECTION_NAME,
            "par_id",
            project_abandons_request_update.par_id,
            project_abandons_request_update,
        )
