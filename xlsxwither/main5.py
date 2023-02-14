import xlsxwriter as xw

workbook = xw.Workbook('fifth_example.xlsx')
worksheet = workbook.add_worksheet()

font_color = workbook.add_format()
font_color.set_font_color('blue')

add_merge_cells = workbook.add_format({
    'bold': True,
    'border': 6,
    'align': 'center',
    'valign': 'vcenter',
    'size': 30,
    'fg_color': 'blue',
    'font_color': 'white'
})

worksheet.merge_range('A10:I10', 'Merge Cells', add_merge_cells)

worksheet.write('A3', 'Name')
worksheet.write('B3', 'Age')
worksheet.write('A4', 'Amanda', font_color)
worksheet.write('B4', 21, font_color)
worksheet.write('A5', 'Alan', font_color)
worksheet.write('B5', 28, font_color)

workbook.close()
