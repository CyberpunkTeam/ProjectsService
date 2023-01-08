from behave import *


@step("el owner a cargo de proyecto crea la solicitud de abandono del proyecto")
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

    url = "/project_abandons_requests/"

    context.response = context.client.post(url, json=body, headers=headers)

    assert context.response.status_code == 201


@then("puedo verificar que se creo que con exito la solicitud de abandono")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.response.status_code == 201


@when("pido la solicitud de abandono creada")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    par_id = context.response.json()["par_id"]
    url = "/project_abandons_requests/" + par_id

    context.response = context.client.get(url)
