import os
from typing import List

from fastapi import APIRouter

from app import config
from app.controllers.projects_controller import ProjectsController
from app.models.auxiliary_models.project_states import ProjectStates
from app.models.projects import Projects
from app.models.requests.project_update import ProjectsUpdate
from app.repositories.projects_repository import ProjectsRepository
from app.routers import auxiliary_repository

router = APIRouter()

# Repository
projects_repository = ProjectsRepository(config.DATABASE_URL, config.DATABASE_NAME)


@router.post("/projects/reset", tags=["team_invitations"], status_code=200)
async def reset():
    if os.environ.get("TEST_MODE") == "1":
        return {"reset": projects_repository.reset() and auxiliary_repository.reset()}


@router.post("/projects/", tags=["projects"], response_model=Projects, status_code=201)
async def create_project(user: Projects):
    return ProjectsController.post(projects_repository, auxiliary_repository, user)


@router.get("/projects/", tags=["projects"], response_model=List[Projects])
async def list_projects(creator_uid: str = None, state: ProjectStates = None):
    return ProjectsController.get(
        projects_repository, auxiliary_repository, creator_uid=creator_uid, state=state
    )


@router.get("/projects/{pid}", tags=["projects"], response_model=Projects)
async def read_project(pid: str):
    return ProjectsController.get(projects_repository, auxiliary_repository, pid)


@router.put("/projects/{pid}", tags=["projects"], response_model=Projects)
async def update_project(pid: str, project_update: ProjectsUpdate):
    return ProjectsController.put(
        projects_repository, auxiliary_repository, pid, project_update
    )
