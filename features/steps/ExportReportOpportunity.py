from behave import*

from pages.ExportReportPage import ExportReportPage


@when(u'click on _Export')
def step_impl(context):
    #-----------------------------------------------
    context.EP=ExportReportPage(context.driver)
    context.EP.click_export_button()


@when(u'now select which columns you need in _report')
def step_impl(context):
    context.EP.select_export_column()

@when(u'click on export _button')
def step_impl(context):
    context.EP.click_SAVE_button()


@when(u'now go to downloads _section')
def step_impl(context):
    context.EP.navigate_to_downloads_section()



@then(u'here validate report generated or _not')
def step_impl(context):
    assert context.EP.is_report_created()




