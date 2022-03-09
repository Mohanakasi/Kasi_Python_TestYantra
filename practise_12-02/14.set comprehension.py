"set comprehension"
""""""" set comprehension to create a set of squares from 1 to 10"""""""
set_ = {item**2 for item in range(1,11)}
# print(set_)

"""tuple of index and item using enumewrate"""
list_ = ['ksi','jmr',1,2,3]
set_ = {(index,item) for index,item in enumerate(list_)}
# print(set_)

