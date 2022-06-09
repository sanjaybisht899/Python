from openpyxl import Workbook , load_workbook

wb = load_workbook('Data.xlsx')
ws = wb.active
print(ws)