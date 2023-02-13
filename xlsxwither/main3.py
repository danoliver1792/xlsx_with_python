import xlsxwriter as xw

workbook = xw.Workbook('third_example.xlsx')
worksheet = workbook.add_worksheet()

font_color = workbook.add_format()
font_color.set_font_color('blue')

font_bg_color = workbook.add_format({
    'align': 'center',
    'font_color': 'red',
    'bold': True,
    'bg_color': 'black'
})

worksheet.write('A1', 'Name', font_bg_color)
worksheet.write('B1', 'Age', font_bg_color)
worksheet.write('A2', 'Amanda', font_color)
worksheet.write('B2', 21, font_color)
worksheet.write('A3', 'Alan', font_color)
worksheet.write('B3', 28, font_color)

workbook.close()
