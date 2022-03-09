"dictionary comprehension"

""" WAP to create a dictionary with item and its index pair"""
list_ = ['kasi','mohana','jmr']
res = {item:index for index,item in enumerate(list_)}
# print(res)
res = {list_[index]:index for index in range(len(list_))}
# print(res)

""" WAP to create a dictionary with word and its length pair"""
string_ = 'kasi nadh'
res = {word:len(word) for word in string_.split()}
# print(res)

"""word and it's count pair"""
s = 'kasi nadh is a king of kasi palace'
words = s.split()
res = {word:words.count(word) for word in words}
# print(res)

"""printing dictionaryu with word and its count pair only if word is of even length"""
s = 'kasi nadh is a king of kasi palace'
words = s.split()
res = {word:words.count(word) for word in words if len(word) % 2 == 0}
# print(res)


""" take key as index and words as values if the word in a string is of odd lenth reverse it else keep as iti is"""
s = 'kasi nadh is a king of kasi palace bangalore and mumbai'
res = {index:word if len(word) % 2 == 0 else word[::-1] for index,word in enumerate(s.split())}
# print(res)

"""(creating a dictionary with word and it's length psir if word is starting with vowel)"""
s = 'kasi nadh is a king of kasi palace'
res = {word:len(word) for word in s.split() if word[0].lower() in 'aeiou'}
# print(res)

"""swaping keys and values"""
d  = {'a':1,"b":2,'c':30}
res = {value:key for key,value in d.items()}
# print(res)

res = {d[key]: key for key in d}
# print(res)

""" char and ascii value pair """
string = "python"
res ={char:ord(char) for char in string_}
print(res)
