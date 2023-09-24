import unittest
from selenium import webdriver
from webdrivermanager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
from selenium.webdriver.common.keys import Keys

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()


    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://pypi.org")
        #print(driver.page_source)
        #self.assertIn("PyPI",driver.title)
        element = driver.find_element(By.NAME,"q")
        element.send_keys("Selenium")
        element.send_keys(Keys.ENTER)
        assert "There were no results for" not in driver.page_source



    def tearDown(self) -> None:
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
