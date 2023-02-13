import xlsxwriter as xw

# configuring workbook
workbook = xw.Workbook('first_example.xlsx')
worksheet = workbook.add_worksheet()

# writing in cells
worksheet.write('A1', 'Name')
worksheet.write('B1', 'Age')
worksheet.write('A2', 'Amanda')
worksheet.write('B2', 21)
worksheet.write('A3', 'Alan')
worksheet.write('B3', 28)

workbook.close()
