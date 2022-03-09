# """"traverse through using recursion"""
# string_ = 'kasi'
# def rec_str(si):
#     if string_[si: si+1]:
#         print(string_[si], end = ' ')
#         rec_str(si+1)
#
# rec_str(0)
# print()

# "traverse through list using recursion"
# list_ = [1,'kasi',1007]
# def list_rec(si):
#     if list_[si: si+1]:
#         print(list_[si])
#         list_rec(si+1)
#
# list_rec(0)

"to print the even numbers for a particular range using recursion"
# def range(end, start = 0):
#     if start <= end:
#         if start % 2 == 0:
#             print(start)
#         range(end, start+1)
#
# range(20)


"recursion program to check series of prime numbrers"
# def primr(end,start = 2):
#     if start <= end:
#         for i in range(2,start):
#             if start % i == 0:
#                 break
#                 print("check")
#         else:
#             print(start)
#         primr(end, start+1)
#
# primr(20)

"to print 10 numbers"
# def numbers(n):
#     if n <= 10:
#         print(n)
#         #n += 1
#         numbers(n+1)
#
# numbers(1)

"""to print 10 to 1 numbers"""
# def numbers(start):
#     if start > 0:
#         print(start)
#         numbers(start-1)
#
# numbers(10)


# """to sum the digits in a number"""
# sum = 0
# def add(num):
#     global sum
#     if num:
#         sum += num%10
#         num //= 10
#         add(num)
#     return sum
# print(add(2586))

# sum = 0
# def add(num):
#     global sum
#     if num > 0:
#         sum += num%10
#         num //= 10
#         add(num)
#     return sum
# print(add(2586))

# sum = 0
# def add(num):
#     global sum
#     if num > 0:
#         last = num % 10
#         sum += last
#         num //= 10
#         add(num)
#     return sum
# print(add(1008))

"""find the sum of first n numbers"""
# sum = 0
# def add(n,start = 0):
#     global sum
#     if start <= n:
#         sum += start
#         add(n,start+1)
#     return sum
#
# print(add(20))

"""wap to reverse a string"""  "usning indexing"
# string_ = 'kasi'
# res = ''
# def rev_rec_str(si):
#     global res
#     if string_[si:si+1]:
#         res = string_[si] + res
#         rev_rec_str(si+1)
#
#     return res
#
# print(rev_rec_str(0))


"""to print a dictionary of word and it's count pair using dictionary"""
# string_= "kasi king kasi is a kasi language of python kasi language"
# dict_ = {}
# def count(words, si= 0, ei= 1):
#     if words[si: ei]:
#         dict_[words[si]] = words.count(words[si])
#         count(words, si+1, ei+1)
#     return dict_
# print(count(string_.split()))



