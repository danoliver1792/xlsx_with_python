from openpyxl import load_workbook


file_path = r"/home/danrlei/PycharmProjects/python8/xlsx/form/dados_form.xlsx"
sheet = load_workbook(filename=file_path)
sheet_select = sheet['Planilha1']

for row in range(2, len(sheet_select['A']) + 1):
    name = sheet_select['A%s' % row].value
    email = sheet_select['B%s' % row].value
    phone = sheet_select['C%s' % row].value
    sex = sheet_select['D%s' % row].value
    about = sheet_select['E%s' % row].value

    print(name)
    print(email)
    print(phone)
    print(sex)
    print(about)
    