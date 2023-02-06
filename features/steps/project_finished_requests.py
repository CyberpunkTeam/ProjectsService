from behave import *

from app.models.auxiliary_models.project_states import ProjectStates
from app.models.auxiliary_models.request_states import RequestStates


@step("el owner a cargo de proyecto crea la solicitud de finalizar el proyecto")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    tid = "2"

    body = {"pid": context.vars["pid"], "tid": tid}
    context.vars["tid"] = tid

    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}

    url = "/project_finished_requests/"

    context.response = context.client.post(url, json=body, headers=headers)

    assert context.response.status_code == 201

    context.vars["pfr_id"] = context.response.json()["pfr_id"]


@then("puedo verificar que se creo que con exito la solicitud de finalizacion")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.response.status_code == 201


@when("pido la solicitud de finalizacion creada")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pfr_id = context.response.json()["pfr_id"]
    url = "/project_finished_requests/" + pfr_id

    context.response = context.client.get(url)
    assert context.response.status_code == 200


@then("puedo ver las solicitud de finalizacion esta pendiente")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.response.json()["state"] == RequestStates.PENDING


@step("el proyecto tiene estado de solicitud de finalizacion enviado")
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
    assert state == ProjectStates.FINISH_REQUEST


@step('el proyecto con nombre "{name}" esta {state_input}')
def step_impl(context, name, state_input):
    """
    :type context: behave.runner.Context
    """
    pid = context.vars["pid"]
    url = f"/projects/{pid}"
    response = context.client.get(url)
    assert response.status_code == 200

    project = response.json()
    state = project.get("state")
    if state_input == "finalizado":
        assert state == ProjectStates.FINISHED
    else:
        assert state == ProjectStates.WIP
