from behave import *


@when("el proyecto finaliza el equipo escribe la review del proyecto")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pid = context.vars["pid"]
    tid = "mock_tid"
    rating = 5
    body = {"pid": pid, "tid": tid, "rating": rating}
    url = "/projects_reviews"
    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}

    context.response = context.client.post(url, json=body, headers=headers)


@then("veo que la review se cargo correctamente")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.response.status_code == 201


@step("el equipo ya escribio la review")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pid = context.vars["pid"]
    tid = "mock_tid"
    rating = 5
    context.vars["rating"] = rating
    body = {"pid": pid, "tid": tid, "rating": rating}
    url = "/projects_reviews"
    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}

    context.response = context.client.post(url, json=body, headers=headers)
    assert context.response.status_code == 201


@when("pido la review del proyecto")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    url = f"/projects_reviews/?pid={context.vars['pid']}"
    context.response = context.client.get(url)


@then("me trae la review")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.response.status_code == 200
    reviews = context.response.json()
    assert len(reviews) == 1
    assert context.vars["rating"] == reviews[0].get("rating")
