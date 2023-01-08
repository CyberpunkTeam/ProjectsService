from behave import *


@step("el equipo a cargo de proyecto crea el abandono del proyecto")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    tid = "2"
    reasons = ["poca comunicacion"]
    body = {"pid": context.vars["pid"], "tid": tid, "reasons": reasons}
    context.vars["tid"] = tid
    context.vars["reasons"] = reasons

    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}

    url = "/project_abandonment/"

    context.response = context.client.post(url, json=body, headers=headers)

    assert context.response.status_code == 201


@then("puedo verificar que se creo que con exito el abandono")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.response.status_code == 201


@when("pido el abandono creado")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pa_id = context.response.json()["pa_id"]
    url = "/project_abandonment/" + pa_id

    context.response = context.client.get(url)


@then("puedo ver las razones por las cual se abandono")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    content = context.response.json()
    reasons = content["reasons"]
    assert reasons == context.vars["reasons"]
