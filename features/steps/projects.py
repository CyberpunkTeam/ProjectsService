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
