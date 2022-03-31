a = 10
b = 0
# try:
#     print(a/b)
# except ZeroDivisionError:
#     print("in zerodivision bloack ")
# print("heill")

"""multiple errors handling"""
a = 10
b = 0
try:
    print(a/b)
    # print(l.append(10))
except ZeroDivisionError:
    print("in zerodivision bloack ")
except NameError:
    print("in name error bloack")
print("heill")


import xlrd
workbook = xlrd.open_workbook("new_100.xlsx")
sheet_ = workbook.sheet_by_name("temp30")
rows_ = sheet_.nrows
cols_ = sheet_.ncols
dict_ = {}
for curre_row in range(rows_):
    print(curre_row)
    user_name = sheet_.cell_value(curre_row, 0)
    password_ = sheet_.cell_value(curre_row, 1)
    dict_[user_name] = int(password_)
print(dict_)



