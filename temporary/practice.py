# list_ = ['Kasi n1233adh', 'Mohana Kasi', 'Jmr','robo19950','KASIgmc']
#
# # for index,item in enumerate(list_):
# #     list_[index] = item.lower()
# # print(list_)
#
# # list2_ = []
# # for item in list_:
# #     temp = ''
# #     for char in item:
# #         if char.islower() :
# #             temp += char.upper()
# #         else:
# #             temp += char
# #     list2_.append(temp)
# # print(list2_)

""'extracting first two characters in a string""'
# a = 'kasinadh'
# print(a[:2])

""'extracting last two characters in a string""'
# a = 'kasinadh'
# print(a[-2:])

# a = [1,2,3,40]
# print(id(a))
# a[2] = 1008
# print(id(a))
# print(a)
#
# string_ = 'python'
# print('kasisis'.upper())
#


# a = [1,2,3,2,8,4,3,4,1]
# print(a.pop())
# print(a.remove(4))
# print(a)
#
#
#
# a = {1,2,32,4}
# print(a.add('kasi'))
# print(a)
#
# a ={'kasi':1008,'jmr':2020}
# print(a.popitem())
# a.setdefault('rao')
# print(a)
# print(a.setdefault('kasi',2020))
# print(a)
#
# a = 'kasi nadh'
# i = 0
# while i < len(a):
#     print(a[i])
#     i += 1
# list_ = [1,2,63,4]
# i = 0
# while i < len(list_):
#     print(list_[i])
#     i += 1
#
# a = (1,2,3,80)
# i = 0
# while i < len(a):
#     print(a[i])
#     i += 1
#
# a = 'python is a language'
# start = 0
# end = 1
# count = 0
# while bool(a[start: end]) != False:
#     count += 1
#     start += 1
#     end += 1
#
# print(count)

"""to print -1 to -10"""
# i = -1
# while i > -11 :
#     print(i)
#     i -= 1

"""to print -11 to -1"""
# i =-11
#
# while i < 0:
#      print(i)
#      i += 1

# """to print 1 to 10"""
# i = 1
# while i < 11:
#     print(i)
#     i += 1

# """to print 10 to 1"""
# i = 10
# while i > 0 :
#     print(i)
#     i -= 1
#
#
# l,*l2,l3 = (1,2,3,4)
# print(l)
# print(l2)
# print(l3)



# string_ = 'string'
# for index,char in enumerate(string_):
#     print(index, char)
#
# print(tuple(enumerate(string_)))
# print(tuple(reversed(string_)))
# for item in enumerate(string_):
#     print(item)
"""modifying original list if the string is of odd lenth reversing if it is even keep as it is"""
# list_ = ['kasi', 'guntur', 'and', 'make','fighter']
# for index,item in enumerate(list_):
#     if len(item) % 2 == 0:
#         list_[index] = item
#     else:
#         list_[index] = item[::-1]
# print(list_)



"write a program to print only the values from the dictionary"
# dict_ = {'python':'language', 'kasi':'guntur', 'bangalore':'karnataka', 'guntur':'ap'}
# for value in dict_.values():
#     print(value, end=' ')
# print()
#
# for key,value in dict_.items():
#     print(key, value, sep='---->',end=' ')

"write a program to create a dictionary with word and it's count pair in a string"
# string_ = 'kasi is from guntur and guntur is a big city and kasi knows python'
# words = string_.split()
# from collections import defaultdict
# dict_ = defaultdict(int)
# for word in words:
#     dict_[word] += 1
# print(dict_)


"write a program to create a dictionary with word and it's length pair in a string"
# string_ = 'kasi is from guntur and guntur is a big city and kasi knows python'
# words = string_.split()
# from collections import defaultdict
# dict_ = defaultdict(int)
# for word in words:
#     dict_[word] = len(word)
# print(dict_)


"write a program to create dictionary with word and it's length pair only if the word is of odd length"
# string_ = 'kasi is from guntur and guntur is a big city and kasi knows python'
# words = string_.split()
# dict_ = {}
# for word in words:
#     if len(word) % 2 != 0:
#         dict_[word] = len(word)
# print(dict_)
# #
# from collections import defaultdict
# dd = defaultdict(int)
# for word in words:
#     if len(word) %2 != 0:
#         dd[word] = len(word)
# print(dd)
#
# string_ = 'kasi is from guntur and guntur is a big city and kasi knows python'
# words = string_.split()
# from collections import defaultdict
# dd =defaultdict(int)
# for word in words:
#     if word[0].lower() in 'aeiou':
#         dd[word]  = len(word)
# print(dd)

