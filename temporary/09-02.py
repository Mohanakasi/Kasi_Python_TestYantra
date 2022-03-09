from collections import defaultdict
from collections import Counter
from itertools import islice
"""to read lines in a file"""
# path = r"C:\Users\Hp\PycharmProjects\Alpha_3\files_directory\txt_log_files\sample.txt"   # smaple.txt file path
# with open (path) as file:
#     for line in file:
#         print(line)


# path = r"C:\Users\Hp\PycharmProjects\Alpha_3\files_directory\txt_log_files\sample.txt"   # smaple.txt file path
# with open (path) as file:
#     count = 0
#     for line in file:
#         count += 1
#     print(f"no of lines in the file is {count}")

# """printing line and count of that line at a time"""
# path = r"C:\Users\Hp\PycharmProjects\Alpha_3\files_directory\txt_log_files\sample.txt"   # smaple.txt file path
# with open (path) as file:
#     count = 0
#     for line in file:
#         count += 1
#         print(line, count)

"""printing line and count of that line at a time""" """(using enumerate)"""

# path = r"C:\Users\Hp\PycharmProjects\Alpha_3\files_directory\txt_log_files\sample.txt"   # smaple.txt file path
# with open (path) as file:
#     for lineno_,line in enumerate(file, start = 2):
#         print(lineno_, line)


"""to count no of words in a entire file"""
# path = r"C:\Users\Hp\PycharmProjects\Alpha_3\files_directory\txt_log_files\sample.txt"   # smaple.txt file path
# with open (path) as file:
#     count = 0
#     for line in file:
#         word = line.split()
#         count += len(word)
#     print(count)

""""""
# path = r"C:\Users\Hp\PycharmProjects\Alpha_3\files_directory\txt_log_files\sample.txt"   # smaple.txt file path
# with open (path) as file:
#     list_ = []
#     for line in file:
#         list_  =  [line] + list_
#         for rline in list_:
#             print(rline)

# """printing dictionary with word and it's count pair  in a file"""
# path = r"C:\Users\Hp\PycharmProjects\Alpha_3\files_directory\txt_log_files\sample.txt"   # smaple.txt file path
# with open (path) as file:
#     res = {}
#     for line in file:
#         list_ = line.split()
#         for word in list_:
#             if word not in res:
#                 res[word] = 1
#             else:
#                 res[word] +=1
#     print(res)


"""printing dictionary with word and it's count pair  in a file"""
"""either we can use default dict for count or if we can do it manually bay checking ehether it is in d or not based on that"""
# path = r"C:\Users\Hp\PycharmProjects\Alpha_3\files_directory\txt_log_files\sample.txt"   # smaple.txt file path
# with open (path) as file:
#     from collections import defaultdict
#     d = defaultdict(int)
#     for line in file:
#         list_ = line.split()
#         for word in list_:
#             d[word] += 1
#     print(d)


"""to print only ip adresses of the data in the file"""
# path = r"C:\Users\Hp\PycharmProjects\Alpha_3\files_directory\txt_log_files\access-log.txt"   # smaple.txt file path
# with open (path) as file:
#     l = []
#     for line in file:
#         list_ = line.split(' ')
#         l.append(list_[0])
#
#
#     print(l)

# """wap to create a dictionary of ip adresses an it's count pair in access-log.txt file"""
"""using default dict"""
# path = r"C:\Users\Hp\PycharmProjects\Alpha_3\files_directory\txt_log_files\access-log.txt"
# with open(path) as file:
#     d = defaultdict(int)
#     for line in file:
#         if line.strip():
#             list_ = line.split()
#             d[list_[0]] +=1
#     print(d)

"""using counter classs"""
# path = r"C:\Users\Hp\PycharmProjects\Alpha_3\files_directory\txt_log_files\access-log.txt"
# from collections import Counter
# with open(path) as file:
#     l = []
#     for line in file:
#         if line.strip():
#             list_ = line.split()
#             l.append(list_[0])
#
#
# var = Counter(l)
# print(var)
# """tpo get most common word in it"""
# print(var.most_common())
path = r"C:\Users\Hp\PycharmProjects\Alpha_3\files_directory\txt_log_files\sample.txt"
n = 2
with open(path) as file:
   for lineno,line in enumerate(file):
       pass
