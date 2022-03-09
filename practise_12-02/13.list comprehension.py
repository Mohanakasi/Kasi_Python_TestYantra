''"""print list having powers of each element of another list"""''
list_ = [1,2,3,4,9]
res = [item**2 for item in list_]
# print(res)

"""to print a list having tuple of index and item of another list"""
list_ = [1,23,'kasi']
res = [(index,item) for index, item in enumerate(list_)]
# print

"""creating list of even no's for particular range using list comprehension"""
res = [item for item in range(20) if item % 2 == 0]
# print(res)

"""creating lists of odd using list comprehension"""
res = [item for item in range(20) if item % 2 != 0]
# print(res)

"""if word is of even length append into list as it is if word is of odd length then reverser it """
list_ = ['kasi','is','from','bangalore']
res = [item if len(item) % 2 == 0 else item[::-1] for item in list_]
# print(res)

"""if item in a list is string keep it as it is else reverse that item"""
list_ = ['kais',1.0,True,[1,4,56]]
res = [item if isinstance(item, str) else str(item)[::-1] for item in list_]
# print(res)

"""create a list having words starting with owel (using list comprehension)"""
list_ = ['kasi', 'User', 'Imr','iam']
res = [word for word in list_ if word[0].lower() in 'aeiou']
# print(res)

"""wap to reverse the elements in the list using list comprehension"""
list_ = ['kasi','python',1008,'happy']

res = [item for item in reversed(list_)]
# print(res)

"without using inbuilt method"
res = [item for item in list_[::-1]]
# print(res)

"""wap to preint alternate elements (even)"""
list_ = ['python',1.58,True,'kasi','laguage0']
res = [item for item in list_[::2]]
# print(res)

"""wap to print only integers in a list"""
list_ = ['kasi', 2021 , 'python' , 1008, 50200037008003 , 'test yanthra', 2022]
res = [item for item in list_ if isinstance(item, int)]
# print(res)

"""wap to print iterable with it's length"""
list_ = ['kasi','python', [1,2,3,'kasi'],{458,25,'a'},{'a':1,'b':1},('py','by'),True,1.8,10087]
st_l = [(item,len(item)) for item in list_ if isinstance(item, (str,tuple,set,list,dict))]
# print(st_l)

"""wap to print strings in list which are of even length"""
list_ = ['mohan','kasi','is','a','king','before','guntur','minister']
res = [item for item in list_ if len(item) % 2 == 0]
# print(res)

"""wap to print strings in the list if the string is of even lenth keepit as it is if it is odd lenth reverse it"""
list_ = ['kasi','python', 'has','00a','inbuilt','modules','and','oops']
res = [item if len(item) % 2 == 0 else item[::-1] for item in list_]
# print(res)

"""wap to reverse the element if it is of type string elser keep it as it is"""
list_ = ['kasi',True,1008,False,2021,'python','jmr',[1,4,0,80]]
res = [item[::-1] if isinstance(item, str) else item for item in list_]
# print(res)

"""wap to print all the palindrome in a list"""
list_ = ['mom','is','better','then','malayalam','dad']
res = [item for item in list_ if item == item[::-1]]
# print(res)
