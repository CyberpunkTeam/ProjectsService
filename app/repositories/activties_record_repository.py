from cpunk_mongo.db import DataBase

from app.models.auxiliary_models.activities_record import ActivitiesRecord


class ActivitiesRecordRepository(DataBase):
    COLLECTION_NAME = "activities_record"

    def __init__(self, url, db_name):
        if db_name == "test":
            import mongomock

            self.db = mongomock.MongoClient().db
        else:
            super().__init__(url, db_name)

    def get(self, pid=None, action=None):
        filters = {}

        if pid is not None:
            filters["pid"] = pid

        if action is not None:
            filters["action"] = action

        return self.filter(self.COLLECTION_NAME, filters, output_model=ActivitiesRecord)

    def insert(self, activity: ActivitiesRecord):
        return self.save(self.COLLECTION_NAME, activity)

    @staticmethod
    def create_repository(url, database_name):
        return ActivitiesRecordRepository(url, database_name)

    def reset(self):
        self.delete_all(self.COLLECTION_NAME)
