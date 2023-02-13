import xlsxwriter as xw

# inserting formulas
workbook = xw.Workbook('fourth_example.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write('A1', 'Group One')
worksheet.write('B1', 'Group Two')
worksheet.write('C1', 'Group Three')
worksheet.write('A2', 21)
worksheet.write('B2', 26)
worksheet.write('C2', 28)
worksheet.write('A3', 26)
worksheet.write('B3', 31)
worksheet.write('C3', 22)
worksheet.write('A4', 24)
worksheet.write('B4', 28)
worksheet.write('C4', 23)

worksheet.write_formula('A5', '=SUM(A2:A4)')
worksheet.write_formula('B5', '=SUM(B2:B4)')
worksheet.write_formula('C5', '=SUM(C2:C4)')

worksheet.write_formula('A6', '=AVERAGE(A2:A4)')
worksheet.write_formula('B6', '=AVERAGE(B2:B4)')
worksheet.write_formula('C6', '=AVERAGE(C2:C4)')

workbook.close()
