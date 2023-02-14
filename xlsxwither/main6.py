import xlsxwriter as xw

workbook = xw.Workbook('sixth_example.xlsx')
worksheet = workbook.add_worksheet()

# conditional formatting
max_format = workbook.add_format({
    'bg_color': 'green',
    'font_color': 'white'
})

min_format = workbook.add_format({
    'bg_color': 'red',
    'font_color': 'white'
})

# inserting values
insert_data = [
    ['Column 1', 'Column 2', 'Column 3', 'Column 4'],
    [34, 50, 12, 34],
    [23, 32, 76, 51],
    [43, 29, 34, 12],
    [29, 58, 73, 19]
]

worksheet.write('A1', 'conditional formatting in cells')

for row in enumerate(insert_data):
    worksheet.write_row(row + 2, 1, range)

worksheet.conditional_format('B4:E8', {'type': 'cell', 'criteria': '>=', 'value': 50, 'format': max_format})
worksheet.conditional_format('B4:E8', {'type': 'cell', 'criteria': '<', 'value': 50, 'format': min_format})
