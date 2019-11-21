# do your magic here

import xlrd

loc = ("HSA_Freshman_3010.xlsx")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

# For row 0 and column 0


for i in range(sheet.nrows):
    fn = sheet.cell_value(i, 0)
    ln = sheet.cell_value(i, 1)

    print("student." + fn[0] + "." + ln + "@horizoncolumbus.org")