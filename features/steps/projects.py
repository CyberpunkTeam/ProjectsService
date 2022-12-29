import random

from behave import *


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
