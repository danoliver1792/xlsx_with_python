import xlsxwriter as xw

# color formatting in Excel
workbook = xw.Workbook('second_example.xlsx')
worksheet = workbook.add_worksheet()

background_color = workbook.add_format({'fg_color': 'yellow'})
font_color = workbook.add_format()
font_color.set_font_color('green')
font_color_two = workbook.add_format()
font_color_two.set_font_color('red')

worksheet.write('A1', 'Name', background_color)
worksheet.write('B1', 'Age', background_color)
worksheet.write('A2', 'Amanda', font_color)
worksheet.write('B2', 21, font_color_two)
worksheet.write('A3', 'Alan', font_color)
worksheet.write('B3', 28, font_color_two)

workbook.close()
