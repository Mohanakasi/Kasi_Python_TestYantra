"""*
   * *
   * * *
   * * * *
             """


# for row in range(4):
#     for col in range(row+1):
#         print("*", end=' ')
#     print()


# for row in range(4):
#     for col in range(4):
#         if row == col:
#             print("*", end = ' ')
#     print()


# for row in range(1,5):
#     print("* "*row)




# for row in range(1,5):
#     print(f'{"* " * row: >8}')






for row in range(1,5):
    for col in range(1,row+1):
        print(col, end = ' ')
    print()





# for row in range(4):
#     for col in range(0, row+1):
#         print(chr(ord("a")+col), end = ' ')
#     print()

"""to read excel files"""
"""install xlrd package standard version 1.2.0"""
import xlrd
path = r"E:\temp_data.xlsx"
"""opening the workbook"""
xl_wb_obj = xlrd.open_workbook(path)

"""opeining the spreadsheet"""
xl_sheet = xl_wb_obj.sheet_by_name("Sheet1")
"""getting all the rows in the sheet as generator object"""
data = xl_sheet.get_rows()
print(data) # generator object

"""traversing through each row"""
# for row in data:
#     print(row)

"""traversing through each row and getting the values in string format"""

for row in data:
    print(row[0].value, row[1].value)





"""the frame work is the hybrid frame work where pytest """