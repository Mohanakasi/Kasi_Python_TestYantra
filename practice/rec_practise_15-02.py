
# def fibo(n, first = 0, second = 1):
#     if first <= n:
#         if first == n:
#             print(f"the given no {n} is a fibo number")
#         else:
#             sum = first + second
#             first = second
#             second = sum
#             fibo(n, first, second)
#     else:
#         print(f"the {n} is not a fibo number")
# fibo(13)

"write a recursion program that checks the number is a prime or not"
# def prime(n,start=2, flag=True):
#     if start < n:
#         if n % start !=0:
#             falg = True
#             prime(n, start+1, flag)
#         else:
#             flag = False
#             return f"the {n} is not a prime number"
#     else:
#         if flag == True:
#             return f"the {n} is a prime number"
#
# print(prime(10))

"write a recursion function that prints 10 to 50 numbers"
# def num(end, start = 10):
#     if start<= end:
#         print(start, end=' ')
#         num(end, start+1)
#
# num(50)

"write recursion function that prints even nubers in the range 10 to 50 "
# def ev_num(end, start = 0):
#     if start <= end:
#         if start % 2 == 0:
#             print(start, end=' ')
#         ev_num(end, start+1)
#
# ev_num(50,10)

"wa recursion function that take a list of numbers and checks each number in a list even or not if even print it"
def ev_list(list_, start=0):
    if start<len(list_):
        if list_[start] % 2 == 0:
            print(list_[start], end=' ')
        ev_list(list_, start+1)

# ev_list([320,8,754,68,327,77,86])


def add(*numnbers):
    sum = 0
    for item in numnbers:
        sum += item
    return sum
# add(1,2,3)

# my_func = add

# my_func(1,856)

res = add(1,2,3)
# print(res)

# def my_arg(*args, **kwargs):
#     print("--->",args)
#     print(kwargs)
#
# res = my_arg
# res(1,2,3,'kasi',name='mohana',age=25)

# def bokkale(*args,name):
#     for i in args:
#         print(f"hai this is {name}")
#
#
# bokkale(1,2,5,8,5,'kasi') # if we created variable of variable no positional arguments in function defination after that all variable
#must be of key word arguments only

# def bokkale(name, *args):
#     for i in args:
#         print(f"hai this is {name}")
#
#
# bokkale('kasi',1,2,5,8,5)
"if you created varible no of positional arguments(*args) after the positional parameter that was the valid case\n" \
"the you can passs first positinal argument and after that you can pass callection of positinal arguments to pack in function def"
""

data = ['kasi',25,8886213059]
def saave(*info,): # packing in function definition
    name,age,mobile = info # unpacking in function body
    print(name)
    print(age)
    print(mobile)
    print(f"my name is {name}, and iam {age}, my mobile num is {mobile}")
# saave(*data) #unpacking in function call

data = {'name': 'kasi', 'age': 25, 'mobile':8886213059}
def saave(*info): # packing in function definition (here keys only packed in the form of tuple)
    print(info) # when dict is un packed only keys were un packed (when we pack it again only keys only packed)
    name,age,mobile = info # unpacking in function body (again keys only unpacked)
    #when we unpack it we get only keys, to get the data we have to call key based main dictionary  (data)
    print(data[name])
    print(data[age])
    print(data[mobile])
    # print(f"my name is {name}, and iam {age}, my mobile num is {mobile}")
# saave(*data) # here keys only unpacked

def func_ano(age:int,name:str):
    print(age, name)


# func_ano(25,86)

# def func_ano(age:int,name:str):
#     print(age, name)
#
#
# func_ano(age = 25, name = 'kasi')

# def new_ano(a,b):
#     new_ano.count += 1
#     print(count)
# new_ano.count = 10


# def add(a,b):
#     return a+b
#
# list_ = [1,23,3,add(1,2)]
# print(list_)
#
# d = {'a':add(1,2)}
# print(d)
# print(add(10,80))
#
# def sum2(a,b):
#     return a+b+add(10,20)
#
# print(sum2(80,90))



"to check a number is prime or not using ecursion"
# def prime_check(num, i = 2):
#     if i < num:
#         if num % i != 0:
#              return prime_check(num, i+1)
#         else:
#             return f"the {num} is not a prime number"
#     else:
#         return f"the {num} is a prime number"
#
# print(prime_check(7))

"to check whether the number is a fibo number or not"
# def fibo_check(num, first=0, second=1):
#     if first <= num:
#         if first == num:
#             return f"the {num} is a fibo number"
#         else:
#             sum = first + second
#             first = second
#             second = sum
#             return fibo_check(num, first, second)
#     else:
#         return f"the {num} is not a fibo number"
# print(fibo_check(12))


"write a recursion program 10 to 1"
def temp(num):
    if num > 0:
        print(num)
        return temp(num-1)

# temp(10)

# "write a recursion program to add the digits of a number"
# def add(num, i=0, sum=0):
#     string_ = str(num)
#     if string_[i:i+1]:
#         sum += int(string_[i])
#         return add(num, i+1, sum)
#     else:
#         return sum
#
# print(add(156))

"write a recursion program to reverse a stirng"
# def rev_kasi(string_, i=0, res=''):
#     if string_[i:i+1]:
#         res = string_[i] + res
#         return rev_kasi(string_, i+1, res)
#     else:
#         return res
#
# print(rev_kasi('mohana'))

"wa recursion program to find the factorial of a number"
# def facto_num(num, res=1):
#     if num>0:
#         res *= num
#         return facto_num(num-1, res)
#     else:
#         return res
#
# print(facto_num(5))

"to find the sum of first n numbers"
def sum_n_num(n, sum=0):
    if n > 0:
        sum += n
        return sum_n_num(n-1, sum)
    else:
        return sum

# print(sum_n_num(5))

"to print fibo series up to n number"
def fibo_ser_n(n, first=0, second=1, i=0):
    if i <= n:
        print(first, end=' ')
        sum = first + second
        first = second
        second = sum
        return fibo_ser_n(n, first, second, i+1)

fibo_ser_n(10)
