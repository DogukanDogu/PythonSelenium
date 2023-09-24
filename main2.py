from selenium import webdriver
from webdrivermanager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.atilsamancioglu.com")
time.sleep(2)
blog_page = driver.find_element(By.XPATH,"/html/body/div[1]/header/div[1]/div[3]/nav/div/ul/li[3]/a")
blog_page.click()

time.sleep(2)

#read_buttons = driver.find_elements(By.CLASS_NAME,"button")

read_button = driver.find_element(By.CLASS_NAME,"button")
time.sleep(2)
read_button.click()
time.sleep(2)
article_list = driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/aside[4]")

print(f"atilsamancioglu.com has {len(article_list.text.splitlines())} blog posts")
