from app.models.auxiliary_models.currency import Currency
from app.models.auxiliary_models.description import Description
from app.models.auxiliary_models.technologies import Technologies
from app.models.auxiliary_models.unit_duration import UnitDuration
from app.models.projects import Projects


def test_create_project():
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
    assert project.name == "Findmyteam"
    assert project.pid == "1"
    assert project.description.summary == "Platform for matching teams and projects"
    assert project.technologies.programming_language == ["python"]
    assert project.idioms == ["English"]
    assert project.tentative_budget == 1000
    assert project.budget_currency == Currency.DOLAR
    assert project.tentative_duration == 7
    assert project.unit_duration == UnitDuration.DAYS
