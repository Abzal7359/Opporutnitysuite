import time

from selenium.webdriver.common.by import By


class ChangeLeadOwnerFromLeadsListPage:
    def __init__(self,driver):
        self.driver=driver

    LEAD_OWNER_COLUMN = (By.XPATH, "//tbody/tr[1]/td[8]/div[1]/span[1]")
    LEAD_OWNER_LABELS = (By.XPATH, "//label[contains(normalize-space(),'')]")


    def changeLeadOwner_and_Validate(self):
        Expecttext = self.driver.find_element(By.XPATH, "(//span[@class='mr-4 relative ng-star-inserted'])[1]").text
        actuall = ""
        lead_owner_column = self.driver.find_element(*self.LEAD_OWNER_COLUMN)
        lead_owner_column.click()
        time.sleep(2)
        labels = self.driver.find_elements(*self.LEAD_OWNER_LABELS)
        for i in range(1, len(labels)):
            if labels[i].text.lower() != Expecttext.lower():
                actuall = labels[i].text
                labels[i].click()
                break
            else:
                pass
        time.sleep(3)
        self.driver.find_element(By.XPATH,"(//tbody//tr//td[2]//span[contains(@class,'cursor-pointer')])[1]").click()
        time.sleep(3)
        expect = f"Lead assigned from {Expecttext} to {actuall}"
        t = self.driver.find_element(By.XPATH, "//div[@class='ng-star-inserted']//p").text
        if expect.lower() in t.lower():
            return True
        else:
            return False