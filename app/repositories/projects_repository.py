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

    def get(self, email=None):
        if email is None:
            return self.filter(self.COLLECTION_NAME, {}, output_model=Projects)
        return self.find_by(self.COLLECTION_NAME, "pid", email, output_model=Projects)

    def insert(self, project: Projects):
        return self.save(self.COLLECTION_NAME, project)

    @staticmethod
    def create_repository(url, database_name):
        return ProjectsRepository(url, database_name)
