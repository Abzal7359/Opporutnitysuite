from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC

from pages.LeadLabelsConfiguratorPage import LeadLabelsConfiguratorPage


class OpportunityStagesPage:
    def __init__(self, driver):
        self.driver = driver

    OPPORTUNITY_STAGES_LINK = (By.XPATH, "(//a[normalize-space()='Opportunity Stages'])[1]")
    ADD_NEW_STAGE_BUTTON = (By.XPATH, "//div[text()=' Add New Stage ']")
    STAGE_NAME_INPUT = (By.XPATH, "//input[@id='stageName']")
    COLOR_PICKER = (By.XPATH, "//app-opportunites-stage-automation/div[2]/div/div[2]/div/div[1]")
    COLOR_OPTION = (By.XPATH, "//app-opportunites-stage-automation/div[2]/div/div[2]/div/div[1]/div[2]/div[14]")
    SAVE_BUTTON = (By.XPATH, "//button[normalize-space()='Save']")
    IN_OPPORTUNITY_STAGE_ROW = (By.XPATH, "//tbody/tr[1]/td[6]/div[1]/span[1]")
    BACK_TO_SETTINGS_BUTTON = (By.XPATH, "//app-topbar/div/div/div[2]/div[1]/img")
    DISABLE_BUTTON = (By.XPATH, "//table/tbody/tr[{}]/td[1]/div/label/div")
    STAGE_TEXT = (By.XPATH, "//table/tbody/tr[{}]/td[2]/div/span")
    ROW_TO_CLICK_XPATH = "//tbody/tr[{}]/td[3]/strong"

    ADD_AUTOMATION_BUTTON_XPATH = (By.XPATH, "//button[normalize-space()='Add Automation']")
    TRIGGER_TYPE_STAGE_XPATH = (By.XPATH, "//p[normalize-space()='Stage']")
    TASK_OPTION_XPATH = "//p[normalize-space()='Task']"
    DESCRIPTION_TEXTAREA_XPATH = "//textarea[@id='description']"
    AFTER_TRIGGER_TIME = "//input[@placeholder='0']"
    ADD_TASK_LABEL_XPATH = "//label[text()='Task ']"
    PRIORITY_OPTION_XPATH = "//label[normalize-space()='Very High']"
    UPDATE_BUTTON_XPATH = "//button[normalize-space()='Update']"
    STAGE_OPTION_XPATH = (By.XPATH, "//label[normalize-space()='Final Call']")
    SUCCESS_TOASTER_MESSAGE_XPATH = (By.XPATH, "//app-toasts-container/div/div/div/div/div/div[2]/p[2]")
    DELETE_STAGE_XPATH = "//tbody/tr[{}]/td[4]//*[local-name()='svg']"

    def validate_stage_deletion(self):
        # Get the current number of stages
        current_stage_count = len(
            self.driver.find_elements(By.XPATH, "//table/tbody/tr/td[1]/div//*[local-name()='svg']"))
        flag=True
        for i in range(2,current_stage_count+1):
            c=self.driver.find_element(By.XPATH,f"//tbody/tr[{i}]/td[2]/div/span[1]").text
            if c==stage_name:
                flag=False



        # Validate whether the stage was deleted successfully
        return current_stage_count == l or flag

    def delete_stage(self):
        self.driver.find_element(By.XPATH, f"//tbody/tr[{afterl}]/td[3]/div/div[2]/strong").click()
        self.driver.find_element(By.XPATH,"(//tbody/tr/td[3]/div/span[2]//*[local-name()='svg'] )[1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"(//tbody/tr/td[3]/div/span[2]//*[local-name()='svg'] )[1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.UPDATE_BUTTON_XPATH).click()
        time.sleep(2)
        # Click on the delete stage icon
        delete_icon_xpath = self.DELETE_STAGE_XPATH.format(afterl)
        self.driver.find_element(By.XPATH, delete_icon_xpath).click()
        time.sleep(5)

    def is_Automation_stage_created(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(self.SUCCESS_TOASTER_MESSAGE_XPATH))

        bol = element.text
        success = "OpportunityStage Automation Rule Created Successfully."
        count_of_task = int(
            self.driver.find_element(By.XPATH, f"//tbody/tr[{afterl}]/td[3]/div/div[2]/strong").text)
        return success == bol and count_of_task == 1

    def create_stageChange_automation(self):
        self.driver.find_element(By.XPATH, f"//tbody/tr[{afterl}]/td[3]/div/div[2]/strong").click()
        self.driver.find_element(*self.ADD_AUTOMATION_BUTTON_XPATH).click()
        self.driver.find_element(*self.TRIGGER_TYPE_STAGE_XPATH).click()
        self.driver.find_element(By.XPATH, self.AFTER_TRIGGER_TIME).send_keys(1)
        vv = self.driver.find_element(By.XPATH, "//div[2]/div/div[4]/div/div/div/div[2]/div[2]/div/button")
        self.driver.execute_script("arguments[0].click()", vv)
        self.driver.find_element(*self.STAGE_OPTION_XPATH).click()
        self.driver.find_element(By.XPATH, self.UPDATE_BUTTON_XPATH).click()

    def is_Automation_task_created(self):
        # bol = context.driver.find_element(By.XPATH, "//app-toasts-container/div/div/div/div/div/div[2]/p[2]").text
        # success = "OpportunityStage Automation Rule Created Successfully."
        time.sleep(1)
        count_of_task = int(
            self.driver.find_element(By.XPATH, f"//tbody/tr[{afterl}]/td[3]/div/div[1]/strong").text)
        return count_of_task == 1

    def create_automation_task(self):
        self.driver.find_element(By.XPATH, self.TASK_OPTION_XPATH).click()

        # Fill in the description
        description_input = self.driver.find_element(By.XPATH, self.DESCRIPTION_TEXTAREA_XPATH)
        description_input.send_keys("please close him")
        self.driver.find_element(By.XPATH, self.AFTER_TRIGGER_TIME).send_keys(1)
        xx = self.driver.find_element(By.XPATH, "//div[2]/div/div[4]/div/div/div[2]/div[2]/div/div/button")
        self.driver.execute_script("arguments[0].click()", xx)
        self.driver.find_element(By.XPATH, "(//app-select-dropdown/div/div/div/div/label)[2]").click()
        self.driver.find_element(By.XPATH, "//input[@placeholder='Input no. of days']").send_keys(1)
        zz = self.driver.find_element(By.XPATH, "//div[2]/div/div[4]/div/div/div[2]/div[4]/div/div/button")
        self.driver.execute_script("arguments[0].click()", zz)
        # Click the "Add Task" label
        self.driver.find_element(By.XPATH, self.ADD_TASK_LABEL_XPATH).click()
        yy = self.driver.find_element(By.XPATH, "//div[2]/div/div[4]/div/div/div[2]/div[5]/div/div/button")
        self.driver.execute_script("arguments[0].click()", yy)
        # Select priority option
        self.driver.find_element(By.XPATH, self.PRIORITY_OPTION_XPATH).click()
        # Click the "Update" button
        self.driver.find_element(By.XPATH, self.UPDATE_BUTTON_XPATH).click()
        time.sleep(2)

    def click_row_and_add_automation(self):
        row_xpath = self.ROW_TO_CLICK_XPATH.format(afterl)
        self.driver.find_element(By.XPATH, row_xpath).click()
        time.sleep(2)
        self.driver.find_element(*self.ADD_AUTOMATION_BUTTON_XPATH).click()

    def click_opportunity_stages_link(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.OPPORTUNITY_STAGES_LINK)).click()

    def add_new_stage(self, stage_namee):
        global l
        global stage_name
        stage_name = stage_namee
        l = len(self.driver.find_elements(By.XPATH, "//table/tbody/tr/td[1]/div//*[local-name()='svg']"))
        self.driver.find_element(*self.ADD_NEW_STAGE_BUTTON).click()
        stage_name_input = self.driver.find_element(*self.STAGE_NAME_INPUT)
        stage_name_input.send_keys(stage_name)
        time.sleep(2)

    def set_stage_color(self):
        color_picker = self.driver.find_element(*self.COLOR_PICKER)
        color_picker.click()
        color_option = self.driver.find_element(*self.COLOR_OPTION)
        color_option.click()
        save_button = self.driver.find_element(*self.SAVE_BUTTON)
        save_button.click()
        time.sleep(3)

    def is_stage_created(self):
        global afterl
        afterl = len(self.driver.find_elements(By.XPATH, "//table/tbody/tr/td[1]/div//*[local-name()='svg']"))

        LLC = LeadLabelsConfiguratorPage(self.driver)
        LLC.navigate_to_opportunity_list()

        self.driver.find_element(*self.IN_OPPORTUNITY_STAGE_ROW).click()

        optext = self.driver.find_element(By.XPATH, f"//app-select-dropdown/div/div/div/div[{afterl + 1}]/label").text

        # return afterl > l and optext == stage_name
        if afterl > l and optext == stage_name:
            print(afterl, optext)
            return True
        else:
            print(afterl, optext)
            return False

    def navigate_back_to_Opportunity_stages(self):
        self.driver.find_element(*self.BACK_TO_SETTINGS_BUTTON).click()
        time.sleep(2)
        self.click_opportunity_stages_link()

    def drag_and_drop_stage(self):

        sc = self.driver.find_element(By.XPATH, f"//table/tbody/tr[{afterl + 1}]/td[1]/div//*[local-name()='svg']")
        ta = self.driver.find_element(By.XPATH, f"//table/tbody/tr[{afterl}]/td[1]/div//*[local-name()='svg']")
        action = ActionChains(self.driver)
        (action
         .click_and_hold(sc)
         .move_to_element(ta)
         .release(ta)
         .perform())
        time.sleep(2)

    def validate_stage_position(self):
        val = self.driver.find_element(By.XPATH, f"//table/tbody/tr[{afterl}]/td[2]").text
        LLC = LeadLabelsConfiguratorPage(self.driver)
        LLC.navigate_to_opportunity_list()
        self.driver.find_element(By.XPATH, "//tbody/tr[1]/td[6]/div[1]/span[1]").click()

        opval = self.driver.find_element(By.XPATH, f"//app-select-dropdown/div/div/div/div[{afterl}]/label").text
        return stage_name in val and opval == stage_name

    def click_disable_button(self):
        indexx = afterl
        disable_button_locator = (self.DISABLE_BUTTON[0], self.DISABLE_BUTTON[1].format(indexx))
        disable_button = self.driver.find_element(*disable_button_locator)
        disable_button.click()
        time.sleep(2)

    def is_stage_disabled(self):
        stage_text_locator = (self.STAGE_TEXT[0], self.STAGE_TEXT[1].format(afterl + 1))
        stage_text = self.driver.find_element(*stage_text_locator).text

        if stage_text == stage_name:
            enable_button_locator = (self.DISABLE_BUTTON[0], self.DISABLE_BUTTON[1].format(afterl + 1))
            enable_button = self.driver.find_element(*enable_button_locator)
            enable_button.click()
            time.sleep(2)
            return True
        else:
            return False
