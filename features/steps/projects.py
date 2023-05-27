import random

from behave import *

from app.models.auxiliary_models.actions import Actions
from app.models.auxiliary_models.activities_record import ActivitiesRecord
from app.models.auxiliary_models.currency import Currency
from app.models.auxiliary_models.internal_states import InternalStates
from app.models.auxiliary_models.project_states import ProjectStates
from app.models.auxiliary_models.unit_duration import UnitDuration


@given("que quiero crear un proyecto")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when(
    'completo alta de proyecto, con nombre "{name}", idiomas "{idioms}", descripcion "{description}", presupuesto "{tentative_budget}" {currency}, con duracion tentativa de {duration} {unit_duration} y tenologias "{technologies}"'
)
def step_impl(
    context,
    name,
    idioms,
    description,
    tentative_budget,
    currency,
    duration,
    unit_duration,
    technologies,
):
    """
    :param name: str
    :param idioms:str
    :param description:str
    .param technologies:str
    :type context: behave.runner.Context
    """
    context.vars["project_to_save"] = {
        "name": name,
        "idioms": idioms.split(","),
        "description": {"summary": description},
        "technologies": {"programming_language": technologies.split(",")},
        "creator_uid": "1",
        "tentative_budget": float(tentative_budget),
        "budget_currency": Currency.DOLAR if currency == "dolares" else Currency.EURO,
        "tentative_duration": int(duration),
        "unit_duration": UnitDuration.DAYS
        if unit_duration == "dias"
        else UnitDuration.MONTHS,
    }


@step("confirmo la creacion")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}

    url = "/projects"

    context.response = context.client.post(
        url, json=context.vars["project_to_save"], headers=headers
    )


@then("se me informa que se creo exitosamente")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.response.status_code == 201
    body = context.response.json()
    assert body.get("state") == ProjectStates.PENDING
    assert body.get("internal_state") == InternalStates.ACTIVE
    assert len(body.get("activities_record")) == 1
    activity = body.get("activities_record")[0]
    activity_expected = ActivitiesRecord(action=Actions.CREATED, pid="fake")
    activity_expected.complete()
    assert activity.get("description") == activity_expected.description


@given(
    'que existe el proyecto con nombre "{name}", idiomas "{idioms}", descripcion "{description}" y tecnologias "{technologies}"'
)
def step_impl(context, name, idioms, description, technologies):
    """
    :param name: str
    :param idioms:str
    :param description:str
    .param technologies:str
    :type context: behave.runner.Context
    """
    context.vars["project_to_save"] = {
        "name": name,
        "idioms": idioms.split(","),
        "description": {"summary": description},
        "technologies": {"programming_language": technologies.split(",")},
        "creator_uid": f"{random.randint(1, 500)}",
        "tentative_budget": float(1000),
        "budget_currency": Currency.DOLAR,
        "tentative_duration": int(7),
        "unit_duration": UnitDuration.DAYS,
    }

    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}

    url = "/projects"

    context.response = context.client.post(
        url, json=context.vars["project_to_save"], headers=headers
    )

    assert context.response.status_code == 201
    context.vars["pid"] = context.response.json()["pid"]
    context.vars[f"{name}_pid"] = context.response.json()["pid"]


@when(
    'edito el nombre del proyecto a "{name}", idiomas "{idioms}", descripcion "{description}" y tecnologias "{'
    'technologies}"'
)
def step_impl(context, name, idioms, description, technologies):
    """
    :param name: str
    :param idioms:str
    :param description:str
    .param technologies:str
    :type context: behave.runner.Context
    """
    context.vars["project_to_save"] = {
        "name": name,
        "idioms": idioms.split(","),
        "description": {"summary": description},
        "technologies": {"programming_language": technologies.split(",")},
    }

    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}

    url = f"/projects/{context.vars['pid']}"

    context.response = context.client.put(
        url, json=context.vars["project_to_save"], headers=headers
    )


@then("se me informa que se actualizo correctamente")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.response.status_code == 200


@step(
    'veo que tiene nombre "{name}", idiomas "{idioms}", descripcion "{description}" y tecnologias "{technologies}"'
)
def step_impl(context, name, idioms, description, technologies):
    """

    :param name: str
    :param idioms: str
    :param description: str
    :param technologies: str
    :type context: behave.runner.Context
    """
    project_updated = context.response.json()
    assert project_updated.get("name") == name
    assert project_updated.get("idioms") == idioms.split(",")
    assert project_updated.get("description").get("summary") == description
    assert project_updated.get("technologies").get(
        "programming_language"
    ) == technologies.split(",")


