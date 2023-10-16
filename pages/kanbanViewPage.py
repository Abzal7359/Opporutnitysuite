import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class KanbanViewPage:
    def __init__(self,driver):
        self.driver=driver

    DASHBOARD_DROPDOWN = (By.XPATH,"(//*[name()='svg'][@class='w-4 h-4 text-slate-400 cursor-pointer hover:text-black ng-star-inserted'])[1]")
    OPPORTUNITY_DETAILS = (By.XPATH,"(//div[@class='flex flex-col bg-white-200 px-4'])//div[@class='mb-2 space-y-2']//div[@class='flex space-x-4 items-center ng-star-inserted']")

    OPPORTUNITY_LINK = (By.XPATH, "(//span[normalize-space()='Opportunity'])[1]")
    DROPDOWN_BUTTON = (By.XPATH,"(//*[name()='svg'][@class='w-4 h-4 text-slate-400 cursor-pointer hover:text-black ng-star-inserted'])[1]")
    TASK_COUNT = (By.XPATH, "(//div[@class='text-[12px] text-[#6B7280]'][contains(normalize-space(),'')])[3]")
    NOTES_COUNT = (By.XPATH, "(//div[@class='text-[12px] text-[#6B7280]'][contains(normalize-space(),'')])[4]")

    add_label_button_xpath = "(//span[normalize-space()='Add Label'])[1]"
    assign_opportunity_owner_xpath = "(//span[normalize-space()='Assign Opportunity Owner'])[1]"
    dropdown_button_xpath = "(//button[@class='absolute inset-y-0 right-0 flex items-center pr-3'])[1]"
    selected_item_xpath = "(//app-select-dropdown/div/div/div/div/label)"
    save_button_xpath = "(//button[normalize-space()='Save'])[1]"
    val=[]
    l=[]

    def select_assigne_person(self):
        # Click on the dropdown button
        self.driver.find_element(By.XPATH, self.dropdown_button_xpath).click()

        # Get the text of the selected person
        self.val.append(self.driver.find_element(By.XPATH, self.selected_item_xpath).text)

        # Select the person from the dropdown
        self.driver.find_element(By.XPATH, self.selected_item_xpath).click()

        # Wait for a moment (if needed)
        time.sleep(2)

        # Click the "Save" button
        save_button = self.driver.find_element(By.XPATH, self.save_button_xpath)
        self.driver.execute_script("arguments[0].click()", save_button)

        # Wait for a moment (if needed)
        time.sleep(3)


    def click_assign_opportunity_owner(self):
        assign_button = self.driver.find_element(By.XPATH, self.assign_opportunity_owner_xpath)
        assign_button.click()


    def check_opportunity_details_displayed(self):
        self.driver.find_element(*self.DASHBOARD_DROPDOWN).click()
        elements = self.driver.find_elements(*self.OPPORTUNITY_DETAILS)
        return len(elements) >= 3

    def get_count(self):
        taskCount = self.driver.find_element(By.XPATH,"(//div[@class='text-[12px] text-[#6B7280]'][contains(normalize-space(),'')])[3]").text
        notesCount = self.driver.find_element(By.XPATH,"(//div[@class='text-[12px] text-[#6B7280]'][contains(normalize-space(),'')])[4]").text
        self.l.append(int(taskCount))
        self.l.append(int(notesCount))

    def isTask_Notes_areCreated(self):
        # self.driver.find_element(*self.OPPORTUNITY_LINK).click()
        # time.sleep(3)
        self.driver.find_element(*self.DROPDOWN_BUTTON).click()
        time.sleep(2)
        taskCountt=int(self.driver.find_element(*self.TASK_COUNT).text)
        notesCountt=int(self.driver.find_element(*self.NOTES_COUNT).text)
        if taskCountt > self.l[0] and notesCountt > self.l[1]:
            self.driver.find_element(*self.DROPDOWN_BUTTON).click()
            return True
        else:
            self.driver.find_element(*self.DROPDOWN_BUTTON).click()
            return False


    def select_multiple_opp(self):
        for i in range(1, 5):
            z = f"(//input[@id='selectedKanbanOpportunity'])[{i}]"
            self.driver.find_element(By.XPATH, z).click()

    def click_add_label_for_bulk(self):
        self.driver.find_element(By.XPATH, self.add_label_button_xpath).click()

    def select_label(self):
        self.driver.find_element(By.XPATH,"(//button[@class='cursor-pointer bg-white w-full border-[1px] h-fit'])[1]").click()
        self.driver.find_element(By.XPATH, "//input[contains(@id,'selectedItem-')]").click()
        z = self.driver.find_element(By.XPATH, "(//button[normalize-space()='Save'])[1]")
        self.driver.execute_script("arguments[0].click()", z)
        time.sleep(5)

    def validate_label_count_and_dropdown_labels(self):

        z = True
        for i in range(1, 5):
            x = f"(//div[@class='p-[.1rem_0.4rem] text-gray-500 text-xs ng-star-inserted'][contains(normalize-space(),'+')])[{i}]"
            d=self.driver.find_element(By.XPATH, x).text
            c = f"(//*[name()='svg'][@class='w-4 h-4 text-slate-400 cursor-pointer hover:text-black ng-star-inserted'])[{i}]"
            self.driver.find_element(By.XPATH, c).click()
            xx = self.driver.find_elements(By.XPATH, "//div[@class='m-[.3rem_.2rem_0_0] ng-star-inserted']")
            if len(xx) == int(d)+1:
                pass
            else:
                z = False
                break
            time.sleep(2)
            self.driver.find_element(By.XPATH, c).click()
        if z:
            return True
        else:
            return False





    def Is_assigne_person_updated(self):
        ss = True
        for i in range(1, 5):

            # wait = WebDriverWait(self.driver, 10)
            # element = wait.until(EC.element_to_be_clickable((By.XPATH, f"(//div[@class='ml-4 items-center']//p[1])[{i}]")))
            #
            # element.click()

            ss = f"(//div[@class='ml-4 items-center']//p[1])[{i}]"
            self.driver.find_element(By.XPATH, ss).click()
            time.sleep(3)
            z = self.driver.find_element(By.XPATH, "(//input[@id='voice-search'])[1]").get_attribute("placeholder")
            if z == self.val[0]:
                pass
            else:
                ss = False
                break

            self.driver.find_element(By.XPATH, "(//span[normalize-space()='Opportunity'])[1]").click()
            time.sleep(5)
        return ss

    lll = []
    def get_text(self):
        actuall = self.driver.find_element(By.XPATH, "//app-kanban/div/div/div[1]/div[3]/div[1]/div/div/div[2]/p[1]").text
        self.lll.append(actuall)

    def drag_and_drop_oneStage(self):
        action = ActionChains(self.driver)
        source = self.driver.find_element(By.XPATH, "//app-kanban/div/div/div[1]/div[3]/div[1]/div")
        target = self.driver.find_element(By.XPATH, "//app-kanban/div/div/div[2]/div[3]/div[1]/div")
        time.sleep(2)
        action.click_and_hold(source).move_to_element(target).release(target)
        action.perform()
        time.sleep(3)

    def valiadte_is_dropped(self):
        ll = []
        exp = self.driver.find_element(By.XPATH, "//app-kanban/div/div/div[2]/div[3]/div[1]/div/div/div[2]/p[1]").text
        if self.lll[0] == exp:
            ll.append(True)

        z = self.driver.find_element(By.XPATH, "//app-kanban/div/div/div[1]/div[1]/span").text
        x = self.driver.find_element(By.XPATH, "//app-kanban/div/div/div[2]/div[1]/span").text
        p = f"Opportunity stage changed from{z}to{x}"

        self.driver.find_element(By.XPATH, "//app-kanban/div/div/div[2]/div[3]/div[1]/div/div/div[2]/p[1]").click()

        time.sleep(3)
        xx = self.driver.find_element(By.XPATH,
                                         "(//div[contains(@class,'flex flex-row justify-between px-2')]//p[@class='font-medium text-sm ng-star-inserted'])").text
        if p in xx:
            ll.append(True)

        else:
            ll.append(False)

        if False not in ll:
            return True
        else:
            return False

    def click_back_kanban(self):
        self.driver.find_element(By.XPATH, "(//span[normalize-space()='Opportunity'])[1]").click()
        time.sleep(3)
        self.driver.refresh()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//app-opportunities-list/div/div[1]/div[2]/button[2]//*[local-name()='svg']").click()
        time.sleep(5)

    twol=[]
    def drag_into_won(self):
        action = ActionChains(self.driver)
        self.driver.execute_script("arguments[0].scrollIntoView(true)",self.driver.find_element(By.XPATH,"//app-kanban/div/div/div[9]/div[1]/span"))
        actu = self.driver.find_element(By.XPATH, "//app-kanban/div/div/div[7]/div[3]/div[1]/div/div/div[2]/p[1]").text
        self.twol.append(actu)
        sc = self.driver.find_element(By.XPATH, "//app-kanban/div/div/div[7]/div[3]/div[1]/div")
        ta = self.driver.find_element(By.XPATH, "//app-kanban/div/div/div[9]/div[3]/div[1]/div")
        time.sleep(2)
        (action
         .click_and_hold(sc)

         .move_to_element(ta)
         .release(ta))
        action.perform()
        time.sleep(3)

    def is_dropped_or_not(self):
        ss = []
        exp = self.driver.find_element(By.XPATH,
                                          "//app-kanban/div/div/div[9]/div[3]/div[1]/div/div/div[2]/p[1]").text
        if self.twol[0] == exp:
            ss.append(True)

        # xxx = context.driver.find_element(By.XPATH, " //*[contains(@id,'cdk-drop-list-')]/div[5]/div[1]/span").text
        yy = self.driver.find_element(By.XPATH, "//app-kanban/div/div/div[9]/div[1]/span").text
        pp = "Opportunity stage changed"

        kuku = self.driver.find_element(By.XPATH, "//app-kanban/div/div/div[9]/div[3]/div[1]/div/div/div[2]/p[1]")
        self.driver.execute_script("arguments[0].click()", kuku)
        time.sleep(3)
        won = self.driver.find_element(By.XPATH,
                                          "(//div[contains(@class,'flex flex-row justify-between px-2')]//p[@class='font-medium text-sm ng-star-inserted'])").text
        if pp and yy in won:
            ss.append(True)

        else:
            ss.append(False)

        if False not in ss:
            return True
        else:
            return False



