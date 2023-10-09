import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class ConvertOpportunityPage:
    def __init__(self,driver):
        self.driver=driver

    LEAD_ROW = (By.XPATH, "(//tbody//tr//td[2]//span[contains(@class,'cursor-pointer')])[1]")
    CONVERT_BUTTON = (By.XPATH, "(//button[normalize-space()='Convert'])[1]")
    CONVERT_TO_OPPORTUNITY = (By.XPATH, "(//p[@class='text-xs rounded-md py-1 mt-1 px-2 w-fit font-medium cursor-pointer ng-star-inserted'])[1]")
    BUDGET_INPUT = (By.XPATH, "(//input[@placeholder='Enter budget'])[1]")
    CONFIGURATION_TYPE_DROPDOWN = (By.XPATH, "//div[9]//div[1]//div[1]//button[1]")
    SELECT_CONFIGURATION = (By.XPATH, "//div[2]/app-select-dropdown/div/div/div/div[2]/label")
    SAVE_BUTTON = (By.XPATH, "(//button[normalize-space()='Save'])[1]")
    LEADS_LINK = (By.XPATH, "//a[normalize-space()='Leads']")





    def change_prefill_details(self):
        xx=self.driver.find_element(By.XPATH, "(//input[@id='voice-search'])[5]")
        self.driver.execute_script("arguments[0].click()", xx)
        ss = self.driver.find_element(By.XPATH, "(//label[normalize-space()='Referrals'])[1]")
        self.driver.execute_script("arguments[0].click()", ss)
        time.sleep(2)
        zz=self.driver.find_element(By.XPATH, "(//input[@id='voice-search'])[6]")
        self.driver.execute_script("arguments[0].click()", zz)
        self.driver.find_element(By.XPATH, "(//label[normalize-space()='Employee'])[1]").click()
        yy=self.driver.find_element(By.XPATH, "(//input[@id='selectLead'])[1]")
        self.driver.execute_script("arguments[0].click()", yy)

    def click_leads_link(self):
        self.driver.find_element(*self.LEADS_LINK).click()
        time.sleep(3)

    def click_lead(self):
        lead_element = self.driver.find_element(*self.LEAD_ROW)
        lead_element.click()
        time.sleep(3)

    def click_convert(self):
        convert_button = self.driver.find_element(*self.CONVERT_BUTTON)
        convert_button.click()
        convert_opportunity_button = self.driver.find_element(*self.CONVERT_TO_OPPORTUNITY)
        convert_opportunity_button.click()

    def enter_budget(self, budget_value):
        budget_input = self.driver.find_element(*self.BUDGET_INPUT)
        budget_input.send_keys(budget_value)
        time.sleep(2)

    def select_configuration_type(self):
        config_dropdown = self.driver.find_element(*self.CONFIGURATION_TYPE_DROPDOWN)
        self.driver.execute_script("arguments[0].click()",config_dropdown)
        # config_dropdown.click()
        time.sleep(2)
        select_config = self.driver.find_element(*self.SELECT_CONFIGURATION)
        self.driver.execute_script("arguments[0].click()", select_config)
        # select_config.click()
        time.sleep(2)
        self.driver.execute_script("arguments[0].click()", config_dropdown)
        # config_dropdown.click()

    def click_save(self):
        save_button = self.driver.find_element(*self.SAVE_BUTTON)
        save_button.click()
        time.sleep(3)

    def is_lead_converted_to_opportunity(self):
        VL = []
        self.driver.find_element(By.XPATH, "(//span[normalize-space()='Lead'])[1]").click()
        time.sleep(3)
        # validating in opurtunity
        self.driver.find_element(By.XPATH, "(//a[normalize-space()='Opportunities'])[1]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,
                                    "(//tbody//tr//td[2]//span[contains(@class,'cursor-pointer')])[1]").click()
        time.sleep(3)

        acti = self.driver.find_elements(By.XPATH, "//div[@class='ng-star-inserted']//p")
        for i in acti:
            if "added opportunity to" in i.text:
                VL.append(True)
                break
        else:
            VL.append(False)

        # print(driver.find_element(By.XPATH,"//div[@class='block']").text)
        # if "Not Contacted" in self.driver.find_element(By.XPATH, "//div[@class='block']").text:
        #     VL.append(True)
        # else:
        #     VL.append(False)

        if False not in VL:
            return True
        else:
            return False



    def fill_all_the_fields(self):
        self.driver.find_element(By.XPATH, "(//input[@id='name '])[1]").clear()
        self.driver.find_element(By.XPATH, "(//input[@id='name '])[1]").send_keys("new one")
        time.sleep(3)

        j = self.driver.find_element(By.XPATH,
                                        "/html/body/app-root/app-layout/div/div/main/div/app-opportunity-onboard/div[2]/div/form/div[1]/div[2]/div/div/div[6]/div/button")
        self.driver.execute_script("arguments[0].click()", j)
        self.driver.find_element(By.XPATH, "//label[normalize-space()='New']").click()
        self.driver.execute_script("arguments[0].click()", j)
        time.sleep(3)

        x = self.driver.find_element(By.XPATH,
                                        "/html/body/app-root/app-layout/div/div/main/div/app-opportunity-onboard/div[2]/div/form/div[1]/div[2]/div/div/div[7]/div/button[1]")
        self.driver.execute_script("arguments[0].click()", x)
        self.driver.find_element(By.XPATH, "//label[normalize-space()='Budget Issue']").click()
        time.sleep(3)

        y = self.driver.find_element(By.XPATH, "//div[10]//div[1]//div[1]//button[1]")
        self.driver.execute_script("arguments[0].click()", y)
        self.driver.find_element(By.XPATH, "(//label[normalize-space()='South'])[1]").click()
        self.driver.execute_script("arguments[0].click()", y)
        time.sleep(3)

        # floor
        yy = self.driver.find_element(By.XPATH, "//div[11]//div[1]//div[1]//button[1]")
        self.driver.execute_script("arguments[0].click()", yy)
        self.driver.find_element(By.XPATH, "//label[normalize-space()='2']").click()
        self.driver.execute_script("arguments[0].click()", yy)
        time.sleep(3)

        # driver.find_element(By.XPATH,"(//input[@id='preferredLocationInput'])[1]").send_keys("hydera")
        actions = ActionChains(self.driver)
        actions.move_to_element(
            self.driver.find_element(By.XPATH, "//span[normalize-space()='Preferred Handover Time']")).perform()
        zz = self.driver.find_element(By.XPATH, "//span[contains(text(),'Select month')]")

        self.driver.execute_script("arguments[0].click()", zz)
        self.driver.find_element(By.XPATH, "(//label[normalize-space()='2'])[1]").click()
        time.sleep(3)

        self.driver.find_element(By.XPATH, "//label[normalize-space()='Loan']").click()
        self.driver.find_element(By.XPATH, "(//label[normalize-space()='Investment'])[1]").click()
        self.driver.find_element(By.XPATH, "(//textarea[@placeholder='Enter remarks'])[1]").send_keys("hello")




