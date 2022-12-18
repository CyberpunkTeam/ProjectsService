from typing import List

from fastapi import APIRouter

from app import config
from app.controllers.projects_controller import ProjectsController
from app.models.projects import Projects
from app.repositories.projects_repository import ProjectsRepository

router = APIRouter()

# Repository
projects_repository = ProjectsRepository(config.DATABASE_URL, config.DATABASE_NAME)


@router.post("/projects/", tags=["projects"], response_model=Projects, status_code=201)
async def create_project(user: Projects):
    return ProjectsController.post(projects_repository, user)


@router.get("/projects/", tags=["projects"], response_model=List[Projects])
async def list_projects():
    return ProjectsController.get(projects_repository)


@router.get("/projects/{pid}", tags=["projects"], response_model=Projects)
async def read_project(pid: str):
    return ProjectsController.get(projects_repository, pid)
