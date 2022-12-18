from app.models.projects import Projects


def test_create_project():
    project = Projects(
        name="Findmyteam",
        pid="1",
        description="Platform for matching teams and projects",
        technologies=["python"],
        idioms=["English"],
    )
    assert project.name == "Findmyteam"
    assert project.pid == "1"
    assert project.description == "Platform for matching teams and projects"
    assert project.technologies == ["python"]
    assert project.idioms == ["English"]
