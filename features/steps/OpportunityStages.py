
from behave import *

from pages.OpportunityStagesPage import OpportunityStagesPage

lii = []


@when(u'click on opportunity stages under Data mangement')
def step_impl(context):
    context.OSP = OpportunityStagesPage(context.driver)
    context.OSP.click_opportunity_stages_link()
    # context.driver.find_element(By.XPATH,"(//a[normalize-space()='Opportunity Stages'])[1]").click()


@when(u'fill details of stage like stage name')
def step_impl(context):
    context.OSP.add_new_stage("close")


@when(u'set colours of stage')
def step_impl(context):
    context.OSP.set_stage_color()

@then(u'validate stage created or not in opportunity list also')
def step_impl(context):
    assert context.OSP.is_stage_created()


@when(u'back to setting and in opportunity stages')
def step_impl(context):
    context.OSP = OpportunityStagesPage(context.driver)
    context.OSP.navigate_back_to_Opportunity_stages()


@when(u'drag and drop created stage at one step less')
def step_impl(context):
    context.OSP.drag_and_drop_stage()


@then(u'validate the stage position is changed or not in opportunity list also')
def step_impl(context):
    assert context.OSP.validate_stage_position()


@when(u'click disable buttoon')
def step_impl(context):
    context.OSP = OpportunityStagesPage(context.driver)
    context.OSP.click_disable_button()
    # context.driver.find_element(By.XPATH, f"//table/tbody/tr[{afterl - 1}]/td[1]/div/label/div").click()
    # time.sleep(2)


@then(u'validate disabled or not')
def step_impl(context):
    assert context.OSP.is_stage_disabled()

@when(u'click on Add automation')
def step_impl(context):
    context.OSP = OpportunityStagesPage(context.driver)
    context.OSP.click_row_and_add_automation()


@when(u'create automation task')
def step_impl(context):
    context.OSP.create_automation_task()

@when(u'validate task automation created or not')
def step_impl(context):
    assert context.OSP.is_Automation_task_created()

@when(u'create automation of stage changing')
def step_impl(context):
    context.OSP = OpportunityStagesPage(context.driver)
    context.OSP.create_stageChange_automation()

@then(u'validate automation stage created or not')
def step_impl(context):
    assert context.OSP.is_Automation_stage_created()


@when(u'click on delete the stage')
def step_impl(context):
    context.OSP = OpportunityStagesPage(context.driver)
    context.OSP.delete_stage()

@then(u'validate created stage deleted or not')
def step_impl(context):
    assert context.OSP.validate_stage_deletion()
