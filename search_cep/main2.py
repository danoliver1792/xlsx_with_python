from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from openpyxl import load_workbook
from time import sleep

# installing chrome driver
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get('https://buscacepinter.correios.com.br/app/endereco/index.php')
browser.maximize_window()

# setting up our excel spreadsheet
file_name = r'/home/danrlei/PycharmProjects/python8/xlsx/search_cep/address_2.xlsx'
sheet_address = load_workbook(file_name)
sheet_select = sheet_address['cep']

# entering the website and informing the zip code
browser.find_element(By.NAME, 'endereco').send_keys('81610170')
sleep(3)
browser.find_element(By.NAME, 'btn_pesquisar').click()
sleep(3)

for row in range(2, len(sheet_select['A']) + 1):
    browser.find_element(By.ID, 'btn_nbusca').click()
    sleep(3)
    # turning it into a string and going to the next line
    cep_search = sheet_select['A%s' % row].value
    sleep(2)
    browser.find_element(By.NAME, 'endereco').send_keys(cep_search)
    sleep(3)
    browser.find_element(By.NAME, 'btn_pesquisar').click()
    sleep(3)

    road = browser.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[1]')[0].text
    sleep(2)
    neighborhood = browser.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[2]')[0].text
    sleep(2)
    city = browser.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[3]')[0].text
    sleep(2)
    cep = browser.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[4]')[0].text
    sleep(2)

    sheet_cep_print = sheet_address['cep']
    row_sheet = len(sheet_cep_print['A']) + 1
    column_a = 'A' + str(row_sheet)
    column_b = 'B' + str(row_sheet)
    column_c = 'C' + str(row_sheet)
    column_d = 'D' + str(row_sheet)

    # printing the information in the cells
    sheet_cep_print[column_a] = road
    sheet_cep_print[column_b] = neighborhood
    sheet_cep_print[column_c] = city
    sheet_cep_print[column_d] = cep

sheet_address.save(filename=file_name)
