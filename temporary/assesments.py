
# a = [10,12,14,16,18]
# b =[20,22,24,26,28]
# if b[0] - a[-1] == 2:
#     temp = b[0]
#     for item in b[1::]:
#         if item - temp == 2:
#             temp = item
#         else:
#             print(f"{b} is not have continuous sequence of {a}")
#             break
#     else:
#         print(f"{b} is a continous sequence with {a}")
# else:
#     print(f"{b} doesnt start with contnuity of {a}")



# # write a comprehension to filter all languages which start's with p
# languages = ['python','java','peri','PHP','Python','JS','C++','Python']
# res = [item for item in languages if item[0].lower() == 'p']
# print(res)

# # write a comprehension to filter all out those names which are less than 6 characters
# names = ['apple','google','gmail','yahoo','flipkart','instagram']
# res = [item for item in names if len(item) < 6]
# print(res)

# # write a list comprehension to reverse the item of a list if the  item is of odd length string otherwise
# # keep them as it is
# names = ['apple','google','yahoo','facebook','yield','flipkart']
# res = [item[::-1] if len(item) % 2 !=0 else item for item in names]
# print(res)

# # write a comprehension to raise the elements in the list to the power of their index
# a = [1,2,3,4,5]
# res = [item ** index for index,item in enumerate(a)]
# print(res)
#
#
# # build a list of tuples with string and it;s length pair using list comprehension
# names = ['apple','google','yahoo','facebook','yelp','flipkart']
# res = [(item,len(item)) for item in names]
# print(res)

# # write a program to print all numeric values in a list using list comprehension
# items = ['apple', 1.2, 'google', '12.60', 26, 50+50j, '100']
# var = [item for item in items if isinstance(item, (int, float, complex))]
# print(var)

"""rotating elements in a list"""
# items = ['apple', 1.2, 'google', 12.6, 26, '100']
# k = 2
# for i in range(k):
#     item = items.pop()
#     items.insert(0,item)
# print(items)


# items = ['lotus-flower','lilly-flower','cat-animal','dog-animal','jasmin-flower','lion-animal']
# from collections import defaultdict
# dd = defaultdict(list)
# for item in items:
#     type = item.split('-')
#     if type[1] == 'flower' or type[1] == 'animal':
#         dd[type[1]] += [type[0]]
# print(dd)



"""wap to convert all the strings in the list to upper case using map"""

list_ = ['Kasi nadh', 'Mohana Kasi', 'Jmr','robo19950','KASIgmc']

"""normal method"""
# def st_conv(string_):
#     temp = ''
#     for char in string_:
#         if char.islower():
#             temp += char.upper()
#         else:
#             temp += char
#     return temp
#
# res = map(st_conv, list_)
# print(list(res))




"""wap to convert all the strings in the list to upper case using map"""
"""only using inbuilt method"""
# list_ = ['Kasi nadh', 'Mohana Kasi', 'Jmr','robo19950','KASIgmc']
# def st_conv(string_):
#
#     return string_.upper()
#
# res = map(st_conv, list_)
# print(list(res))









"""wap to convert allthe negeative numbers into positive using map"""

# list_ = ['kasi','jmr',-18,-25,320,'python',89,50+50j,-48,-320,-8,-6,'mohana kasi']
# def n_p_conv(item):
#     if isinstance(item, int) and item < 0:
#         return abs(item)
#
# res = map(n_p_conv, list_)
# print(list(res))
#
# """using filter """
# res = filter(n_p_conv, list_)
# print(list(res))


"""wap that returns the list of numbers raised to the power of their indices using map"""
# list_ = [42,3,54,8,2,9,12]
# def power(item):
#     index, num = item
#     return num ** index
#
#
#
# res = map(power, enumerate(list_))
# print(list(res))


"""wap that returns all the words in lower case in the given sentence"""
string_ = 'KASI is in BANGALORE and he is Learning python'
def low_case(item):
    if item.islower():
        return item

res = filter(low_case, string_.split())
print(list(res))


# """""""""""""""""""sorted class"""""

# """wap to print longest word and it's length pair"""""
# sentence = 'hai hello python progeramming'
# d = {word: len(word) for word in sentence.split()}
# res = sorted(d.items(), key = lambda item: item[-1])
# print(res[-1])


"""wap to print loagest non repeated word"""

# sentence = 'hai hello hai python kasi python kasi is kinger'
# l = sentence.split()
# d = {word: len(word) for word in l if l.count(word) == 1}
# res = sorted(d.items(), key = lambda item: item[-1])
# print(res[-1])


# l = [{'name': 'a','class': 10, 'age': 26},
#      {'name': 'b','class': 10, 'age': 27},
#      {'name': 'c','class': 10, 'age': 25}]
# res = sorted(l, key = lambda item: item['name'])
# print(res)

def temp(item):
    return item


res = filter(temp, [1,2,3])
print(list(res))















