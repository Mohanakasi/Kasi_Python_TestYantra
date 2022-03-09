"lists"
"list are collection of homogenious & heterogenious data types"
"bounded by [] and each element seperated by ','"
"represented by list and default value is []"
"in list data type indexing and slicing is possible"

"list creation"
var = list('hello')
# print(var)
var = [1,2,3,'hai']
# print(var)
var = list()
# print(var)


"merging two lists"
list1 = [1,2,3,'kasi',[1,2,3]]
list2 = ['hello',1008,'how']
# print([*list1,*list2]) #unpacking two list into one list or merging two lists

"unpacking  list"
list1 = [1,2,3,'kasi',[1,2,3]]
# print(*list1) # unpacking list
list_ = ['kasi',1]
string_,num = list_ # packing or unpacking variables must be at left side only
# print(string_,num)
"packing"
l = string_,num
# print(l)

"inbuilt methods"
"append"
"it will appen the given element at the last of the list"
"it accepts all data types"
"it returns nothing"
list_ = [7,58]
# list_.append([1,2],[3.4]) # append accept only one argument
# list_.append(1)
# list_.append('kasi')
# list_.append('jmr')
# list_.append(1.585)
# list_.append(50+50j) # when we appending the complex number into the list it will appended as tuple
# list_.append(True)
# list_.append([1008,[10]])
# list_.append(('hello','python',3.10))
# list_.append({'bangalore',560068})
# list_.append({'a':10, 'b':20, 'c':30})
# print(list_)

"extend"
"extends existing list with the elements of given sequence"
list2_ = ['mohana','kasi']
# list2_.extend('rao')
# print(list2_)
# list2_.extend([['jmr'],2020,['kasi']])
# print(list2_)
"""if the tuple of tuple containig sile element the extend will consider it as single element and insert it as 
individual element"""
# list2_.extend((('hai'),('hello')))
# print(list2_)
# list2_.extend((('hai',777),('jmr',9999)))
# print(list2_)
# list2_.extend(('hai',1),('bye',2),('c',30)) # extend will accept only one collection as an argument
# print(list2_)
# list2_.extend({456,555})
# print(list2_)
# list2_.extend({'a':10}) # when we extend dictionary into list it will inser only keys into the list
# print(list2_)

"insert"
"inserts the element at the specified position"
"it will accept the both individual and collection data types"
"position and element are the arguments of insert"
"it will returns nothing and modifies the original list"
list_ = []
# list_.insert(4,'kasi') # if the positin was not there it will insert element at 0 index
# list_ = [1,'jaya madhuri','kasi']
# print(list_)
# list_.insert(20,1.58)
# print(list_)
# list_.insert(len(list_)-1,'robo')
# print(list_)
# # list_.insert('mohan') # both the position and element are mandatory arguments
# list_.insert(1,{1008})
# print(list_)
# list_.insert(0,{'a':200})
# print(list_)
# list_.insert(3,('king')) # if tuple containg single element only element inserted into the list
# print(list_)
# list_.insert(4,(1,99999))
# print(list_)
# list_.insert(30,{'a':20})
# print(list_)

"""pop()"""
"pop will removes the element from the specified position"
"position is the optional argument for pop"
"if position was not given then it will removes the last element"
"if the given position is out of index then it will gives you index error"
"it will returns removed elemet and modifies the original list"
# list_ = [{'a': 200}, 1, {1008}, 'king', (1, 99999), 'jaya madhuri', 'kasi', 'robo', 1.58, {'a': 20}]
# print(list_.pop())
# print(list_.pop(3))
# print(list_.pop(0))
# print(list_.pop(50)) # index error

"remove()"
"removes the first occurance of the specified element"
"element is the argument"
"if element is not found it will raise value error"
"it will returns nothing and modifies the original string"
# list_ = [{'a': 200}, 1, {1008}, 'king', (1, 99999), 'jaya madhuri', 'kasi', 'robo', 1.58, {'a': 20}]
# print(list_.remove({1008})) # returns nothing
# print(list_)
# # list_.remove('mohana') #value error
# list_ = [1,2,3,7,8,9,1,50,4,3,6,4,5,6,8,4]
# list_.remove(1) # removes first occurance only
# print(list_)


"sort()"
"sort the list"
"in order to sort list must contains homegeneous elements"
"key and reverse are the optional arguments"
"returns none modifies the original list"
list_ = ['kasi','king','abudabi','mohana']
# list_.sort()
# print(list_)
# list_.sort(key = len)
# print(list_)
# list_.sort(reverse=True)
# print(list_)
# list_.sort(key=len, reverse=True)
# print(list_)
# list_.sort(key=lambda item:item[-1])
# print(list_)
# list_.sort(key=lambda item:item[2])
# print(list_)
# list_.sort(key=lambda item:item[2], reverse=True)
# print(list_)

"index"
"it will give index of the specified element"
"if the value is not found it will raise vlaue error"
"it will return the index of the first occurance of the elemet"
# list_ = [10,21,1,3,5,1]
# print(list_.index(1))
# print(list_.index(10))


# "count"
# "it will return the no of occurances of a particular element"
# "if the element is not found inthe list it will gives you 0"
# "element is the mandatory argument"
# "it will return count as integer "
# l = ['kasi',10078,'mohana','kasi',1,45,36,4,1,69,96,1,96,69]
# print(l.count(1007))
# print(l.count(69))
# print(l.count('kasi'))
# print(l.count(1))
