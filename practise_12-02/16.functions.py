"functions"
"write a function to create a dictionary of word and it's count pair in the following sentence"
from collections import defaultdict
sentence = 'it is a very good book and reading book is good habit'
d = defaultdict(int)
def word_count(sequence):
    global d
    words = sentence.split()
    for word in words:
        d[word] += 1
    return d

# print(word_count(sentence))


"write a function to count the no of elements present in the list without using the inbuilt function"
# a = ['hai','guys','welcome','to']
def count_(list_):
    count = 0
    for item in list_:
        count += 1
    return count

# print(count_(a))

"write a function to return the words starting with vowels"
b = 'please like shar and subscribe is from '
def vow_words(string_):
    list_ = []
    for word in string_.split():
        if word[0].lower() in 'aeiou':
            list_.append(word)
    return list_

# print(vow_words(b))

"write a function to check if the given no is prime or not"
num = 12
def prime_check(number):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                return f"{number} is not a prime"
        else:
            return f"{number} is a prime"
    else:
        return "please enter the number greater then 1"

# print(prime_check(num))

"write a function to return nth fibonaci number"
n = 10
def fibo(n):
    first = 0
    second = 1
    i = 1
    while i <= n:
        if i == n:
            print(first)
            break
        sum = first + second
        first = second
        second = sum
        i += 1
# fibo(10)

"write a function to reverse a stirng without using inbuilt function"
s = "please like share and subscribe"
def rev_string(string_):
    res = ''
    for char in string_:
        res = char+res
    return res

# print(rev_string(s))

"write a function to return the prime number present after the given number(if the given no is prime return the same)"
number = 12
def prime_check(num):
    while num > 0:
        for i in range(2,num):
            if num % i ==0:
                num += 1
                break
        else:
            return f"{num} is a prime number"

# print(prime_check(number))

"write a function to return the string by converting upper case to lower case and vice versa without using inbuilt method"
s = 'dont foRGet to Press Bell ICON'

def swap_case(string_):
    res = ''
    for char in string_:
        if 'a'<= char <= 'z':
            res += chr(ord(char)-32)
        elif 'A'<= char <= 'z':
            res += chr(ord(char)+32)
        else:
            res += char
    return res

# print(swap_case(s))

"""write a function that takes a string as input and returns the first, last  and middle two characters as the output"""
s = 'to get all the notifications about upcoming videos'
def sam(string_):
    for i in range(len(string_)):
        if i == 0 or i == len(string_) - 1:
            print(string_[i], end=' ')
        elif i == len(string_) // 2:
            print(string_[i: i+2], end=' ')

# sam(s)


"to print first 10 fibonaci numbers"
def fibo(range):
    first = 0
    second = 1
    i = 1
    while i <= range:
        print(first, end= ' ')
        sum = first + second
        first = second
        second = sum
        i += 1

# fibo(10)

"to check whether the given number is fibonsci number or not"
def fibo(num):
    first = 0
    second = 1
    while first <= num:
        if first == num:
            return f"{num} is a fibonaci numnber"
        sum = first + second
        first = second
        second = sum
    else:
        return f"{num} is not a fibonaci numner"

# print(fibo(34))


"wreite a function thst takes integers and float as data type as arguments and returns it sum"
def temp(*args):
    sum = 0
    for item in args:
        sum += item
    return sum

# print(temp(10,15,1.5))

"""printing integers only when variable positonal argms passed"""
def int_pr(*args):
    for item in args:
        if isinstance(item,int):
            print(item)
#
# int_pr(1,2,3,'kasi')


"to print a series of numbers using recursion"
def s_num(end,start=0):
    if start <= end:
        print(start,end = ' ')
        s_num(end,start+1)
#
# s_num(50)

"to print 10 to 1 using recursion"
def num(start):
    if start > 0:
        print(start, end = ' ')
        num(start-1)

# num(10)

"write a lambda function that checks if the given no is even or not"
res = lambda num: num % 2 == 0
# print(res(2))

"wtite a lambda function that returns the last element of the sequence"
res = lambda sequence:sequence[-1]
# print(res('kasi'))

"write a lamda function that checks if the given string is a palindrome or not"
res = lambda string_: string_ == string_[::-1]
# print(res('mom'))

"write a program that checks if the given list of numbers are of even or not"
res = lambda num: num %2 == 0
ev_check = map(res, [1,2,3,4])
# print(list(ev_check))

"wap to return strings which are starting with vowels"
list_ = ['kasi','is','a','king','orange']
def func(string_):
    if string_[0].lower() in 'aeiou':
        return string_

res = map(func, list_)
# print(list(res))

"wap to get length of the each word"
s = 'hello world hello kasi hello python'
def len_word(word):
    return word,len(word)

res = map(len_word, s.split())
# print(list(res))

"wap to get a list tuples continig character and it's ascii values"
s = 'hello kasi'
def func(char):
    return char,ord(char)


res = map(func, s)
print(list(res))

"wap to return even values in the below list"
list_ = [2,4,8,7,6,9,1]
def ev_check(num):
    if num % 2 == 0:
        return num

res = filter(ev_check, list_)
print(list(res))

"wap to returns all the words that are starting with vowels in a given sentence"
sentence = 'hai is it ok to introduce my id'
def vow(word):
    if word[0].lower() in 'aeiou':
        return word

res = filter(vow, sentence.split())
print(list(res))












































