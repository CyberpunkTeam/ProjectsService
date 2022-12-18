import mongomock

from app import config
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
        description="Platform for matching teams and projects",
        technologies=["python"],
        idioms=["English"],
    )

    ok = repository.insert(project)

    assert ok


@mongomock.patch(servers=(("server.example.com", 27017),))
def test_get_user():
    url = config.DATABASE_URL
    db_name = config.DATABASE_NAME
    repository = ProjectsRepository(url, db_name)
    pid = "1"
    project = Projects(
        name="Findmyteam",
        pid=pid,
        description="Platform for matching teams and projects",
        technologies=["python"],
        idioms=["English"],
    )

    ok = repository.insert(project)

    assert ok

    project_found = repository.get(pid)

    assert len(project_found) == 1

    project_found = project_found[0]

    assert project_found.name == "Findmyteam"
    assert project_found.pid == "1"
    assert project_found.description == "Platform for matching teams and projects"
    assert project_found.technologies == ["python"]
    assert project_found.idioms == ["English"]
