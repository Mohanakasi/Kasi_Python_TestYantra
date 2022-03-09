"dictionaries"
"it is a collection of key value pairs"
"each element is maped with specific key"
"bounded by {} and seperated by ','"
"it is a mutable data type"
"it doesnt support indexing and slicing"
"but we can fetch the element by using the key as like indexing"
"we can find the length of the dictionary using len function it will count the how many keys present in the dictionary"

"dictionary creation"

dict_ = {'a':20, 'b':10}
"using dict constructor"
d = dict([('a',10), ('b',20)])
# print(d)
d = dict({('c',20), ('d',30)})
# print(d)
d = dict((('c',20), ('d',30)))
# print(d)
# d = dict('kasi'=1008, 'jmr'=50) # while creating keyword arguments no need to provide qoutes to the key raise to the syntex err
# print(d) # it will implicitly takes it as key as string data type
d = dict(kasi=50, jmr=80)
# print(d)

"characterstics of dictionaries"
"key duplication not allowed"
"if key is repeated the value is the value of the key is overided with new value"
"value repetition is allowed"
"key can have composite keys (multiple keys)"
"key must be of immutable data type"
"value can be of any data type"
# d = {[1]: 506} # error key is of type list(mutable data type)
# print(d)
# d = {{1}:5685} # error key is type set(mutable data type)
# print(d)
d = {(1):1007} # tuple is allowed as key because it is of immutable data type
# print(d)
d = {(1,2):1007}
# print(d)
d = {(1,2,3):{1007}}
# print(d)

"to clear the dictionary we use clear()"
d = {(1,2,3):{1007}}
d.clear()
# print(d)

"""del will deallocate the memory created to the dictionary"""
d = {(1,2,3):{1007}}
del d
# print(d) #raise error because the dictionary is removed by del key word



"inbuilt methods"


"get()"
"it will give the value associated with specified key"
"it returns the value of the key and wont modifies the original dictionary"
"if the key is not present in the dictionary it will return none"

d = {'kasi':20, 'jmr':20, 'vrdl':19}
# print(d.get('kasi'))
# print(d.get('robo')) # no error as key is not present if we access by using normal method it will raises error i.e (d[key])
# print(d.get('robo','not found the key'))
# print(d.get('jmr'))
# print(d.get('vrdl'))
# print(d)

"keys()"
"it will give the list of keys of the dictionary"
"it will return the list containing keys"
"it wont modifies the original dictionary"
d = {'kasi':20, 'jmr':20, 'vrdl':19}
# print(d.keys())

"values()"
"it will gives the list of all values present in the dictionary"
"it will return the list containing values present in the dictionary"
"it wont modify the dictionary"
d = {'kasi':20, 'jmr':20, 'vrdl':19}
# print(d.values())

"items()"
"it will give the list containing tuples. each tuple containing key and value"
"it will return a list of tuples containing key and value"
"it wont modify the original dictionary"
d = {'kasi':20, 'jmr':20, 'vrdl':19}
# print(d.items())

"update()"
"it will update existing dictinary with the specified key and values"
"if the dictionary is empty it will add the key and values into the dictionary"
"if the key is already present in the dictionary it will update the  key with the new value"
"it wont return any thing it will modifies the original dictionary"
"i will takes only one argument"
"it will take the input in the form of keyword pairs of multiple pairs"
# d = {'kasi':20, 'jmr':20, 'vrdl':19}
# d.update(king=1008)
# print(d)
# d.update(king=777, queen=4444, guntur=8888)
# print(d)
# d = {}
# d.update(mohanakasi=2020)
# print(d)
# d.update(mohanakasi=2022)
# print(d)
# d.update({'a':44, 'v':807})
# print(d)
# d.update({'a':44},{'v':807}) # raises error because update will take only one argument incase of keyword it will take multiple
# print(d)

"fromkeys()"
"returns a dictionary with the specified key and value"
"from keys() will convert the iterable containig elements into the dictionary by assigning one default value to the all keys"
"it will take iterable and default value as an argument"
"it will return created dictionary"

list_ = ['a', 'b', 'c']
dict_ = dict.fromkeys(list_, 'nothing')
# print(dict_)

list_ = ['kasi', 'jmr']
dict_ = dict.fromkeys(list_,2020)
# print(dict_)

set_ = {'kasi', 'jmr'}
dict_ = dict.fromkeys(set_,2020)
# print(dict_)

tuple_ = ('mohana','rao')
dict_ = dict.fromkeys(tuple_,'none')
# print(dict_)

string_ = 'kasi'
dict_ = dict.fromkeys(string_,'no')
# print(dict_)

"pop()"
"it will remove the specified key and it's value from the dictionary"
"it will take key name and defalut messege as an arguments"
"if the key is not found in the dictionary it will raise key error"
"to avoid that key error if we provide any default messege in pop() it will return that default messege if key is not there"
"it will return the removed value of corres[ponfing key  and it modifies the original dictionary"
dict_ = {'a':20, 'b':800, 'z':2020}
# print(dict_.pop('c')) # key error as key not there in dictionary
# print(dict_.pop('c','notfound')) # returns default messege if key not found in the dictionary
print(dict_.pop('z'))


"popitem()"
"it will removes the last key and value pair in the dictionary"
"it doesnt takes any argument"
"it will returns the tuple of removed key and value"
"if the dictionary is empty it will raises key error as dictionary is emptry"
dict_ = {'kasi':2020, 'jmr':2020, 'meet': 'vrdl lab'}
# print(dict_.popitem('kasi')) # raises error because it doesn't takes any argument
# print(dict_.popitem())
# print(dict_.popitem())
# print(dict_.popitem())
# print(dict_.popitem())
