from datetime import datetime

from fastapi import HTTPException

from app.models.projects_reviews import ProjectsReviews


class ProjectsReviewsController:
    @staticmethod
    def post(repository, project_review: ProjectsReviews):
        project_review.complete()
        ok = repository.insert(project_review)
        if not ok:
            raise HTTPException(status_code=500, detail="Error saving")

        return project_review

    @staticmethod
    def get(repository, pid=None, tid=None):
        result = repository.get(pid=pid, tid=tid)
        return result
