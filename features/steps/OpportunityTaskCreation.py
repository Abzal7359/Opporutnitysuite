import configparser
import time

from behave import *

from pages.LeadsPage import LeadsPage
from pages.TasksPage import TasksPage
config = configparser.ConfigParser()
config.read(r'config.txt')



@when(u'click on tasks _bar')
def step_impl(context):
    #TP=tasks page
    context.LP=LeadsPage(context.driver)
    context.TP=context.LP.clickOnTasksPage()

    time.sleep(float(config.get('waiting_time', 'min_wait')))




@when(u'click on create _task')
def step_impl(context):
    context.TP.clickOnCreateTask()



@when(u'write task and set task _details')
def step_impl(context):
    for r in context.table:
        context.TP.enterTaskDetails(r["textbox"], r["time"])




@when(u'click task _save')
def step_impl(context):
    context.TP.clickOnTaskSave()


@then(u'ckeck task is created or _not')
def step_impl(context):

    assert context.TP.isTaskCreated()

    time.sleep(2)


#task editing like clone and adding comment


@when(u'click clone task and change priority and save')
def step_impl(context):
    context.TP = TasksPage(context.driver)
    context.TP.click_to_clone_task()




@when(u'check task is cloned or not validate in activity area')
def step_impl(context):
    context.TP = TasksPage(context.driver)
    assert context.TP.isTaskCreated()


@when(u'click on view details on task and add comment')
def step_impl(context):
    context.LP = LeadsPage(context.driver)
    context.TP = context.LP.clickOnTasksPage()
    context.TP.add_comment()


@Then(u'check in activity area')
def step_impl(context):
    context.TP = TasksPage(context.driver)
    assert context.TP.isCommentAddedInTask()