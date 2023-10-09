from behave import *

from pages.NotesPage import NotesPage




@when(u'clickon Notes _taskbar')
def step_impl(context):
    context.NP=NotesPage(context.driver)
    context.NP.click_onNotes()


@when(u'click on create _notes')
def step_impl(context):
    context.NP.click_On_CreateNotes()


@when(u'write description in notes and _save')
def step_impl(context):
    for i in context.table:
        context.NP.enter_note_in_box(i["notesDescription"])

@then(u'check the note is created or _not')
def step_impl(context):
    context.NP = NotesPage(context.driver)
    assert context.NP.isNoteCreate()