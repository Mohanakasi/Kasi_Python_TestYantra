path = r"C:\Users\Hp\PycharmProjects\Alpha_3\files_directory\txt_log_files\sample.log"
# with open(path) as file:
#     count = 0
#     for line in file:
#         print(line, len(line), sep = "$", end = " ")
#         print()

# with open(path) as file:
#     for line in file:
#         if line.strip():
#             list_ = line.split('  ')
#             print(list_[-1])

# path = r"C:\Users\Hp\PycharmProjects\Alpha_3\files_directory\txt_log_files\football.txt"
# with open(path, encoding = "UTF-8") as file:
#     for line in file:
#         if line.strip():
#             list_ = line.split('\t')
#             print(list_)
#             print(list_[1])

from collections import *
with open(path) as file:
    dd = {}
    for line in file:
        if line.strip():
            list_ = line.split()
            for word in list_:
                dd
