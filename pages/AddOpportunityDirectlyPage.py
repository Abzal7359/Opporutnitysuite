import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class AddOpportunityDirectlyPage:
    def __init__(self,driver):
        self.driver=driver

    OPPORTUNITIES_LINK = (By.XPATH, "(//a[normalize-space()='Opportunities'])[1]")
    ADD_OPPORTUNITY_BUTTON = (By.XPATH, "(//button[normalize-space()='Add Opportunity'])[1]")
    SAVE_BUTTON=(By.XPATH,"(//button[normalize-space()='Save'])[1]")

    def click_to_save(self):
        self.driver.find_element(*self.SAVE_BUTTON).click()


    def enter_opportunity_details(self,mobile,firstname,lname,email):
        # code to bufget and configuration
        self.driver.find_element(By.XPATH, "(//input[@placeholder='Enter budget'])[1]").send_keys("4000000")
        self.driver.find_element(By.XPATH, "//div[12]//div[1]//div[1]//button[2]").click()
        self.driver.find_element(By.XPATH, "(//input[@id='selectedItem-0'])[1]").click()
        time.sleep(2)

        # code to fill details
        self.driver.find_element(By.XPATH, "(//input[@id='name '])[1]").clear()
        self.driver.find_element(By.XPATH, "(//input[@id='name '])[1]").send_keys("new one")
        time.sleep(3)

        # entering mobile number
        self.driver.find_element(By.XPATH, "//input[@id='phone-number']").send_keys(mobile)
        self.driver.find_element(By.XPATH,"//input[@placeholder='Enter first name' and @formcontrolname='name']").send_keys(firstname)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Enter last name' ]").send_keys(lname)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Enter email' ]").send_keys(email)

        self.driver.find_element(By.XPATH, "(//input[@id='voice-search'])[1]").click()
        self.driver.find_element(By.XPATH, "(//label[normalize-space()='Channel partner'])[1]").click()
        time.sleep(3)

        xx = self.driver.find_element(By.XPATH, "(//input[@id='voice-search'])[2]")
        self.driver.execute_script("arguments[0].click()", xx)
        self.driver.find_element(By.XPATH, "(//div[2]/app-select-dropdown/div/div/div/div/label)[7]").click()

        # self.driver.find_element(By.XPATH, "//span[text()='Use assignment rule for auto assigning']").click()
        j = self.driver.find_element(By.XPATH, "/html/body/app-root/app-layout/div/div/main/div/app-opportunity-onboard/div[2]/div/form/div[1]/div[2]/div/div/div[9]/div/button")
        self.driver.execute_script("arguments[0].click()", j)
        self.driver.find_element(By.XPATH, "//label[normalize-space()='New']").click()
        self.driver.execute_script("arguments[0].click()", j)
        time.sleep(3)

        x = self.driver.find_element(By.XPATH,"/html/body/app-root/app-layout/div/div/main/div/app-opportunity-onboard/div[2]/div/form/div[1]/div[2]/div/div/div[10]/div/button[2]")
        self.driver.execute_script("arguments[0].click()", x)
        self.driver.find_element(By.XPATH, "(//div[2]/app-select-dropdown/div/div/div/div/label)[3]").click()
        time.sleep(3)

        y = self.driver.find_element(By.XPATH,"/html/body/app-root/app-layout/div/div/main/div/app-opportunity-onboard/div[2]/div/form/div[1]/div[2]/div/div/div[13]/div/div/button[2]")
        self.driver.execute_script("arguments[0].click()", y)
        self.driver.find_element(By.XPATH, "(//label[normalize-space()='South'])[1]").click()
        self.driver.execute_script("arguments[0].click()", y)
        time.sleep(3)

        # floor
        yy = self.driver.find_element(By.XPATH,"/html/body/app-root/app-layout/div/div/main/div/app-opportunity-onboard/div[2]/div/form/div[1]/div[2]/div/div/div[14]/div/div/button[2]")
        self.driver.execute_script("arguments[0].click()", yy)
        self.driver.find_element(By.XPATH, "//label[normalize-space()='2']").click()
        self.driver.execute_script("arguments[0].click()", yy)
        time.sleep(3)

        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, "//span[normalize-space()='Preferred Handover Time']")).perform()
        zz = self.driver.find_element(By.XPATH, "//span[contains(text(),'Select month')]")

        self.driver.execute_script("arguments[0].click()", zz)
        self.driver.find_element(By.XPATH, "(//label[normalize-space()='2'])[1]").click()
        time.sleep(3)

        self.driver.find_element(By.XPATH, "//label[normalize-space()='Loan']").click()
        self.driver.find_element(By.XPATH, "(//label[normalize-space()='Investment'])[1]").click()
        self.driver.find_element(By.XPATH, "(//textarea[@placeholder='Enter remarks'])[1]").send_keys("hello")

    def click_opportunities_link(self):
        opportunities_link = self.driver.find_element(*self.OPPORTUNITIES_LINK)
        opportunities_link.click()
        time.sleep(3)

    def click_opportunities_linkk(self):
        #after report generation  we clicking opportunity
        act = ActionChains(self.driver)
        (act
         .move_to_element(self.driver.find_element(By.XPATH, "//span[contains(text(),'Sales')]"))
         .move_to_element(self.driver.find_element(By.XPATH, "(//a[normalize-space()='Opportunities'])[1]"))
         .click()
         .perform())
        time.sleep(3)


    def click_add_opportunity_button(self):
        add_opportunity_button =self.driver.find_element(*self.ADD_OPPORTUNITY_BUTTON)
        add_opportunity_button.click()
        time.sleep(2)
    def is_opportunity_added(self):
        L = []
        acti = self.driver.find_elements(By.XPATH, "//div[@class='ng-star-inserted']//p")
        for i in acti:
            s = False
            if "added opportunity to" in i.text:
                s = True
            if s:
                L.append(s)
                break
        # print(driver.find_element(By.XPATH,"//div[@class='block']").text)
        # if "Not Contacted" in self.driver.find_element(By.XPATH, "//div[@class='block']").text:
        #     L.append(True)
        # else:
        #     L.append(False)
        if False not in L:
            return True
        else:
            return False

