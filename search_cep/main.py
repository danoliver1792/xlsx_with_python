from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get('https://buscacepinter.correios.com.br/app/endereco/index.php')
browser.maximize_window()

browser.find_element(By.NAME, 'endereco').send_keys('81610170')
sleep(3)
browser.find_element(By.NAME, 'btn_pesquisar').click()
sleep(3)

road = browser.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[1]')[0].text
print(road)
sleep(2)
neighborhood = browser.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[2]')[0].text
print(neighborhood)
sleep(2)
city = browser.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[3]')[0].text
print(city)
sleep(2)
cep = browser.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[3]')[0].text
sleep(2)
