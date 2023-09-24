from selenium import webdriver
from webdrivermanager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com")
time.sleep(2)
#WebDriverWait(driver,4).until(expected_conditions.visibility_of_element_located((By.NAME,"q")))
input_search_text_by_name = driver.find_element(By.NAME,"q")
time.sleep(2)
#WebDriverWait(driver,4).until(expected_conditions.visibility_of_element_located((By.NAME,"btnK")))
input_button_search = driver.find_element(By.NAME,"btnK")
#input_search_text_by_class = driver.find_element(By.CLASS_NAME,"gLFyf")
#input_search_text_by_xpath = driver.find_element((By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea"))

#print(input_search_text_by_name)
#print(input_search_text_by_class)
#print(input_search_text_by_xpath)

input_search_text_by_name.send_keys("Doğukan Doğu")
time.sleep(2)
#WebDriverWait(driver,4).until(expected_conditions.element_to_be_clickable((By.NAME,"btnK")))
input_button_search.click()


while True:
    continue
