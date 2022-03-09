# def in_(func):
#     def c(*args, **kwargs):
#         print("some c1")
#         func(*args, **kwargs)
#         print("some c1_1")
#     return c
#
# def inn_(func):
#     def c(*args, **kwargs):
#         print("more_c2")
#         func(*args, **kwargs)
#         print("more")
#     return c
#
# @in_
# @inn_
# def call(b):
#     print(b)
# call('hi')
#

# def temp(func):
#     print('hi')
#
#
# def temp2():
#     @temp
#     def c():
#         print("hi2")
# # temp2()

# path = r"C:\Users\Hp\PycharmProjects\python_training\my_files\csv_files\mohana.csv"
# import csv
# with open(path, 'w') as csv_file:
#     write_obj = csv.writer(csv_file)
#     write_obj.writerow(['a','b','c'])
#     write_obj.writerows([(1,2,3),(3,4,5)])


# import json
# dict1 = {'x':10, 'y':20}
# b = json.dumps(dict1)
# print(type(b))
# print(type(json.loads(b)))

# s = "Kalyan is good"
# for index in range(len(s)):
#     print(s[index])

# l = (3, 34, 35)
# for i in l:
#     print(i)
#
# s = 'Kalyan is king'
# a = s.split()
# print(a)
# for i in a:
#     print(i)
#
# set_ = [3, 435, 45, 34]
# for index, item in enumerate(set_):
#     # print(index, end=', ')
#     if index % 2 != 0:
#         print(item)

#
# l = ["Kalyan", "Kasi", "Sree"]
# for i in l:
    # if len(i) % 2 == 0:
    #     print(i)
    # else:
    #     print(i[::-1])
#
#
s = "Kasi is  345 wert 456 @#$%^& great"
# count = 0
# for i in s:
#     count += 1
# print(count)
# print(len(s))
# for i in s:
    # if "0" <= i <= "9":
    #     print(i)
    # if "a" <= i <= "z" or "A" <= i <= "Z":
    #     print(i, end=' ')
# for i in s:
#     if i.isalpha():
#         print(i)
#
# for i in s:
#     if i.isdigit():
#         print(i)
# l = ["Kasi", "kalyan"]
# for i in l:
#     print(i, len(i))
#
# l = ['iam', 'kasi', 'userid']
# for i in l:
#     if i[0] in "aeiouAEIOU":
#         print(i)

# l = [10,20,30,40,50,60,70,80,10,50]
# for i in l:
#     if i == 20:
#         print(i)
#         break

# "print elements other than 20"
# for i in l:
#     if i == 20:
#         continue
#     else:
#         print(i)
# d = {'a':10, 'b':20, 'c':30}
# for keys in d:
#     print(keys)
#
# for keys in d:
#     print(d[keys])
#
# for keys, values in d.items():
#     print(keys, values)
# for index, items in enumerate(d):
#     print(index, items)


# num = 100
# for i in range(2, num):
#     if num % i == 0:
#         print("NOt a prime")
#         break
# else:
#     print("Prime")












"print prime numbers between 100 to 300"
for num in range(10, 20):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(f"{num} is prime")





        