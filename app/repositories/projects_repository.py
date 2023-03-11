from cpunk_mongo.db import DataBase

from app.models.projects import Projects


class ProjectsRepository(DataBase):
    COLLECTION_NAME = "projects"
    FILTER_NAMES = {}

    def __init__(self, url, db_name):
        if db_name == "test":
            import mongomock

            self.db = mongomock.MongoClient().db
        else:
            super().__init__(url, db_name)

    def get(
        self,
        pid=None,
        creator_uid=None,
        state=None,
        programming_language=None,
        frameworks=None,
        platforms=None,
        databases=None,
        budget_currency=None,
        min_tentative_budget=None,
        max_tentative_budget=None,
        idioms=None,
        projects_types=None,
    ):
        filters = {}

        if pid is not None:
            filters["pid"] = pid

        if creator_uid is not None:
            filters["creator_uid"] = creator_uid

        if state is not None:
            filters["state"] = state

        if programming_language is not None and len(programming_language) > 0:
            filters["technologies.programming_language"] = {"$in": programming_language}

        if frameworks is not None and len(frameworks) > 0:
            filters["technologies.frameworks"] = {"$in": frameworks}

        if platforms is not None and len(platforms) > 0:
            filters["technologies.platforms"] = {"$in": platforms}

        if databases is not None and len(databases) > 0:
            filters["technologies.databases"] = {"$in": databases}

        if idioms is not None and len(idioms) > 0:
            filters["idioms"] = {"$in": idioms}

        if projects_types is not None and len(projects_types) > 0:
            filters["project_type"] = {"$in": projects_types}

        if budget_currency is not None:
            filters["budget_currency"] = budget_currency

        if min_tentative_budget is not None and max_tentative_budget is not None:
            filters["tentative_budget"] = {
                "$lte": max_tentative_budget,
                "$gte": min_tentative_budget,
            }
        elif min_tentative_budget is not None:
            filters["tentative_budget"] = {"$gte": min_tentative_budget}
        elif max_tentative_budget is not None:
            filters["tentative_budget"] = {"$lte": max_tentative_budget}

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
