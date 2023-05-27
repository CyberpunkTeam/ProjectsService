import os
from typing import List

from fastapi import APIRouter

from app import config
from app.controllers.projects_controller import ProjectsController
from app.models.auxiliary_models.currency import Currency
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
async def list_projects(
    creator_uid: str = None,
    state: ProjectStates = None,
    currency: Currency = None,
    min_budget: float = None,
    max_budget: float = None,
    project_types: str = None,
    idioms: str = None,
    programming_languages: str = None,
    frameworks: str = None,
    platforms: str = None,
    databases: str = None,
    internal_state: str = None,
):
    return ProjectsController.get(
        projects_repository,
        auxiliary_repository,
        creator_uid=creator_uid,
        state=state,
        currency=currency,
        min_budget=min_budget,
        max_budget=max_budget,
        project_types=project_types.split(",")
        if project_types is not None
        else project_types,
        idioms=idioms.split(",") if idioms is not None else idioms,
        programming_languages=programming_languages.split(",")
        if programming_languages is not None
        else programming_languages,
        frameworks=frameworks.split(",") if frameworks is not None else frameworks,
        platforms=platforms.split(",") if platforms is not None else platforms,
        databases=databases.split(",") if databases is not None else databases,
        internal_state=internal_state,
    )


@router.get("/projects/{pid}", tags=["projects"], response_model=Projects)
async def read_project(pid: str):
    return ProjectsController.get(projects_repository, auxiliary_repository, pid)


@router.put("/projects/{pid}", tags=["projects"], response_model=Projects)
async def update_project(pid: str, project_update: ProjectsUpdate):
    return ProjectsController.put(
        projects_repository, auxiliary_repository, pid, project_update
    )
