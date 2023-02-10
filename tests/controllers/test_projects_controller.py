from unittest.mock import Mock

import pytest
from fastapi import HTTPException

from app.controllers.projects_controller import ProjectsController
from app.models.auxiliary_models.currency import Currency
from app.models.auxiliary_models.description import Description
from app.models.auxiliary_models.technologies import Technologies
from app.models.auxiliary_models.unit_duration import UnitDuration
from app.models.projects import Projects


def test_get_all_projects():
    repository = Mock()
    repository.get.return_value = [
        Projects(
            name="Findmyteam",
            pid="1",
            description=Description(summary="Platform for matching teams and projects"),
            technologies=Technologies(programming_language=["python"]),
            idioms=["English"],
            creator_uid="1",
            tentative_budget=1000,
            budget_currency=Currency.DOLAR,
            tentative_duration=7,
            unit_duration=UnitDuration.DAYS,
        ),
        Projects(
            name="Findmyteam",
            pid="2",
            description=Description(summary="Platform for matching teams and projects"),
            technologies=Technologies(programming_language=["python"]),
            idioms=["English"],
            creator_uid="1",
            tentative_budget=1000,
            budget_currency=Currency.DOLAR,
            tentative_duration=7,
            unit_duration=UnitDuration.DAYS,
        ),
    ]
    result = ProjectsController.get(repository, repository)
    assert len(result) == 2


def test_get_project():
    repository = Mock()
    repository.get.return_value = [
        Projects(
            name="Findmyteam",
            pid="1",
            description=Description(summary="Platform for matching teams and projects"),
            technologies=Technologies(programming_language=["python"]),
            idioms=["English"],
            creator_uid="1",
            tentative_budget=1000,
            budget_currency=Currency.DOLAR,
            tentative_duration=7,
            unit_duration=UnitDuration.DAYS,
        ),
        Projects(
            name="Findmyteam",
            pid="2",
            description=Description(summary="Platform for matching teams and projects"),
            technologies=Technologies(programming_language=["python"]),
            idioms=["English"],
            creator_uid="1",
            tentative_budget=1000,
            budget_currency=Currency.DOLAR,
            tentative_duration=7,
            unit_duration=UnitDuration.DAYS,
        ),
    ]
    result = ProjectsController.get(repository, repository, "1")
    assert result.name == "Findmyteam"


def test_error_project_not_found():
    repository = Mock()
    repository.get.return_value = []
    with pytest.raises(HTTPException):
        ProjectsController.get(repository, repository, pid="1")


def test_create_project():
    repository = Mock()
    repository.insert.return_value = True
    project = Projects(
        name="Findmyteam",
        pid="2",
        description=Description(summary="Platform for matching teams and projects"),
        technologies=Technologies(programming_language=["python"]),
        idioms=["English"],
        creator_uid="1",
        tentative_budget=1000,
        budget_currency=Currency.DOLAR,
        tentative_duration=7,
        unit_duration=UnitDuration.DAYS,
    )
    result = ProjectsController.post(repository, repository, project)
    assert result == project


def test_error_create_user():
    repository = Mock()
    repository.insert.return_value = False
    project = Projects(
        name="Findmyteam",
        pid="2",
        description=Description(summary="Platform for matching teams and projects"),
        technologies=Technologies(programming_language=["python"]),
        idioms=["English"],
        creator_uid="1",
        tentative_budget=1000,
        budget_currency=Currency.DOLAR,
        tentative_duration=7,
        unit_duration=UnitDuration.DAYS,
    )
    with pytest.raises(HTTPException):
        ProjectsController.post(repository, repository, project)
