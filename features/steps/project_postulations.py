from behave import *

from app.models.auxiliary_models.states import States


@given('que quiero postular a mi equipo "{team_name}" al projecto "{project_name}"')
def step_impl(context, team_name, project_name):
    """
    :param team_name: str
    :param project_name: str
    :type context: behave.runner.Context
    """
    context.vars["tid"] = len(team_name)
    context.vars[f"{team_name}_tid"] = str(len(team_name))


@when(
    "completo el formulario de postulacion con presupuesto estimado {budget} {currency}"
)
def step_impl(context, budget, currency):
    """
    :param budget: str
    :param currency: str
    :type context: behave.runner.Context
    """
    currencies = {"pesos": "PESO_ARG", "dolares": "DOLAR"}
    context.vars["postulation"] = {
        "pid": context.vars["pid"],
        "tid": context.vars["tid"],
        "currency": currencies[currency],
        "estimated_budget": int(budget),
    }


@step('descripcion de propuesta "{proposal_description}"')
def step_impl(context, proposal_description):
    """
    :param proposal_description: str
    :type context: behave.runner.Context
    """
    body = context.vars["postulation"]
    body["proposal_description"] = proposal_description


@step("envio postulacion")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}

    url = "/projects/postulations/"

    context.response = context.client.post(
        url, json=context.vars["postulation"], headers=headers
    )


@then("se confirma que se envio la propuesta")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.response.status_code == 201


@step('que el equipo "{team_name}" se postulo mi projecto "{project_name}"')
def step_impl(context, team_name, project_name):
    """
    :param team_name: str
    :param project_name: str
    :type context: behave.runner.Context
    """
    context.vars[f"{team_name}_tid"] = str(len(team_name))
    context.vars["tid"] = str(len(team_name))
    currencies = {"pesos": "PESO_ARG", "dolares": "DOLAR"}
    body = {
        "pid": context.vars["pid"],
        "tid": context.vars["tid"],
        "currency": currencies["pesos"],
        "estimated_budget": 100,
        "proposal_description": "description",
    }

    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}

    url = "/projects/postulations/"

    response = context.client.post(url, json=body, headers=headers)

    assert response.status_code == 201
    context.vars["ppid"] = response.json()["ppid"]


@when('pido los postulados a mi proyecto "{project_name}"')
def step_impl(context, project_name):
    """
    :param project_name: str
    :type context: behave.runner.Context
    """
    url = f"/projects/postulations/?pid={context.vars['pid']}"
    context.response = context.client.get(url)


@then('recibo que el equipo "{team_name}" se postulo')
def step_impl(context, team_name):
    """
    :param team_name: str
    :type context: behave.runner.Context
    """
    tid = context.vars[f"{team_name}_tid"]
    postulations = context.response.json()
    tids = []
    for postulation in postulations:
        tids.append(postulation.get("tid"))

    assert tid in tids


@when('pido los postulados de mi equipo "{team_name}"')
def step_impl(context, team_name):
    """
    :param team_name: str
    :type context: behave.runner.Context
    """
    url = f"/projects/postulations/?tid={len(team_name)}"
    context.response = context.client.get(url)


@then('recibo el proyecto "{project_name}"')
def step_impl(context, project_name):
    """
    :param project_name: str
    :type context: behave.runner.Context
    """
    pid = context.vars[f"{project_name}_pid"]
    postulations = context.response.json()
    pids = []
    for postulation in postulations:
        pids.append(postulation.get("pid"))

    assert pid in pids


@when("{state} la postulacion")
def step_impl(context, state):
    """
    :param state: str
    :type context: behave.runner.Context
    """
    states = {"acepto": States.ACCEPTED, "cancelo": States.REJECTED}
    body = {"state": states[state]}
    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}

    url = f"/projects/postulations/{context.vars['ppid']}"

    context.response = context.client.put(url, json=body, headers=headers)

    assert context.response.status_code == 200


@then("la postulacion figura como {state}")
def step_impl(context, state):
    """
    :param state: str
    :type context: behave.runner.Context
    """
    states = {"aceptada": States.ACCEPTED, "cancelada": States.REJECTED}
    body = context.response.json()
    assert body.get("state") == states[state]
