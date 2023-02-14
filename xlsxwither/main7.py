import xlsxwriter as xw

# inserting column chart
workbook = xw.Workbook('seventh_example.xlsx')
worksheet = workbook.add_worksheet()

bold_row = workbook.add_format({'bold': 1})

titles = ['Vendedores', 'Total Vendas']
values = [
    ['Ana', 'Pedro', 'Alan', 'Francisco', 'Rosa', 'Amanda'],
    [400, 300, 89, 34, 350, 120]
]

worksheet.write_row('A1', titles, bold_row)
worksheet.write_column('A2', values[0])
worksheet.write_column('B2', values[1])

graphic = workbook.add_chart({'type': 'column'})
graphic.add_series({
    'name': '=$B$1',
    'categories': '=$A$2:$A$7',
    'values': '=$B2$:$B7$'
})

graphic.set_title({'name': 'Grafico Total de Vendas'})
graphic.set_x_axis({'name': 'Vendedores'})
graphic.set_y_axis({'name': 'Vendas'})

graphic.set_style(11)
worksheet.insert_chart('D2', graphic, {'x_offset': 25, 'y_offset': 10})

workbook.close()