@when('edito el estado a "{new_state}"')
def step_impl(context, new_state):
    """
    :param new_state: str
    :type context: behave.runner.Context
    """
    body_to_update = {"state": context.vars["states2english"].get(new_state)}
    context.vars["body_to_update"] = body_to_update
    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}

    url = f"/projects/{context.vars['pid']}"

    context.response = context.client.put(url, json=body_to_update, headers=headers)


@step('veo que tiene el estado "{new_state}"')
def step_impl(context, new_state):
    """
    :param new_state: str
    :type context: behave.runner.Context
    """

    project_updated = context.response.json()
    assert project_updated.get("state") == context.vars["states2english"].get(new_state)

    action = ""
    if new_state == "finalizado":
        action = Actions.FINISHED
    elif new_state == "cancelado":
        action = Actions.CANCELLED
    if action != "":
        activity = project_updated.get("activities_record")[1]
        activity_expected = ActivitiesRecord(action=action, pid="fake")
        activity_expected.complete()
        assert activity.get("description") == activity_expected.description


@when('cuando pido todos los proyectos con estado "{state}"')
def step_impl(context, state):
    """
    :param state: str
    :type context: behave.runner.Context
    """
    url = f"/projects/?state={context.vars.get('states2english').get(state)}"

    context.response = context.client.get(url)


@then("me retorna {amount} proyectos")
def step_impl(context, amount):
    """
    :param amount: int
    :type context: behave.runner.Context
    """
    assert context.response.status_code == 200
    projects = context.response.json()
    assert len(projects) == int(amount)


@given(
    'que existe el proyecto con nombre "{name}" y tipo "{project_type}", idiomas "{idioms}", descripcion "{description}", tecnologias "{programming_language}", framework "{frameworks}" y presupuesto de {budget} {currency}'
)
def step_impl(
    context,
    name,
    project_type,
    idioms,
    description,
    programming_language,
    frameworks,
    budget,
    currency,
):
    """
    :param currency:
    :param budget:
    :param frameworks:
    :param programming_language:
    :param description:
    :param project_type:
    :param idioms:
    :type context: behave.runner.Context
    """
    context.vars["project_to_save"] = {
        "name": name,
        "idioms": idioms.split(","),
        "description": {"summary": description},
        "technologies": {
            "programming_language": programming_language.split(","),
            "frameworks": frameworks.split(","),
        },
        "creator_uid": f"{random.randint(1, 500)}",
        "tentative_budget": float(budget),
        "budget_currency": currency,
        "tentative_duration": int(7),
        "unit_duration": UnitDuration.DAYS,
        "project_type": project_type,
    }

    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}

    url = "/projects"

    context.response = context.client.post(
        url, json=context.vars["project_to_save"], headers=headers
    )

    assert context.response.status_code == 201
    context.vars["pid"] = context.response.json()["pid"]
    context.vars[f"{name}_pid"] = context.response.json()["pid"]


@when('filtro por proyectos con tecnologia "{programming_languages}"')
def step_impl(context, programming_languages):
    """
    :param programming_languages:
    :type context: behave.runner.Context
    """
    query_params = f"?programming_languages={programming_languages}"

    url = "/projects" + query_params

    context.response = context.client.get(url)


@when(
    'filtro por proyectos con tecnologia "{programming_languages}", presupuesto entre {min_budget} y {max_budget} {currency}.'
)
def step_impl(context, programming_languages, min_budget, max_budget, currency):
    """
    :param currency:
    :param max_budget:
    :param min_budget:
    :param programming_languages:
    :type context: behave.runner.Context
    """
    query_params = f"?programming_languages={programming_languages}&min_budget={min_budget}&max_budget={max_budget}&currency={currency}"

    url = "/projects" + query_params

    context.response = context.client.get(url)


@step('edito el estado interno a "{state}"')
def step_impl(context, state):
    """
    :type context: behave.runner.Context
    """
    state = "BLOCKED" if state == "bloqueado" else "ACTIVE"
    body_to_update = {"internal_state": state}
    context.vars["body_to_update"] = body_to_update
    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}

    url = f"/projects/{context.vars['pid']}"

    context.response = context.client.put(url, json=body_to_update, headers=headers)


@step('veo que tiene el estado interno "{state}"')
def step_impl(context, state):
    """
    :type context: behave.runner.Context
    """
    state = "BLOCKED" if state == "bloqueado" else "ACTIVE"
    project_updated = context.response.json()
    assert project_updated.get("internal_state") == state
