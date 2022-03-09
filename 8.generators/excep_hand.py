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


