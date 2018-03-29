import xlrd
import openpyxl

a = openpyxl
d = a.load_workbook("images.xlsx")
e = d.active
print (e['a1'].value)
e['a1'].value = "Gemi"
d.save("images.xlsx")
