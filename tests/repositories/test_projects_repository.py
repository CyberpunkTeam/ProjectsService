import mongomock

from app import config
from app.models.auxiliary_models.currency import Currency
from app.models.auxiliary_models.description import Description
from app.models.auxiliary_models.technologies import Technologies
from app.models.auxiliary_models.unit_duration import UnitDuration
from app.models.projects import Projects
from app.repositories.projects_repository import ProjectsRepository


@mongomock.patch(servers=(("server.example.com", 27017),))
def test_save_project():
    url = config.DATABASE_URL
    db_name = config.DATABASE_NAME
    repository = ProjectsRepository(url, db_name)

    project = Projects(
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
    )

    ok = repository.insert(project)

    assert ok


@mongomock.patch(servers=(("server.example.com", 27017),))
def test_get_project_by_pid():
    url = config.DATABASE_URL
    db_name = config.DATABASE_NAME
    repository = ProjectsRepository(url, db_name)
    pid = "1"
    project = Projects(
        name="Findmyteam",
        pid=pid,
        description=Description(summary="Platform for matching teams and projects"),
        technologies=Technologies(programming_language=["python"]),
        idioms=["English"],
        creator_uid="1",
        tentative_budget=1000,
        budget_currency=Currency.DOLAR,
        tentative_duration=7,
        unit_duration=UnitDuration.DAYS,
    )

    ok = repository.insert(project)

    assert ok

    project_found = repository.get(pid)

    assert len(project_found) == 1

    project_found = project_found[0]

    assert project_found.name == "Findmyteam"
    assert project_found.pid == "1"
    assert (
        project_found.description.summary == "Platform for matching teams and projects"
    )
    assert project_found.technologies.programming_language == ["python"]
    assert project_found.idioms == ["English"]
    assert project_found.tentative_budget == 1000
    assert project_found.budget_currency == Currency.DOLAR
    assert project_found.tentative_duration == 7
    assert project_found.unit_duration == UnitDuration.DAYS


@mongomock.patch(servers=(("server.example.com", 27017),))
def test_get_project_by_creator_uid():
    url = config.DATABASE_URL
    db_name = config.DATABASE_NAME
    repository = ProjectsRepository(url, db_name)
    pid = "1"
    project = Projects(
        name="Findmyteam",
        pid=pid,
        description=Description(summary="Platform for matching teams and projects"),
        technologies=Technologies(programming_language=["python"]),
        idioms=["English"],
        creator_uid="1",
        tentative_budget=1000,
        budget_currency=Currency.DOLAR,
        tentative_duration=7,
        unit_duration=UnitDuration.DAYS,
    )

    ok = repository.insert(project)

    assert ok

    project_found = repository.get(creator_uid="1")

    assert len(project_found) == 1
