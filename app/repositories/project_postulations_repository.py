from cpunk_mongo.db import DataBase

from app.models.project_postulations import ProjectPostulations


class ProjectPostulationsRepository(DataBase):
    COLLECTION_NAME = "project_postulations"

    def __init__(self, url, db_name):
        if db_name == "test":
            import mongomock

            self.db = mongomock.MongoClient().db
        else:
            super().__init__(url, db_name)

    def get(self, pid=None, tid=None, ppid=None, state=None):
        filters = {}
        if pid is not None:
            filters["pid"] = pid

        if state is not None:
            filters["state"] = state

        if tid is not None:
            filters["tid"] = tid

        if ppid is not None:
            filters["ppid"] = ppid

        return self.filter(
            self.COLLECTION_NAME, filters, output_model=ProjectPostulations
        )

    def insert(self, project_postulation: ProjectPostulations):
        return self.save(self.COLLECTION_NAME, project_postulation)

    @staticmethod
    def create_repository(url, database_name):
        return ProjectPostulationsRepository(url, database_name)

    def put(self, project_postulation_update):
        return self.update(
            self.COLLECTION_NAME,
            "ppid",
            project_postulation_update.ppid,
            project_postulation_update,
        )

    def reset(self):
        self.delete_all(self.COLLECTION_NAME)
