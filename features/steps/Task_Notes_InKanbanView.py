import configparser
import time

from behave import *
from selenium.webdriver.common.by import By

from pages.LeadsPage import LeadsPage
from pages.NotesPage import NotesPage
from pages.kanbanViewPage import KanbanViewPage

config = configparser.ConfigParser()
config.read(r'config.txt')

l=[]
@when(u'click on kanban view button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//app-opportunities-list/div/div[1]/div[2]/button[2]//*[local-name()='svg']").click()
    time.sleep(float(config.get('waiting_time', 'max_wait')))


@when(u'click on dropdown of one opportunity and check it is showing details or not')
def step_impl(context):
    context.KVP=KanbanViewPage(context.driver)
    assert context.KVP.check_opportunity_details_displayed()




@when(u'get text of how many tasks and notes count')
def step_impl(context):
    context.KVP = KanbanViewPage(context.driver)
    context.KVP.get_count()


@when(u'click on that oppportunity')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//div[1]/div/div/div[2]/p[1]").click()
    time.sleep(float(config.get('waiting_time', 'avg_wait')))


@when(u'create task and validate in activity area')
def step_impl(context):
    context.LP = LeadsPage(context.driver)
    context.TP = context.LP.clickOnTasksPage()

    time.sleep(2)
    context.TP.clickOnCreateTask()
    context.TP.enterTaskDetails("interested to site visit", "1640")
    context.TP.clickOnTaskSave()
    assert context.TP.isTaskCreated()


@when(u'create note and validate in activity area')
def step_impl(context):
    context.NP = NotesPage(context.driver)
    context.NP.click_onNotes()
    context.NP.click_On_CreateNotes()
    context.NP.enter_note_in_box("notesDescription in notes box")
    if context.NP.isNoteCreate():
        context.driver.find_element(By.XPATH, "(//span[normalize-space()='Opportunity'])[1]").click()
        time.sleep(float(config.get('waiting_time', 'avg_wait')))
        assert True
    else:
        context.driver.find_element(By.XPATH, "(//span[normalize-space()='Opportunity'])[1]").click()
        time.sleep(float(config.get('waiting_time', 'avg_wait')))
        assert False





@then(u'validate the task and note count is reflected or not in kanban view dropdown')
def step_impl(context):
    assert context.KVP.isTask_Notes_areCreated()
