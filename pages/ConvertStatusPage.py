import time

import configparser
from selenium.webdriver.common.by import By
from dataproviders import data
from pages.ChangeLabelsFromLeadsListPage import ChangeLabelsFromLeadsListPage


class ConvertStatusPage:
    def __init__(self,driver):
        self.driver=driver

    config = configparser.ConfigParser()
    config.read(r'config.txt')

    ACTIVITY_TAB = (By.XPATH, "(//a[normalize-space()='Activity'])[1]")
    CONVERT_BUTTON = (By.XPATH, "//button[normalize-space()='Convert']")
    LOST_LINK = (By.XPATH,"(//p[@class='text-xs rounded-md font-medium py-1 px-2 w-fit mt-1 ml-2 cursor-pointer ng-star-inserted'])[1]")
    LOST_REASON_DROPDOWN = (By.XPATH, "(//button[@class='cursor-pointer w-full border-[1px] flex justify-start items-center relative'])[1]")
    LOST_REASON_OPTION_1 = (By.XPATH, "(//div[@class='flex items-center cursor-pointer p-2 ng-star-inserted']//input)[1]")
    LOST_REASON_OPTION_2 = (By.XPATH, "(//div[@class='flex items-center cursor-pointer p-2 ng-star-inserted']//input)[2]")
    LOST_REASON_TEXTAREA = (By.XPATH, "//div[@class='angular-editor-textarea']")
    SAVE_BUTTON = (By.XPATH, "//button[normalize-space()='Save']")

    CHANGE_ASSIGNEE_BUTTON = (By.XPATH, "(//button[contains(@class,' pr-3')])[1]")
    ASSIGNEE_OPTION = (By.XPATH, "(//div[@class='flex items-center cursor-pointer p-2 ng-star-inserted'])[5]")
    EXPECTED_STATUS_TEXT = "status changed from"

    name = data.c[1]+" "+data.c[0]
    # name = config.get('edit_profile_name', 'changed_name')

    LEAD_BUTTON = (By.XPATH, "(//span[normalize-space()='Lead'])[1]")
    LOST_TAB = (By.XPATH, "(//h6[normalize-space()='Lost'])[1]")
    EXPECTED_ASSIGNED_TEXT = "assigned"
    EXPECTED_STATUS = "Active"

    OPEN_TAB = (By.XPATH, "(//h6[normalize-space()='Open'])[1]")
    LEAD_NAME_LINKS = (By.XPATH, "(//tbody//tr//td[2]//span[contains(@class,'cursor-pointer')])")

    def click_convert_button(self):
        time.sleep(2)
        activity_tab = self.driver.find_element(*self.ACTIVITY_TAB)
        self.driver.execute_script("arguments[0].click()", activity_tab)
        convert_button = self.driver.find_element(*self.CONVERT_BUTTON)
        convert_button.click()

    def click_lost_link(self):
        lost_link = self.driver.find_element(*self.LOST_LINK)
        lost_link.click()
        time.sleep(2)

    def enter_lost_reason_text(self, reason):
        dropdown = self.driver.find_element(*self.LOST_REASON_DROPDOWN)
        self.driver.execute_script("arguments[0].click()", dropdown)
        option_1 = self.driver.find_element(*self.LOST_REASON_OPTION_1)
        option_2 = self.driver.find_element(*self.LOST_REASON_OPTION_2)
        option_1.click()
        option_2.click()
        self.driver.execute_script("arguments[0].click()", dropdown)
        textarea = self.driver.find_element(*self.LOST_REASON_TEXTAREA)
        textarea.send_keys(reason)
        time.sleep(3)

    def click_savee_button(self):
        save_button = self.driver.find_element(*self.SAVE_BUTTON)
        save_button.click()
        time.sleep(5)

    def click_change_assignee(self):
        time.sleep(3)
        change_assignee_button = self.driver.find_element(*self.CHANGE_ASSIGNEE_BUTTON)
        self.driver.execute_script("arguments[0].click()", change_assignee_button)
        time.sleep(2)
        assignee_option = self.driver.find_element(*self.ASSIGNEE_OPTION)
        assignee_option.click()
        time.sleep(3)

    def isStatus_converted_To_Lost(self):
        l = []

        # global name

        status_element = self.driver.find_element(By.XPATH, "//div[@class='ng-star-inserted']//p")
        if self.EXPECTED_STATUS_TEXT in status_element.text:
            l.append(True)

        lead_link = self.driver.find_element(*self.LEAD_BUTTON)
        lead_link.click()
        time.sleep(5)
        lost_tab = self.driver.find_element(*self.LOST_TAB)
        lost_tab.click()
        time.sleep(3)

        leads = self.driver.find_elements(By.XPATH, "//tbody//tr//td[2]//span[contains(@class,'cursor-pointer')]")
        for lead in leads:
            if self.name in lead.text:
                l.append(True)
                lead.click()
                break
        if False not in l:
            return True
        else:
            return False



    def isConverted_from_lost_to_Active(self):
        lisst = []
        # expectT = "assigned"
        assigned_element = self.driver.find_element(By.XPATH, "//div[@class='ng-star-inserted']//p")
        if self.EXPECTED_ASSIGNED_TEXT in assigned_element.text:
            lisst.append(True)
        # ac = "Active"
        status_element = self.driver.find_element(By.XPATH,"(//span[@class='inline-flex items-center rounded-full px-2.5 py-0.5 text-xs font-medium ng-star-inserted'])[1]")
        if self.EXPECTED_STATUS == status_element.text:
            lisst.append(True)

        lead_link = self.driver.find_element(*self.LEAD_BUTTON)
        lead_link.click()
        time.sleep(5)
        if False not in lisst:
            return True
        else:
            return False

    def isActive_check_in_OpenFIlter(self):
        li = []
        open_tab = self.driver.find_element(*self.OPEN_TAB)
        open_tab.click()
        time.sleep(2)
        leads = self.driver.find_elements(*self.LEAD_NAME_LINKS)

        for lead in leads:
            if self.name in lead.text:
                time.sleep(2)
                lead.click()
                li.append(True)  # converting to active also completed
                break
        if False not in li:
            Label = ChangeLabelsFromLeadsListPage(self.driver)
            Label.click_lead_menu()
            return True
        else:
            Label = ChangeLabelsFromLeadsListPage(self.driver)
            Label.click_lead_menu()
            return False