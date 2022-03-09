"tuple"
"collection of homogeneous and heterogeneous items"
"bounded by () and separated by ',' "
"these are immutable data type"
"it is a sequence data type indexing and slicing is possible like string and list"
"we can find total elements present inside the tuple by using len"


"tuple creation"
# tuple_ = (1, 2.5, True, 50+50j, 'kasi', [1008, 'rao'], ('jmr',2020), {1,2,3}, {'a': 20})
# print(tuple_)
# tuple_ = tuple((1, 2.5, True, 50+50j, 'kasi', [1008, 'rao'], ('jmr',2020), {1,2,3}, {'a': 20}))
# print(tuple_)

"inbuilt methods in tuple"
"count"
"it will count the no of occurrences of the given element in the tuple "
"if the given element is not found it will return 0"
"it will returns count as integer"
# tuple_ = (1,2,50,89,1,36,'kasi',63,456,63,'kasi')
# print(tuple_.count('kasi'))
# print(tuple_.count('mohana')) # if element is not found it will return 0
# print(tuple_.count(1))
# print(tuple_.count(63))
# print(tuple_.count(89))

"index"
"it will give the index no of the first occurrence of the given element"
"if element is not found it will raise the value error"
"return index no as integer"
tuple_ = (1,2,50,89,1,36,'kasi',63,456,63,'kasi')
print(tuple_.index(63))
print(tuple_.index(1))
print(tuple_.index('kasi'))
# print(tuple_.index('rao')) # value error

