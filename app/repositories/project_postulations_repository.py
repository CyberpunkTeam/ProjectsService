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

    def get(self, pid=None, tid=None, ppid=None):
        if pid is None and tid is None:
            return self.filter(
                self.COLLECTION_NAME, {}, output_model=ProjectPostulations
            )
        elif pid is not None:
            return self.find_by(
                self.COLLECTION_NAME, "pid", pid, output_model=ProjectPostulations
            )
        elif pid is not None:
            return self.find_by(
                self.COLLECTION_NAME, "ppid", ppid, output_model=ProjectPostulations
            )
        else:
            return self.find_by(
                self.COLLECTION_NAME, "tid", tid, output_model=ProjectPostulations
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
