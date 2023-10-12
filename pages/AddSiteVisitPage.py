import time

from selenium.webdriver.common.by import By


class AddSiteVisitPage:
    def __init__(self,driver):
        self.driver=driver

    siteVisits_XPATH="(//a[@id='Sitevisit'])[1]"
    createSiteVisit_XPATH="(//button[normalize-space()='Site Visit'])[1]"
    saveButton_XPATH="(//button[normalize-space()='Save'])[1]"
    listt=[]
    def clickOnSiteVisits_bar(self):
        self.driver.find_element(By.XPATH, self.siteVisits_XPATH).click()
        time.sleep(3)
    def createSite_Visit(self):
        self.driver.find_element(By.XPATH, self.createSiteVisit_XPATH).click()
        time.sleep(2)

    def fill_siteVisit_details(self,date,timee):
        self.driver.find_element(By.XPATH, "(//div[contains(@class,'pointer-events-none')]//button)[1]").click()
        self.driver.find_element(By.XPATH, "(//div[2]/app-select-dropdown/div/div/div/div/label)[6]").click()
        #(//label[normalize-space()='Nitish Rana'])[1]
        self.driver.find_element(By.ID, "date").send_keys(date)
        time.sleep(1)
        self.driver.find_element(By.ID, "time").send_keys(timee)

    def fill_siteVisit_details_opportunity(self,date,timee):
        self.driver.find_element(By.XPATH, "(//div[contains(@class,'pointer-events-none')]//button)[1]").click()
        self.driver.find_element(By.XPATH, "(//div[2]/app-select-dropdown/div/div/div/div/label)[6]").click()
        self.driver.find_element(By.ID, "date").send_keys(date)
        time.sleep(1)
        self.driver.find_element(By.ID, "time").send_keys(timee)

    def click_On_Save(self):
        self.driver.find_element(By.XPATH, self.saveButton_XPATH).click()
        time.sleep(3)

    def is_siteVisitAdded(self):

        l = self.driver.find_elements(By.XPATH,"//div[@class='py-4 ml-4 bg-white mb-4 rounded-lg space-y-2 ng-star-inserted']")
        if len(l) >= 1:
            self.listt.append(True)
        else:
            self.listt.append(False)

        #validating in activities page wheather the site visit adding activity is displayed or not
        activites=self.driver.find_element(By.XPATH,"//a[@id='activities']")
        self.driver.execute_script("arguments[0].click()",activites)
        time.sleep(3)
        expectedd="Site Visit"
        actuall=self.driver.find_element(By.XPATH,"//div[@class ='py-4 ml-6 ng-star-inserted']//p").text
        if expectedd in actuall:
            self.listt.append(True)
        else:
            self.listt.append(False)
        self.driver.find_element(By.XPATH, self.siteVisits_XPATH).click()
        time.sleep(2)
        if False not in self.listt:
            return True
        else:
            return False


