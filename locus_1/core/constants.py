import openpyxl


book = openpyxl.open('excel_data/real_data.xlsx')
sheet = book.active

LOCUSES = []

for row_index in range(3, sheet.max_row + 1):
    LOCUSES.append(sheet[row_index][0].value)

book.close()
