import configparser
import time

from behave import *
from selenium.webdriver.common.by import By

from pages.kanbanViewPage import KanbanViewPage
config = configparser.ConfigParser()
config.read(r'config.txt')

val=[]

@when(u'select four opportunities in kanban view')
def step_impl(context):
    context.KVP=KanbanViewPage(context.driver)
    time.sleep(float(config.get('waiting_time', 'avg_wait')))
    context.KVP.select_multiple_opp()



@when(u'click on add label for bulk')
def step_impl(context):
    context.KVP.click_add_label_for_bulk()

@when(u'select label from dropdown and save it')
def step_impl(context):
    context.KVP.select_label()



@then(u'valiadte that labels added by count and by checking in dropdown that all labels are showing')
def step_impl(context):
    assert context.KVP.validate_label_count_and_dropdown_labels()


@when(u'click on Assign Opportunity Owner')
def step_impl(context):
    context.KVP = KanbanViewPage(context.driver)
    context.KVP.click_assign_opportunity_owner()
    # context.driver.find_element(By.XPATH, "(//span[normalize-space()='Assign Opportunity Owner'])[1]").click()



@when(u'select assigning person from dropdown and save it')
def step_impl(context):
    context.KVP.select_assigne_person()

@then(u'validate that assigne person is updated or not')
def step_impl(context):
    assert context.KVP.Is_assigne_person_updated()


