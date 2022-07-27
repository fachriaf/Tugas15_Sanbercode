import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}
  
    def teardown_method(self, method):
        self.driver.quit() 
        
    def test_a_success_login(self): 
        # steps
        driver = self.driver #buka web browser
        self.driver.get("https://formy-project.herokuapp.com/form")
        time.sleep(1)
        self.driver.set_window_size(1376, 744)
        time.sleep(1)
        self.driver.find_element(By.ID, "first-name").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "first-name").send_keys("fachri")
        time.sleep(1)
        self.driver.find_element(By.ID, "last-name").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "last-name").send_keys("aldin")
        time.sleep(1)
        self.driver.find_element(By.ID, "job-title").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "job-title").send_keys("quality assurance")
        time.sleep(1)
        self.driver.find_element(By.ID, "radio-button-1").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".input-group:nth-child(7) > .col-sm-8:nth-child(3)").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "radio-button-2").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "radio-button-3").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "checkbox-3").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "select-menu").click()
        time.sleep(1)
        dropdown = self.driver.find_element(By.ID, "select-menu")
        time.sleep(1)
        dropdown.find_element(By.XPATH, "//option[. = '5-9']").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "datepicker").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//option['27/07/2022']").click()
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, "Submit").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "h1").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "h1").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "h1").text == "Thanks for submitting your form"
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "h1").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "h1").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "h1").text == "Thanks for submitting your form"
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "html").click()
        time.sleep(1)


if __name__ == "__main__": 
    unittest.main()