"type casting"
# a = 1233
# print(float(a))
# print(complex(a))
# print(bool(a))
# print(str(a))

float_ = 805.98
# print(int(float_))  #"to romoove decimal value in a number we have to use int type conversion or trunc"
# print(complex(float_))
# print(bool(float_))
# print(str(float_))
# print(list(float_))

"complex"
# com_ = 50+50j
# print(bool(str(com_)))
# print(str(com_))
# print(bool(com_)) # in complex we can perform tpe conversion only to boolean

"boolean"
# bool_ = True
# print(int(bool_))
# print(float(bool_))
# print(complex(bool_))
# print(str(bool_))
"string"
# string_ = 'hello'
# print(bool(string_))
"""if we want to convert the string into int or complex or float it must be a string of numeric only"""
# s = '50+50j'
# print(complex(s))
# s = '1286'
# print(int(s))
# print(float(s))

# string_ = 'hello'
# print(list(string_))
# print(tuple(string_))
# print(set(string_))

"""list"""
list_ = [1,2,3,4,6,8]
# print(str(list_))
# print(tuple(list_))
# print(set(list_))
# "dictionary"
# list_ = [(1,2)]
# print(dict(list_))
"""when the list containing tuples of two elemets ech then it will be converted to dictionary """
# list_ = [('a',458),('b',4)]
# print(dict(list_))

"""tupple"""
# tuple_ = (1,2,3,'kasi')
# print(str(tuple_))
# print(list(tuple_))
# print(set(tuple_))
"""when the tuple contains any one of  list, set,data type it cant be converted to set"""
# tuple_ = (1,2,3,'kasi',[1,2,3],{1,4,5}, {'a':1})
# # print(set(tuple_)) # error
"""when the tuple consists of tuples of two elements each then it will be converted to dictionary"""
# tuple_ = ((1,2),(3,4))
# print(dict(tuple_))

"set"
# set_ = {1,2,3,4,'str'}
# print(str(set_))
# print(list(set_))
# print(tuple(set_))
# "when the set contains tuple of two elements each it will be converted to dictionary"
# set_ = {(1,2),(3,4)}
# print(dict(set_))

"dictionary"
dict_ = {'kasi':1008, 'jmr': 2020}
print(str(dict_))
"""when the dictionary is converted to list,tuple,set only keys will be available in particular data type"""
print(list(dict_))
print(tuple(dict_))
print(set(dict_))





