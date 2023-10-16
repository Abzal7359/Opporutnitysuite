import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TasksPage:
    def __init__(self,driver):
        self.driver=driver

    createTask_XPATH="//button[normalize-space()='Create Task']"
    textArea_XPATH="//div[@class='angular-editor-textarea']"
    priority_XPATH="(//div[contains(@class,'sm:px-6')]//div[contains(@class,'relative')])//input[@placeholder='Medium']"
    time_XPATH="//input[@id='dueTime']"
    taskSave_XPATH="//button[normalize-space()='Save']"

    #------------------------------------------------------
    # editing task
    CLONE_TASK_BUTTON = "//div[@class='flex flex-col']//div[1]//div[1]//div[2]//*[name()='svg']"
    PRIORITY_INPUT = "(//div[contains(@class,'sm:px-6')]//div[contains(@class,'relative')])//input[@placeholder='High']"
    VIEW_DETAILS_BUTTON = (By.XPATH, "(//a[contains(text(),'View Details')])[1]")
    COMMENT_INPUT = (By.XPATH, "(//input[@placeholder='Write comment here'])[1]")
    POST_BUTTON = (By.XPATH, "//button[normalize-space()='Post']")

    List_tasks=[]

    def add_comment(self):

        self.driver.find_element(*self.VIEW_DETAILS_BUTTON).click()
        time.sleep(3)
        self.driver.find_element(*self.COMMENT_INPUT).send_keys("hello")
        self.driver.find_element(*self.POST_BUTTON).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//body").click()

        time.sleep(2)


    def click_to_clone_task(self):
        self.driver.find_element(By.XPATH,self.CLONE_TASK_BUTTON).click()
        self.driver.find_element(By.XPATH, "(//p[@class='text-sm'])[1]").click()
        time.sleep(2)
        c = self.driver.find_element(By.XPATH,self.PRIORITY_INPUT)
        self.driver.execute_script("arguments[0].click()", c)
        self.driver.find_element(By.XPATH, "(//label[normalize-space()='Very High'])[1]").click()
        self.driver.find_element(By.XPATH, "(//button[normalize-space()='Save'])[1]").click()
        time.sleep(3)











    def clickOnCreateTask(self):
        self.driver.find_element(By.XPATH,self.createTask_XPATH).click()
        time.sleep(2)

    def enterTaskDetails(self,message,timee):
        self.driver.find_element(By.XPATH, self.textArea_XPATH).send_keys(message)
        time.sleep(2)
        priority = self.driver.find_element(By.XPATH, self.priority_XPATH)
        self.driver.execute_script("arguments[0].click()", priority)
        time.sleep(2)

        p = self.driver.find_element(By.XPATH, "//label[normalize-space()='High']")
        self.driver.execute_script("arguments[0].click()", p)

        time.sleep(1)
        self.driver.find_element(By.XPATH, self.time_XPATH).send_keys(timee)
        time.sleep(2)
        # adding documnet
        # # self.driver.find_element(By.XPATH,"(//*[name()='svg'][@class='w-4 h-4'])[12]").click()
        # self.driver.find_element(By.XPATH, "//*[@id='file-upload - ']").send_keys(
        #     "C://Users/abzalhussain/Desktop/builldingone.jpg")
        # # time.sleep(6)
        # # self.driver.find_element(By.XPATH,"//button[contains(text(),'Close')]").click()
        # wt = WebDriverWait(self.driver, 10)
        # element = wt.until(
        #     EC.element_to_be_clickable((By.XPATH, "//div/div[1]/div[1]/div/div/span//*[local-name()='svg']")))
        # element.click()
        # # self.driver.find_element(By.XPATH, "//div/div[1]/div[1]/div/div/span//*[local-name()='svg']")
        # # self.driver.find_element(By.XPATH, "(//*[name()='svg'][@class='w-4 h-4'])[12]").click()
        # self.driver.find_element(By.XPATH, "//*[@id='file-upload - ']").send_keys(
        #     "C://Users/abzalhussain/Desktop/building.jpg")
        # self.driver.find_element(By.XPATH, self.taskSave_XPATH).click()

    def enterTaskDetailss(self, message, timee):
        self.driver.find_element(By.XPATH, self.textArea_XPATH).send_keys(message)
        time.sleep(2)
        priority = self.driver.find_element(By.XPATH, self.priority_XPATH)
        self.driver.execute_script("arguments[0].click()", priority)
        time.sleep(2)

        p = self.driver.find_element(By.XPATH, "//label[normalize-space()='High']")
        self.driver.execute_script("arguments[0].click()", p)

        time.sleep(1)
        self.driver.find_element(By.XPATH, "//form/div[1]/div[2]/div/div/div[2]/div[1]/div[1]/button").click()
        self.driver.find_element(By.XPATH, "(//app-select-dropdown/div/div/div/div)").click()
        self.driver.find_element(By.XPATH, self.time_XPATH).send_keys(timee)
        time.sleep(2)
        # adding documnet
        self.driver.find_element(By.XPATH, "//*[@id='file-upload - ']").send_keys(
            "C://Users/abzalhussain/Desktop/builldingone.jpg")
        wt = WebDriverWait(self.driver, 10)
        element = wt.until(
            EC.element_to_be_clickable((By.XPATH, "//div/div[1]/div[1]/div/div/span//*[local-name()='svg']")))
        element.click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//*[@id='file-upload - ']").send_keys(
            "C://Users/abzalhussain/Desktop/building.jpg")

    def clickOnTaskSave(self):
        self.driver.find_element(By.XPATH,self.taskSave_XPATH).click()
        time.sleep(3)

    def isTaskCreated(self):
        l = self.driver.find_elements(By.XPATH, "//div[@class='py-4 ml-4 bg-white mb-4 rounded-lg ng-star-inserted']")
        # boolean = False
        #below line for doc validationn
        # kix = self.driver.find_element(By.XPATH, "//app-task/div/div[3]/div/div[1]/div[4]/div").is_displayed()
        if len(l) >= 1 :            #and kix this keep in if for doc val
            self.List_tasks.append(True)
        else:
            self.List_tasks.append(False)
        # task created or not validating in activity page
        c = self.driver.find_element(By.XPATH, "//a[@id='activities']")
        self.driver.execute_script("arguments[0].click()", c)
        time.sleep(2)
        expectedd = "Task created"
        actuall = self.driver.find_element(By.XPATH,
                                           "(//div[contains(@class,'flex flex-row justify-between px-2')]//p[@class='font-medium text-sm ng-star-inserted'])").text
        if expectedd in actuall:
            self.List_tasks.append(True)
        else:
            self.List_tasks.append(False)
        # self.driver.find_element(By.XPATH, self.).click()
        time.sleep(2)
        if False not in self.List_tasks:
            return True
        else:
            return False


    def isCommentAddedInTask(self):
        l=[]
        c = self.driver.find_element(By.XPATH, "//a[@id='activities']")
        self.driver.execute_script("arguments[0].click()", c)
        time.sleep(2)
        expectedd = "Task comment added by"
        actuall = self.driver.find_element(By.XPATH,"(//div[contains(@class,'flex flex-row justify-between px-2')]//p[@class='font-medium text-sm ng-star-inserted'])").text
        if expectedd in actuall:
            l.append(True)
        else:
            l.append(False)
        # self.driver.find_element(By.XPATH, self.).click()
        time.sleep(2)
        if False not in l:
            return True
        else:
            return False
