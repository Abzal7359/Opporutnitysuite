import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
class NotesPage:
    def __init__(self,driver):
        self.driver=driver
    NotesTaskBar_XPATH="(//a[@id='notes'])[1]"
    createNotes_XPATH="(//button[normalize-space()='Create Notes'])[1]"
    notes_box_XPATH="(//div[@class='angular-editor-textarea'])[1]"
    notesSave_button="//button[@type='submit']"
    closePopUp_XPATH="/html/body/app-root/app-layout/div/div/main/div/app-view-lead/div/div[2]/div/main/div[2]/div/app-notes/div/div[3]/div[1]/app-task-alert/div/div[2]/div/div/div[2]/button[1]"
    noteIsCreated_XPATH="//div[@class='bg-white mt-2 pr-4 rounded-md ml-4 mb-4 ng-star-inserted']"

    List_notes=[]

    def click_onNotes(self):

        self.driver.find_element(By.XPATH,self.NotesTaskBar_XPATH).click()
        time.sleep(2)
    def click_On_CreateNotes(self):
        self.driver.find_element(By.XPATH,self.createNotes_XPATH).click()
        time.sleep(2)
        # time.sleep(1)
    def enter_note_in_box(self,description):
        self.driver.find_element(By.XPATH, self.notes_box_XPATH).clear()
        self.driver.find_element(By.XPATH, self.notes_box_XPATH).send_keys(description)
        time.sleep(2)
        #adding doc
        # self.driver.find_element(By.XPATH, "//*[@id='file-upload - ']").send_keys(
        #     "C://Users/abzalhussain/Desktop/builldingone.jpg")
        # time.sleep(3)
        # wt = WebDriverWait(self.driver, 10)
        # element = wt.until(
        #     EC.element_to_be_clickable((By.XPATH, "//app-add-note/form/div/div/div/span//*[local-name()='svg']")))
        # element.click()
        #
        # self.driver.find_element(By.XPATH, "//*[@id='file-upload - ']").send_keys(
        #     "C://Users/abzalhussain/Desktop/building.jpg")
        # time.sleep(3)
        #
        self.driver.find_element(By.XPATH, self.notesSave_button).click()
        time.sleep(2)
        c = self.driver.find_element(By.XPATH, "//a[@id='activities']")
        self.driver.execute_script("arguments[0].click()", c)
        time.sleep(2)
        self.click_onNotes()



    def isNoteCreate(self):
        l = self.driver.find_elements(By.XPATH, self.noteIsCreated_XPATH)
        #below line to val doc
        # dd = self.driver.find_element(By.XPATH, "//app-notes/div/div[3]/div/div[1]/div/div/div[3]/div").is_displayed()
        if len(l) >= 1 :                       #and dd:  keep this to val doc
            self.List_notes.append(True)
        else:
            self.List_notes.append(False)

            # task created or not validating in activity page
        c = self.driver.find_element(By.XPATH, "//a[@id='activities']")
        self.driver.execute_script("arguments[0].click()", c)
        time.sleep(2)
        expectedd = "Note added"
        actuall = self.driver.find_element(By.XPATH,
                                           "(//div[contains(@class,'flex flex-row justify-between px-2')]//p[@class='font-medium text-sm ng-star-inserted'])").text
        if expectedd in actuall:
            self.List_notes.append(True)
        else:
            self.List_notes.append(False)
            # self.driver.find_element(By.XPATH, self.).click()
        time.sleep(2)
        if False not in self.List_notes:

            return True
        else:

            return False


