from volvo_task.locators.locators import locators

class homePage():
    
    def __init__(self, driver):
        self.driver = driver 
        
    def suv_element(self):
        self.driver.find_element_by_xpath(locators.suv_element_xpath).click()
        
    def sedan_element(self):
        self.driver.find_element_by_xpath(locators.sedan_element_xpath).click()