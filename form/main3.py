from openpyxl import load_workbook
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

file_path = r"/home/danrlei/PycharmProjects/python8/xlsx/form/dados_form.xlsx"
sheet = load_workbook(filename=file_path)
sheet_select = sheet['Planilha1']

for row in range(2, len(sheet_select['A']) + 1):
    name = sheet_select['A%s' % row].value
    email = sheet_select['B%s' % row].value
    phone = sheet_select['C%s' % row].value
    sex = sheet_select['D%s' % row].value
    about = sheet_select['E%s' % row].value

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://pt.surveymonkey.com/r/Y9Y6FFR")
    driver.maximize_window()
    sleep(3)

    driver.find_element(By.NAME, '683928983').send_keys(name)
    sleep(2)
    driver.find_element(By.NAME, '683932318').send_keys(email)
    sleep(2)
    driver.find_element(By.NAME, '683930688').send_keys(phone)
    sleep(2)

    if sex == "Masculino":
        driver.find_element(By.XPATH, '//*[@id="683931881_4497366118_label"]/span[1]').click()
        sleep(2)
    else:
        driver.find_element(By.XPATH, '//*[@id="683931881_4497366119_label"]/span[1]').click()
        sleep(2)

    driver.find_element(By.NAME, '683932969').send_keys(about)
    sleep(2)
    driver.find_element(By.XPATH, '//*[@id="patas"]/main/article/section/form/div[2]/button').click()
    sleep(5)
