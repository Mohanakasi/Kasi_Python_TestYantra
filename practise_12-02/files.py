import os
from collections import defaultdict
from collections import Counter
from itertools import islice
from collections import deque
import csv
import json
"wap to to count no of lines present in the file"
path = r"C:\Users\Hp\PycharmProjects\python_training\my_files\text files\sample.txt"
# with open(path) as file:
#     count = 0
#     for line in file:
#         count += 1
#     # print(count)

"wap to print line and line no from the file"
# with open(path) as file:
#     for lineno, line in enumerate(file):
#         print(lineno, line)

"wap to count no of words in a given file"
# with open(path) as file:
#     count = 0
#     for line in file:
#         count += len(line.split())
#     print(count)

"wap to print files from last of the file"
# with open(path) as file:
#     for line in reversed(list(file)):
#         print(line)

"wap to count the no of space in a file"
# with open(path) as file:
#     count = 0
#     for line in file:
#         count += line.count(' ')
#     print(count)

"wap to count the no words that are starting with vowels"
# with open(path) as file:
#     count = 0
#     for line in file:
#         words = line.split()
#         for word in words:
#             if word[0].lower() in 'aeiou':
#                 count += 1
#     print(count)

"wap to create a dictionary with word it's count pair in the given file"
# with open(path) as file:
#     d = defaultdict(int)
#     for line in file:
#         words = line.split()
#         for word in words:
#             d[word] += 1
#     print(d)

"wap to extract all the ip addresses from acceslog.txt file"
path = r'C:\Users\Hp\PycharmProjects\python_training\my_files\text files\access-log.txt'
# with open(path) as file:
#     l = []
#     for line in file:
#         if line.strip():
#             words = line.split()
#             l.append(words[0])
#
# print(l)
# ip_ = Counter(l)
# print(ip_)
# print(ip_.most_common(1)) # first most common ip

"to print nth line in a file"
"normal method"
# n = 10
# with open(path) as file:
#     for lineno, line in enumerate(file):
#         if lineno == n:
#             print(line)
#             break


"using islice "
# n = 10
# with open(path) as file:
#     res = islice(file, n-1, n)
#     print(list(res))

"wap to print last n lines"
"normal method"
n = 10
# with open(path) as file:
#     for lineno,line in enumerate(file):
#         pass
#     print(lineno)
#     file.seek(0)
#     res = islice(file, lineno-n, lineno)
#     print(list(res))

"using deque"
# with open(path) as file:
#     lines = deque(file, n)
#     print(list(lines))

"writing into file"
"it will overides the previous data present in the file"
path = r"C:\Users\Hp\PycharmProjects\python_training\my_files\text files\sindhu.txt"
# with open(path,'w') as file:
    # file.write([1,2,3]) # data writing must be of string only
    # file.write("new modified data")

"writing the data present in the one file to another file"
read_path = r"C:\Users\Hp\PycharmProjects\python_training\my_files\text files\sindhu12.txt"
writ_path = r"C:\Users\Hp\PycharmProjects\python_training\my_files\text files\sindhu.txt"
# with open(read_path) as file1, open(writ_path,'w') as file2:
#     for line in file1:
#         file2.write(line)

"if we want to insert iteables into file we have to make use of writelines"
path = r"C:\Users\Hp\PycharmProjects\python_training\my_files\text files\new.txt"
with open(path,'w') as file:
    file.writelines(['kasi','jmr','it','will''accept\n','only','strings','and','iam','done\n','this','is'])
    # even it accpeting iterable the iterable must contains only strings
