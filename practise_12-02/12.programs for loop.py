"progrmas"
"print the elements in the list if the word is of even length, if the word is of odd length reverse it"
list_ = ['kasi', 'external','is','control']
# for item in list_:
#     if len(item) % 2 == 0:
#         print(item)
#     else:
#         print(item[::-1])




"loop breaking statements"
"pass"
"if you want to empty the block you have to use pass keyword"
"ex"
# for item in range(0,10):
#     if item % 2 == 0:
#         pass
#     else:
#         print(item)
#
"wap to return the index of the first occurance of the given elemet"
list_ = [10,20,30,40,50]
ele = 20
# for index,item in enumerate(list_):
#     if item == ele:
#         print(item,"----->",index)
#         break
# else:
#     print("item not found")

"wap to print elements other than given number"
list_ = [10,20,30,40,50]
ele = 20
# for index,item in enumerate(list_):
#     if item == ele:
#         continue
#     else:
#         print(item, end = ' ')

"wap to remove the given element from the list"
list_ = [10, 20, 30, 40, 50]
ele = 20
# for index, item in enumerate(list_):
#     if item == ele:
#         list_.remove(item)
# print(list_)

"to prime numbers in the range using for loop"
# for num in range(2,20):
#     if num > 1:
#         for i in range(2,num):
#             if num % i == 0:
#                 break
#         else:
#             print(num, end=' ')


"""zip class"""
"zip will map the elements of the one iterable with elements in the another iterable"
"it will return a list of tuples. each tuple containing first element of iterable1 and second ele of iterable2 viceversa"
"if the both the iterables are not same data loss will loss occur"
"string ---- zip"
s1 = 'hai'
s2 = 'hek'
# print(list(zip(s1,s2))) # [('h', 'h'), ('a', 'e'), ('i', 'k')]

"list zip "
l = [1,2,3]
l2 = ['kasi',4,56]
# print(list(zip(l,l2))) # [(1, 'kasi'), (2, 4), (3, 56)]

"set zip"
s ={'kasi','jmr0',2020}
s2 = {'madhu','mohana',2020}
# print(list(zip(s,s2))) #[('jmr0', 'mohana'), (2020, 2020), ('kasi', 'madhu')]

"dictionary zip"
d = {'a':10, 'b':20, 'c':30}
d1 = {'d':40, 'e':50, 'g':9}
# print(list(zip(d,d1)))  # [('a', 'd'), ('b', 'e'), ('c', 'g')] only keys mapped


"zip_longest"
"if the two iterables are different length we go for zip_longest"
"to avoid data loss occur in zip class we use zip_longest"
"zip_longest is available in itertools module"

from itertools import zip_longest
s = 'hello'
s1 = 'hai'
# print(list(zip_longest(s,s1))) # [('h', 'h'), ('e', 'a'), ('l', 'i'), ('l', None), ('o', None)]

l = [1,2,3,45,6]
l2 = [8,6,8,9,4,5,6]
# print(list(zip_longest(l,l2))) # [(1, 8), (2, 6), (3, 8), (45, 9), (6, 4), (None, 5), (None, 6)]

"""wap to create a dictionary with word and it's count pair"""
# list_ = ['kasi','mohana','jmr','kasi',1,2,23,1,'kasi']
from collections import defaultdict
d = defaultdict(int)
for item in list_:
    d[item] += 1
# print(d)

"wap to create a dictionary of word and it's length pair of string"
"using inbuilt class"
string_ = 'kasi is a king of amaravathi'
d = defaultdict(int)
for item in string_.split():
    d[item] = len(item)
# print(d)
"without using any inbuilt method"
d = {}
for item in string_.split():
    d[item] = len(item)
# print(d)

"wap to create a dictionary word and it's length pair if the word is of even length"
d = {}
for item in string_.split():
    if len(item) % 2 == 0:
        d[item] = len(item)
# print(d)

"wap to create a dictionary word and it's length pair if the word is starting with vowel"
d = {}
for item in string_.split():
    if item[0].lower() in 'aeiou':
        d[item] = len(item)
# print(d)

"wap to create a dictionary with word and it's count pair only if the word is not repeated"
string_ = 'kasi is a king of kasi word'
# print(string_.count('kasi'))
# words = string_.split()
# d = defaultdict(int)
# for item in words:
#     if words.count(item) == 1:
#         d[item] = words.count(item)
# print(d)

"wap to create a dictionary with word and it's count pair only if the word is repeated"
string_ = 'kasi is a king of kasi word'
# print(string_.count('kasi'))
d = defaultdict(int)
for item in string_.split():
    if string_.count(item) > 1:
        d[item] = string_.count(item)
# print(d)

"wap to create a dictionary with word and it's count pair only if the word is repeated"
"without using inbuilt method"
string_ = 'kasi is a king of kasi word'
# print(string_.count('kasi'))
# print(string_.count('a'))
words = string_.split()
d = {}
for item in words:
    if words.count(item) > 1 and item not in d:
        d[item] = 1
    elif words.count(item) > 1 and item in d:
        d[item] += 1
# print(d)


"wap to reverse the values in the dictionary if the value is of type string"
d = {'a':10, 'b':300, 'c':80, 'd':'kasi', 'e':'jmr'}
for key in d:
    if isinstance(d[key], str):
        d[key] = d[key][::-1]
# print(d)

"wap to creat e dictionary with it's index and item in a given list"
# list_ = ['kasi','python','rao','jmr','bangalore']
# d = {}
# for index,item in enumerate(list_):
#     d[item] = index
# print(d)

"grouping flowers and animals in the below list"
# list_ = ['lotus-flower', 'lilly-flower','dog-animal','cat-animal','jasmine-flower']
# d = defaultdict(list)
# for item in list_:
#     word = item.split('-')
#     d[word[1]] += [word[0]]
# print(d)

# "wap to map cities and population into dictionary"
# cities = ['guntur','vijayawada','bangalore','chennai']
# population = [100,200,300,400]
# d = {}
# for city,pop in zip(cities,population):
#     d[city] = pop
# print(d)


