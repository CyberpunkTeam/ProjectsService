from cpunk_mongo.db import DataBase

from app.models.projects import Projects


class ProjectsRepository(DataBase):
    COLLECTION_NAME = "projects"

    def __init__(self, url, db_name):
        if db_name == "test":
            import mongomock

            self.db = mongomock.MongoClient().db
        else:
            super().__init__(url, db_name)

    def get(self, pid=None, creator_uid=None, state=None):
        filters = {}

        if pid is not None:
            filters["pid"] = pid

        if creator_uid is not None:
            filters["creator_uid"] = creator_uid

        if state is not None:
            filters["state"] = state

        return self.filter(self.COLLECTION_NAME, filters, output_model=Projects)

    def insert(self, project: Projects):
        return self.save(self.COLLECTION_NAME, project)

    @staticmethod
    def create_repository(url, database_name):
        return ProjectsRepository(url, database_name)

    def put(self, project_update):
        return self.update(
            self.COLLECTION_NAME, "pid", project_update.pid, project_update
        )

    def reset(self):
        self.delete_all(self.COLLECTION_NAME)