"write a program to create a dictionary with word and it's count pair only if the word is not repeated"
# string_ = 'kasi is from guntur and guntur is a big city and kasi knows python'
# words = string_.split()
#
# for word in words:
#     if words.count(word) == 1:
#         d[word] = words.count(word)
# print(d)

# dict_ = {'a':1008, 'b': 'kasi', 'c': 'jmr', 'd':2020}
# for key in dict_:
#     if isinstance(dict_[key], str):
#         dict_[key] = dict_[key][::-1]
# print(dict_)

# for key,value in dict_.items():
#     if isinstance(value, str):
#         dict_[key] = value[::-1]
# print(dict_)

"""wap to get all the duplicate items and no of times the item is repeated in the list"""
string_ = 'kasi is from guntur and guntur is a big city and kasi knows python'
words = string_.split()
d ={}
# for item in words:
#     if item not in d and words.count(item) > 1:
#         d[item] = 1
#     elif item in d and words.count(item) > 1:
#         d[item] += 1
# print(d)
#
# from collections import defaultdict
# dd = defaultdict(int)
# for item in words:
#     if words.count(item) > 1:
#         dd[item] += 1
# print(dd)

#
# string_ = 'kasi is from guntur and guntur is a big city and kasi knows python and kasi in bangalore'
# words = string_.split()
# from collections import defaultdict
# dd = defaultdict(list)
# for word in words:
#     if words.count(word) > 1:
#         dd[words.count(word)] += [word]
# print(dd)


# string_ = 'kasi is from guntur and guntur is a big city and kasi knows python'
# words = string_.split()
# d ={}
# for index, word in enumerate(words):
#     if word not in d:
#         d[word] = [index]
#     else:
#         d[word] += [index]
# print(d)

# from collections import defaultdict
# dd = defaultdict(list)
# for index,item in enumerate(words):
#     dd[item] += [index]
# print(dd)


# string_ = 'kasi is from guntur and guntur is a big city and kasi knows python'
# words = string_.split()
# d = {word: words.count(word) for word in words}
# print(d)


# d = {word:words.count(word) for word in words if len(word) % 2 == 0}
# print(d)

# d = {index:word[::-1] if len(word) % 2 != 0 else word for index,word in enumerate(words)}
# print(d)

# d = {word:len(word) for word in words if word[0].lower() in 'aeiou'}
# print(d)

"""item & index pair only if the item is of string """
# d = {item:index for index,item in enumerate(words) if isinstance(item, str)}
# print(d)

# d = {'a': 1008, 'b':20, 'c': 30}
# dd = {value:key for key,value in d.items()}
# print(dd)

# string_ = 'kasi nadh'
# d = {char:ord(char) for char in string_}


# def func(end, start=2):
#     for num in range(start, end):
#         if num>1:
#             for i in range(2,num):
#                 if num % i == 0:
#                     break
#             else:
#                 print(num, end =' ')
#
# func(20)

"""to print first 10 fibonaci series"""
# def fibo(n):
#     first = 0
#     second = 1
#     i = 0
#     while i < n:
#         print(first)
#         c = first +second
#         first = second
#         second = c
#         i += 1
# fibo(10)

"""to check whether a number is a fibo number or not"""
# def fibo(num):
#     first = 0
#     second = 1
#     while first <= num:
#         if first == num:
#             return f"the {num} is a fibo number"
#         c = first + second
#         first = second
#         second = c
#     return f"the {num} is not  fibo number"
# print(fibo(89))

"""generate fibo numbers from 1 to 100"""
# def fibo_num(end, start = 0):
#     first = 0
#     second = 1
#     list_ = []
#     while first <= end:
#         list_.append(first)
#         c = first + second
#         first = second
#         second = c
#     return list_
# print(fibo_num(100))


# def func(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum
#
# print(func(1,2.5,3.5,89,59,520))


# def sam(*args):
#     for item in args:
#         if isinstance(item,int):
#             print(item)
#
# sam(1,2,3,3.5,4.,50+50j,True,'kasi')

# def sam(*args):
#     for item in args:
#         if isinstance(item, str):
#             print(item[::-1])
#
# sam(1,2,3,4,0,4.5,50+50j,True,'kais','python','jmr')


# def func(**kwargs):
#     for key,item in kwargs.items():
#         print(key, item, sep='----->')
#
# func(a=10,b=20,c=30)


# l = [1,2,3,4,5,'kasi']
# def func(*args):
#     for item in args:
#         print(item)
#
# func(*l)


# def func(a:int, b:float):
#     return a+b
# print(func(1,2.5))


