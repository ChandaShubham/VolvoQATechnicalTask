# Validating all SUV and Sedan models are available or not

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import HtmlTestRunner
from volvo_task.locators.locators import locators
from volvo_task.page_object.home_page import homePage

class volvoHomePage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver= webdriver.Chrome(executable_path=r"..\AppData\Local\Programs\Python\Python311\Lib\site-packages\selenium\webdriver\chrome\chromedriver-win64\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.get('https://www.volvocars.com/in/')
        cls.driver.maximize_window()

    def handle_cookie_consent(self):

        cookieElement = self.driver.find_element_by_id(locators.cookie_element_id)
        print(locators.cookie_element_id)
        if cookieElement.is_displayed():
            cookieElement.click()

    def test_validate_suv_models(self): 
        
        driver = self.driver
        home_page = homePage(driver)
        
        # Create an instance of ActionChains
        actions = ActionChains(driver)
        # Scroll down using action chains
        actions.send_keys(Keys.PAGE_DOWN).perform()  # Scrolls down one page
         
        # Alternatively, scroll to a specific element
        allModelElement = driver.find_element_by_xpath(locators.allModel_element_xpath)
        actions.move_to_element(allModelElement).perform()
        
        #Validating SUV models
        home_page.suv_element()
         
        for xpath in locators.suv_models_xpath_list:
            #Find element by XPath
            suv_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
         
            #Perform assertions on the element
            assert suv_element.is_displayed(), f"Element '{xpath}' is not displayed"
            print(f"Assertion passed: Element '{xpath}' is displayed")

    def test_validate_sedan_models(self):
        driver = self.driver
        home_page = homePage(driver)
        # Validating Sedan models
        home_page.sedan_element()
         
        for xpath in locators.sedan_models_xpath_list:
            # Find element by XPath
            sedan_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
         
            # Perform assertions on the element
            assert sedan_element.is_displayed(), f"Element '{xpath}' is not displayed"
            print(f"Assertion passed: Element '{xpath}' is displayed")

    @classmethod
    def tearDownClass(cls):
        # Close the WebDriver instance
        cls.driver.close()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../eclipse-workspace/volvo_project/reports'))