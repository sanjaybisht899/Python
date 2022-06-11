
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "Data"
ws.append(['snapshot', 'leaf current field position','leaf previous field position',])
a = ["Ford", "Volvo", "BMW"]
char='A'
for i in range(0,len(a)):
    ws[char + str(i+2)]=a[i]

wb.save('data.xlsx')