"""CHECKING A NUMBER WHETHER IT IS A PRIME OR NOT"""
# def prime(num):
#     if num > 1:
#         for i in range(2,num):
#             if num % i == 0:
#                 return f"the {num} is not a prime"
#         else:
#             return f"the {num} is a prime"
#     else:
#         return f"please enter the numbers greater than 1"
#
# print(prime(6))

"WRITE A PROGRAM TO RETURN FIRST DIGIT OF A NUMBER"
# def check(num):
#     temp = str(num)
#     return int(temp[0])
#
# print(check(10008))

# def tailed(sequence, n):
#     return sequence[-n:]
#
# print(tailed('kasi learns python', 4))


# def numbers(n):
#     if n < 10:
#         print(n)
#         n += 1
#         return numbers(n)
#     return n
#
# print(numbers(1))


# def numbers(start, end):
#     if start > end:
#         print(n)
#         n -= 1
#         return numbers(n)
#     return n
#
#
# print(numbers(10,1))

# """wap to get the indexes of each item in the below list"""
# names  = ['apple', 'google', 'apple','yahoo', 'yahoo', 'google', 'gmail','gmail']
# from collections import defaultdict
# dd = defaultdict(list)
# for index,item in enumerate(names):
#     dd[item] += [index]
# print(dd)
#
#
# """reverse the values in the dictionary if the value is of type string"""
#
# d = {'a': 'hello', 'b': 100, 'c':10.1, 'd':'world'}
# for key,value in d.items():
#     if isinstance(value,str):
#         d[key] = value[::-1]
# print(d)


# """write a program to get all the duplicate items and no of times that is repeated in the list"""
# names  = ['apple', 'google', 'apple','yahoo', 'yahoo', 'google', 'gmail','gmail', 'apple']
# from collections import defaultdict
# dd = defaultdict(list)
# for item in names:
#     if names.count(item) > 1:
#         dd[names.count(item)] += [item]
#
# print(dd)


# """creating dictionary of cities and population pairs using dictionary comprehension"""
# cities = ['tokyo', 'delhoi', 'mumbai', 'bengalore', 'chennai']
# population = [100, 200, 300, 4000, 500]
# dict_ = {city:pop for city,pop in zip(cities, population)}
# print(dict_)

"""write a program to flip keys and values"""
# d = {'a': 'hello', 'b': 100, 'c':10.1, 'd':'world'}
# dict_ = {}
# for key in d:
#     dict_[d[key]] = key
# print(dict_)
# """or"""
# for key,value in d.items():
#     dict_[value] = key
# print(dict_)
# """group even and odd values using dictionary comprehension0"""
# l = [1,2,2,3,4,4,5,5,5,6,7,7,8,8,8,88,89,99]
# d = {}






# """group both of the dictionary items in a single dictionary using dictionary coprehensin"""
# D = {'names': 'apple', 'ID': 152778}
# d = {'names': 'apple', 'ID': 657678}
#
# dd = {key1:d[key2] if keyfor key1,key2 in zip(D,d)}
# print(dd)




# T = (9,56,78,123,456)
# dd = {item:ord(item) for item in T}
# print(dd)


# list_ = ['food@table', 'lilly@flower', 'human@walk', 'being@work']
# dd = {item.split('@')[0]:item.split('@')[1] for item in list_}
# print(dd)




# s = [(4,56,78),('one', 'two', 'three')]
# n1,*res,n2 = s
# dd = {string_:num for num,string_ in zip(n1,n2)}
# print(dd)

n1,n2 = s = [(4,56,78),('one', 'two', 'three')]

# list_ = ['kasi', 'Jmr','Python']
# def upper(item):
#     return item.upper()
#
# res = map(upper, list_)
# print(list(res))

# "wap to convert all the negative numbers into positive using map"
# list_ = [-1,-2,25,-350,650]
# def pos(num):
#     if num < 0:
#         return abs(num)
#
# res = map(pos, list_)
# print(list(res))


# """wap that returns list all numbers to the power of therir indices"""
#
# list_ = [1,8,9,6]
# def power(item):
#     index,item = item
#     return item ** index
#
# res = map(power, enumerate(list_))
# print(list(res))

# """wap that returns all the words in the sentence which are in lower"""
# sentence = 'hello world Python kasi'
# def func(word):
#     if word.islower():
#         return word
#
# res = map(func, sentence.split())
# print(list(res))

# """lambda expression to return lat element of a sequence"""
# sequence = 'Pamkl'
# res = lambda sequence:sequence[-1]
# print(res(sequence))




# """to check whether a stering is a palindrome or not"""
# sequence = 'kasi'
# pal = lambda s: s == s[::-1]
# print(pal(sequence))


