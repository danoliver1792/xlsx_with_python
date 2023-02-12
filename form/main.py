from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://pt.surveymonkey.com/r/Y9Y6FFR")
driver.maximize_window()
sleep(3)

driver.find_element(By.NAME, '683928983').send_keys('Danrlei')
sleep(2)
driver.find_element(By.NAME, '683932318').send_keys('danrlei.jesus@hotmail.com')
sleep(2)
driver.find_element(By.NAME, '683930688').send_keys('41992220452')
sleep(2)
driver.find_element(By.XPATH, '//*[@id="683931881_4497366118_label"]/span[1]').click()
sleep(2)
driver.find_element(By.NAME, '683932969').send_keys('Sou dev')
sleep(2)
driver.find_element(By.XPATH, '//*[@id="patas"]/main/article/section/form/div[2]/button').click()
sleep(5)
