import time

from selenium.webdriver.common.by import By


class OpportunitiesPage:
    def __init__(self,driver):
        self.driver=driver

    ASSIGN_OPPORTUNITY_BUTTON = (By.XPATH, "(//span[normalize-space()='Assign Opportunity Owner'])[1]")
    OPPORTUNITY_OWNER_DROPDOWN = (By.XPATH, "(//button[@class='absolute inset-y-0 right-0 flex items-center pr-3'])[1]")
    expected=[]

    def click_assign_opportunity_owner_button(self):
        assign_lead_owner_button = self.driver.find_element(*self.ASSIGN_OPPORTUNITY_BUTTON)
        assign_lead_owner_button.click()

    def select_opportunity_owner(self):
        lead_owner_dropdown = self.driver.find_element(*self.OPPORTUNITY_OWNER_DROPDOWN)
        lead_owner_dropdown.click()
        self.expected.append(self.driver.find_element(By.XPATH, "(//div[2]/app-select-dropdown/div/div/div/div/label)[9]").text)
        lead_owner_option= self.driver.find_element(By.XPATH,"(//div[2]/app-select-dropdown/div/div/div/div/label)[9]")
        lead_owner_option.click()
        self.driver.find_element(By.XPATH, "(//button[normalize-space()='Save'])[1]").click()

        time.sleep(5)

    def isAssignedOpportunityOwner_Changed(self):
        val=[]
        for j in range(4):
            s = f"//tbody/tr[{j + 1}]/td[9]/div[1]/span[1]"
            actual = self.driver.find_element(By.XPATH, s).text
            if actual.lower() == self.expected[0].lower():
                val.append(True)
        if False not in val:
            return True
        else:
            return False