import os
from typing import List

from fastapi import APIRouter

from app import config
from app.controllers.projects_reviews_controller import ProjectsReviewsController
from app.models.projects_reviews import ProjectsReviews
from app.repositories.projects_reviews_repository import ProjectsReviewsRepository


router = APIRouter()

# Repository
projects_reviews_repository = ProjectsReviewsRepository(
    config.DATABASE_URL, config.DATABASE_NAME
)


@router.post("/projects/reset", tags=["projects_reviews"], status_code=200)
async def reset():
    if os.environ.get("TEST_MODE") == "1":
        return {"reset": projects_reviews_repository.reset()}


@router.post(
    "/projects_reviews/",
    tags=["projects_reviews"],
    response_model=ProjectsReviews,
    status_code=201,
)
async def create_project(project_review: ProjectsReviews):
    return ProjectsReviewsController.post(projects_reviews_repository, project_review)


@router.get(
    "/projects_reviews/",
    tags=["projects_reviews"],
    response_model=List[ProjectsReviews],
)
async def list_projects(pid: str = None, tid: str = None):
    return ProjectsReviewsController.get(projects_reviews_repository, pid=pid, tid=tid)
