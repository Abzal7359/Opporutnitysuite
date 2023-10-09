from behave import *

from pages.AddDocumentPage import AddDocumentPage


@when(u'user clicks on Document _option')
def step_impl(context):
    # ADCP=adddocumentpage
    context.ADCP = AddDocumentPage(context.driver)
    context.ADCP.click_document_option()


@when(u'in that page he clicks Add _Documents')
def step_impl(context):
    context.ADCP.click_add_documents_button()


@when(u'user upload file _here')
def step_impl(context):
    context.ADCP.upload_file("C://Users/abzalhussain/Desktop/download.jpeg")


@when(u'clicks _save')
def step_impl(context):
    context.ADCP.click_save_button()


@then(u'check wheather the file is uploaded or _not')
def step_impl(context):
    assert context.ADCP.check_uploaded_files()