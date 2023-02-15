import openpyxl

workbook = openpyxl.load_workbook('meses.xlsx')
sheet1 = workbook['Sheet1']
sheet2 = workbook['Sheet2']

cells = sheet1['A2':'A13']

for row in cells:
    for cell in row:
        sheet2[cell.coordinate] = cell.value

workbook.save('meses_editado.xlsx')
