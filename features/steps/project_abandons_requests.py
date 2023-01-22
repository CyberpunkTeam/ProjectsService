from behave import *

from app.models.auxiliary_models.project_states import ProjectStates
from app.models.auxiliary_models.request_states import RequestStates


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


@when("actualizo la solicitud de {request_type} a {new_state}")
def step_impl(context, request_type, new_state):
    """
    :param request_type: str
    :poram new_state: str
    :type context: behave.runner.Context
    """
    state = (
        RequestStates.ACCEPTED if new_state == "aceptado" else RequestStates.REJECTED
    )
    context.vars["new_state"] = state
    body = {"state": state}

    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}

    if request_type == "abandonado":
        par_id = context.response.json()["par_id"]
        url = f"/project_abandons_requests/{par_id}"
    else:
        pfr_id = context.response.json()["pfr_id"]
        url = f"/project_finished_requests/{pfr_id}"
    context.response = context.client.put(url, json=body, headers=headers)

    assert context.response.status_code == 200


@then("puedo ver que la solicitud se actualizo correctamente")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    state = context.response.json()["state"]
    assert context.vars["new_state"] == state


@step("el proyecto tiene estado de solicitud de abandono enviado")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pid = context.vars["pid"]
    url = f"/projects/{pid}"
    response = context.client.get(url)
    assert response.status_code == 200

    project = response.json()
    state = project.get("state")
    assert state == ProjectStates.ABANDONS_REQUEST
