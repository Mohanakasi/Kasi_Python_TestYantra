string_ = 'python is language'
# list_ = string_.split()
# print(sorted(string_.split(), key=len, reverse=True))

# list_ = [1,2,3,10,0,90,4560,45]
# print(sorted(list_))
# print(sorted(list_, reverse=True))


# string_ = 'hello world python programming'
# res = sorted(string_.split(), key=len)
# # print(res[0])
# # print(res[-1])
#
# print(res[0], len(res[0]))
# print(res[-1], len(res[-1]))


# list_ = ['python','java','c', 'string']
# res = sorted(list_, key = lambda item: item[0])
# print(res)


# d = {'a': 100, 'D': 1, 'C': 1008}
# res = sorted(d.items())
# print(res)

# "sort the list elements based on their length"
# list_ = ['kasi', 'was', 'king', 'once', 'upon','a','time']
# res = sorted(list_, key = lambda item:item[-1])
# print(res)

# string_ = 'kasi is a king once upon a time'
# res = sorted(string_.split())
# print(res[0],res[-1])

# string_ = 'asi is a aking once upon a time'
# res = sorted(string_.split(), key = lambda item:item[0])
# print(res[0],res[-1])

"""to print most repeated word in a string"""
# string_ = "kasi is a king kasi is of python testing kasi language"
# words = string_.split()
# d = {word:words.count(word) for word in words}
# res = sorted(d.items(), key=lambda item:item[-1])
# print(res[-1][0])

# """wap to print the longest word and with it's length"""
# string_ = "kasi is a king kasi is of python testing kasi language"
# words = string_.split()
# d ={word:len(word) for word in words}
# res = sorted(d.items(), key = lambda item:item[-1])
# print(res)
# print(res[-1]) # most common word

"""longest non repeated word"""
# string_ = "kasi is a chromatic king kasi is of python testing kasi language"
# words = string_.split()
# d = {word:words.count(word) for word in words if words.count(word) == 1}
# res = sorted(d, key = len)
# print(res[-1])

l = [{'name': 'ram', 'class': 6, 'age': 12},
     {'name': 'kasi', 'class': 10, 'age': 25},
     {'name': 'raju', 'class':12, 'age': 30}]
"sort the above item based on the list"
# res = sorted(l, key =lambda item:item['name'])
# print(res)
# res = sorted(l, key =lambda item:item['age'])
# print(res[-0])
print(add(10,50))