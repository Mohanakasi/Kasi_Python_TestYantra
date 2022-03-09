"set"
"set is underscored and un-ordered"
"it is a mutable data type and elements inside the set are hashable"
"it will accept only immutable data type for set creation"
"elements inside the set are unique"
"bounded by {} and separated by ','"
"default value is set()"


"set creation"
"it will accept only immutable data type while set creation"
# set_ = {1,2,3,{1,2},447} # type error becuse set is also mutable data type
# set_ = {1,2,[1,2,3],{'a':50}} # type error even list and dictionary also mutable data type
# set_ = {1,2,'kasi',('jmr')}
# print(set_)
# "using set constructor"
# set_ = set('kasi')
# print(set_)
# set_ = set(('kasi'))
# print(set_)
# set_ = set(('kasi',1008))
# print(set_)
# set_ = set({'kasi','jmr'})
# print(set_)
# set_ = set(['kasi','mohana'])
# print(set_)

"inbuilt methods"

"union()"
"it will return a set containing all elements from the two sets"
"we have to take two sets"
"it wont modifies the any one of the set"
"it will return new set"

# set1_ = {1,2,3,8,100,'kasi'}
# set2_ = {456,'kasi',1008,2,3,}
# print(set1_.union(set2_))
# set1_ = {100,108,'mohana',456,(1,2,3)}
# set2_ = {108,(1,2,3),456}
# print(set1_.union(set2_))
# set1_ = {100,108,'mohana',456,(1,2,3)}
# set2_ = {108,(1,2,3,4),456}
# print(set1_.union(set2_))

# set1_ = {1,2,3,8,100,'kasi'}
# set2_ = {456,'kasi',1008,2,3,}
# set3_ = {488,253,662}
# print(set1_.union(set2_,set3_))


"update()"
"it will update the base set with all elements from the both the sets"
"it will returns nothing"
"it will modifies the original set"
# set1_ = {1,2,3,8,100,'kasi'}
# set2_ = {456,'kasi',1008,2,3,}
# set1_.update(set2_)
# print(set1_)
# set2_.update(set1_)
# print(set2_)


"intersection()"
"it will return common elements present in the both the sets"
"it will return new set, it wont modify the base set"
# set1_ = {1,2,3,8,100,'kasi'}
# set2_ = {456,'kasi',1008,2,3,}
# print(set1_.intersection(set2_))
# print(set2_.intersection(set1_))
# print(set1_)
# print(set2_)

"intersection_update()"
"it will modify the base set with common elements present inside the both the sets"
"it returns nothing and modifies the base set"
# set1_ = {1,2,3,8,100,'kasi'}
# set2_ = {456,'kasi',1008,2,3,}
# set1_.intersection_update(set2_)
# print(set1_) # only base set is modified
# print(set2_)
# set1_ = {456,256,'kasi',1008,208}
# set2_ = {4556,'kasi',1008,2,3,}
# set2_.intersection_update(set1_)
# print(set1_)
# print(set2_)


"symmetric_difference()"
"returns a set containing elements of which are not common to the both the sets"
"it return s new set it wont modify the original set"
# set1_ = {1,2,3,8,100,'kasi'}
# set2_ = {456,'kasi',1008,2,3,}
# print(set1_.symmetric_difference(set2_))
# print(set1_.symmetric_difference(set2_))

# "symmetric_difference_update()"
# "it will update the base set with the elements which are of not common to both the sets"
# "it returns nothing it will modifies the original set"
# set1_ = {1,2,3,8,100,'kasi'}
# set2_ = {456,'kasi',1008,2,3,}
# # set1_.symmetric_difference_update(set2_)
# # print(set1_)
# set2_.symmetric_difference_update(set1_)
# print(set2_)


"add()"
"it will add the specified element at random position"
"if the item is already present in the list it wont add that element"
"element is the mandatory argument"
"it returns nothing and set is modified"
"the element add into the set is of immutable data type only"
# set_ = {'kasi',1008}
# set_.add('mohana')
# print(set_)
# set_.add(('rao')) # if tuple consists of single element it will add that single lement only not with tuple
# print(set_)
# set_.add(('rao',456))
# print(set_)
# set_.add(700)
# print(set_)
# set_.add(True)
# print(set_)
# # set_.add() # if item is not provided it will give type error
# set_.add(50+50J)
# print(set_)

"""remove"""
"it will remove the specified item from the set"
"it wont return anything it will modify the original set"
"if the given element is not found in the set key error will be raised"
set_ = {'python',3.10,'kasi','jmr',2020,'chennai','bangalore',2021}
set_.remove(2020)
print(set_)
# set_.remove(50000) # key error
set_ = {123,(100,1000,'jmr'),'kasi'}
# set_.remove('jmr') # key error because inside a tuple element cant be rmoved whole tuple can be remooved
# print(set_)

"discard()"
"it will removes the specified element from the set"
"it will returns nothing it will modifies the original set"
"it wont raise the error if the element is not found in the set"
set_ = {'chathrapathi','sivaji',1846,'king','of','maharastra'}
# set_.discard('of')
# print(set_)
# set_.discard(1000000) # no error raised
# print(set_)

"pop()"
"it will removes randam element from the set"
"it will takes no arguments"
"it will returns removed element from the set and it will modifies the original set"
"it will raises key error if the set is empty"
set_ = {'chathrapathi','sivaji',1846,'king','of','maharastra'}
# print(set_.pop())
# print(set_)
# set_.pop('raja') # type error as it dont takes any arguments we are passing a argument

"""issubset()"""
"if all the elements of base set are present second set then base set is called as subset of second set or original set"
"if all the elements are present in original set it will returns true or else false"
"it returns boolean value it wont modify the any of the set"
# set_ = {456,888,777}
# set2_ = {452,1007,888,456,42,777}
# print(set_.issubset(set2_))
# set_ = {456,888,777,20}
# set2_ = {452,1007,888,456,42,777}
# print(set_.issubset(set2_))
# set_ = {456,888,777}
# set2_ = {452,1007,888,42,777}
# print(set_.issubset(set2_))
# set_ = {456,888}
# set2_ = {452,1007,888,456,42,777}
# print(set_.issubset(set2_))

"""issuperset()"""
"if the all the items in the specified set is present in the original set the it will return true and the original set is "
"called as superset of base specified set"
"it will returns boolean value and it wont modifies the original set"
# set_ = {1,2,3,4}
# set2_ = {45,1,89,3,78,2,4}
# print(set2_.issuperset(set_))
# set_ = {1,2,3,4}
# set2_ = {45,1,89,3,78,2}
# print(set2_.issuperset(set_))

"isdisjoint()"
"if the both sets dosent conatining any common elemets then it returns true else false"
set_ = {1,3,4}
set2_ = {8,7}
print(set_.isdisjoint(set2_))
set_ = {456,'kasi','rao'}
set2_ = {86,'jmr',2022}
print(set_.isdisjoint(set2_))
print(set2_.isdisjoint(set_))
