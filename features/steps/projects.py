import random

from behave import *

from app.models.auxiliary_models.project_states import ProjectStates


@given("que quiero crear un proyecto")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when(
    'completo alta de proyecto, con nombre "{name}", idiomas "{idioms}", descripcion "{description}" y tenologias "{technologies}"'
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
        "description": description,
        "technologies": technologies.split(","),
        "creator_uid": "1",
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


@given(
    'que existe el proyecto con nombre "{name}", idiomas "{idioms}", descripcion "{description}" y tenologias "{technologies}"'
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
        "description": description,
        "technologies": technologies.split(","),
        "creator_uid": f"{random.randint(1, 500)}",
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
    'edito el nombre del proyecto a "{name}", idiomas "{idioms}", descripcion "{description}" y tenologias "{'
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
        "description": description,
        "technologies": technologies.split(","),
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
    'veo que tiene nombre "{name}", idiomas "{idioms}", descripcion "{description}" y tenologias "{technologies}"'
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
    assert project_updated.get("description") == description
    assert project_updated.get("technologies") == technologies.split(",")


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
