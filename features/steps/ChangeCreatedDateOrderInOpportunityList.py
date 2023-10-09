import configparser
import time

from behave import *

from pages.ChangeCreatedDateOrderInLeadsListPage import ChangeCreatedDateOrderInLeadsListPage
from pages.EditOpportunityDetailsFromListPage import EditOpportunityDetailsFromListPage
config = configparser.ConfigParser()
config.read(r'config.txt')



@when(u'clickon Opportunity button to back to opportunity')
def step_impl(context):
    context.EOPD = EditOpportunityDetailsFromListPage(context.driver)
    context.EOPD.click_opportunity_link()




@when(u'click on descending date _button')
def step_impl(context):
    context.CD=ChangeCreatedDateOrderInLeadsListPage(context.driver)
    context.CD.click_descending_date_buttonn()


@then(u'validate dates in descending order or _not')
def step_impl(context):
    assert context.CD.is_in_descendingOrder()
    time.sleep(float(config.get('waiting_time', 'avg_wait')))


@when(u'click on ascending date _button')
def step_impl(context):
    context.CD = ChangeCreatedDateOrderInLeadsListPage(context.driver)
    context.CD.click_ascending_date_buttonn()


@then(u'validate dates in ascending order or _not')
def step_impl(context):
    context.CD = ChangeCreatedDateOrderInLeadsListPage(context.driver)
    assert context.CD .is_in_ascendingOrder()