# """wap to check palindrome and print it if it is a palindrome"""
# pal = lambda s: f"the {s} is a palindrome"  if s == s[::-1] else 'not a palindrome'
# print(pal('vrrv'))


# """wap to check whether the no is even or not"""
# ev_odd = lambda num: "even" if num % 2 == 0 else "odd"
# print(ev_odd(1))


"wap to check whether the list of numbers or even or not"
"""using lambda"""
# list_ = [1,2,3,8,45,26,12,87]
# ev = lambda num: num if num % 2 == 0 else None
# res = map(ev, list_)
# print(list(res))

# list_ = [1,2,3,8,45,26,12,87]
# def ev(num):
#     if num % 2 == 0:
#         return num
#
# res = map(ev, list_)
# print(list(res))


# """wap to return stirngs wich are starting with vowel"""
# list_ = ['kasi', 'is', 'guntur','and','ur','name']
# def vow(string_):
#     if string_[0].lower() in 'aeiou':
#         return string_
#
# check = map(vow, list_)
# print(list(check))

# """wap to get list of lenth of each word"""
# string_ = 'hello kasi guntur'
# def lenght_(word):
#     return (word, len(word))
#
# res = map(lenght_, string_.split())
# print(list(res))


# """write a program to get a list of tuples contains character and it's ascii value"""
# s = 'mapfunctions'
# def ch_ascii(char):
#     return (char, ord(char))
#
# res = map(ch_ascii, s)
# print(list(res))
# l = [1,2,2,4]
# def func(item):
#     return item[1] ** item[0]
#
# res = map (func, enumerate(l))
# print(list(res))



# """to add two list simultaneously using map"""
#
# a = [1,2,3,4]
# b = [1,4,6,7]
# def add(item, item1):
#     return item +item1
#
# res = map(add, a, b)
# print(list(res))


# """wap to return even values in the list"""
# list_ = [1,4,2,3,7,6,67,80,757]
# def ev(num):
#     if num % 2 == 0:
#         return num
#
# even = filter(ev, list_)
# print(list(even))

# """wap that return list of strings which are of odd length"""
# list_ = ['kas', 'and','fello','pythons']
# def odd_str(string_):
#     if len(string_) % 2 != 0:
#         return string_
#
# check = filter(odd_str, list_)
# print(list(check))


# """wap that returns all the words which are strating with vowel in a given sentence"""
# sentence = "we have more passionate to learn python and it's applications that is in depth"
# def vowel(word):
#     if word[0].lower() in 'aeiou':
#         return word
#
# check = filter(vowel, sentence.split())
# print(list(check))



"""the variable which is created out side the function we call it as global variable for that global variable we can access it
inside function but we cant modify or change value of that variable inside the function so to modify the global variable inside
a function we have a key word called global by using global key word we can initialize a global variable insede a function or 
we can name it "global variable name" variable which is created outside function and then we can access it and modify that inside
the function"""

a = 'kasi'
# def glob():
#     print(a)
#     a += 'mohana'   # gives yo error
#     print(a)
# glob()

# def glob():
#     print(a)   #"""we cant use that variable before the global variable declarstion """
#     global a    # it will throwas you error the global varible used prior to the global declaration
#     a += 'mohana'
#     print(a)
# glob()

# def glob():
#     global a
#     print(a)
#     a += 'mohana'
#     print(a)
# glob()


"""non local variables are the variables which are created inside the function so you can modify that varibles inside function
only. we cant access those variables ourtside function. if you want access those outside a function again we have to make use
of global key word at local name space or global name space"""

# def local():
#     global string_ = 'kasi'
#
# local()
# print(string_)
#
#
# list_ = [1,2,3,4]
# list2_ = []
# for item in list_:
#     if item % 2 == 0:
#         list2_.append(item)
#
# print(list2):
#
#

# list_ = [1,2,3,4]
# def even(item):
#     if item % 2 == 0:
#         return item
#
# res = map(even, list_)
# print(list(res))





#
#
#
# a = [10,12,14,16,18]
# b = [20,22,24,26,28]
# l = [*a, *b]
# i = 0
# while i <len(l)-1:
#     difference = l[i+1] - l[i]
#     if difference == 2:
#         i += 1
#     else:
#         print("b is not sequence of a")
#         break
# else:
#     print("b is sequence of a")
#


s = 'aaaAAAvvvbb'
i = 0
count = 0
res = ''
while i < len(s):
    if s[i] == s[i+1:i+2]:
        count += 1
        i += 1
    else:
        count += 1
        res += s[i]+str(count)
        count = count-count
        i += 1
print(res)







