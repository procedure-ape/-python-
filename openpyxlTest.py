import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active

x = ['asdasd','dsadsa','123123']
sheet.append(x)

wb.save(filename = 'test.xlsx')
