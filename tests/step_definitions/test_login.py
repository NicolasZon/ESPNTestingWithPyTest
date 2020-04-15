from pytest_bdd import when, then, scenarios

ESPN_HOME_PAGE = "https://www.espn.com/?src=com"


scenarios('../features/login.feature')


@when("the user performs the flow to log into ESPN")
def step_impl():
    raise NotImplementedError(u'STEP: When the user performs the flow to log into ESPN')


@then("the user can see her name in the user section")
def step_impl():
    raise NotImplementedError(u'STEP: Then the user can see her name in the user section')