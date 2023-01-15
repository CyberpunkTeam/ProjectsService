from cpunk_mongo.db import DataBase

from app.models.projects_reviews import ProjectsReviews


class ProjectsReviewsRepository(DataBase):
    COLLECTION_NAME = "project_reviews"

    def __init__(self, url, db_name):
        if db_name == "test":
            import mongomock

            self.db = mongomock.MongoClient().db
        else:
            super().__init__(url, db_name)

    def get(self, pid=None, tid=None):
        filters = {}

        if pid is not None:
            filters["pid"] = pid

        if tid is not None:
            filters["tid"] = tid

        return self.filter(self.COLLECTION_NAME, filters, output_model=ProjectsReviews)

    def insert(self, activity: ProjectsReviews):
        return self.save(self.COLLECTION_NAME, activity)

    @staticmethod
    def create_repository(url, database_name):
        return ProjectsReviewsRepository(url, database_name)

    def reset(self):
        self.delete_all(self.COLLECTION_NAME)
