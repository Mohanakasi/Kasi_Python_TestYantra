"arthematic operators"
"addition"
a = 10
b = 20
# print(a+b)
#
a = 1.5
b = 2.5
# print(a+b)

a = 50+50j
b = 60+30j
# print(a+b)

a = True
b = False
# print(a+b)

a = 'kasi'
b = 'jmr'
# print(a+b)

a = [1,2,3]
b = [4,5,6]
# print(a+b)

a = [1,2,3,'kasi',[456],{789}]
b = [34,56,89,{'a':300}]
# print(a+b)

a = (1,2,3)
b = (3,4,5,6)
# print(a+b)

"""in set two sets were not added"""
set1_ = {1,2,3,4}
set2_ = {3,4,5,6}
# print(set1_+set2_) # then we have to use unpacking
# print({*set1_,*set2_}) # it will remove duplicates while unpacking

"indictionary also addition of two dictionaries not possible"
d = {'a':320, 'b':560}
d1 = {'c':589}
# print(d+d1) # then we have to use unpacking
# print({*d, *d1}) # it will unpack only keys



"== operator"
"checks if oth the operands are equal or not"
# print(1==2) # false
# print(1==1)
# print('kasi'=='kasi') # true
# print(['kasi'] == ['k','a','s','i']) # false
# print(['a','s','k','i'] == ['k','a','s','i']) # false
"while checking collection data type with equal operator the order of the elements at left collection must be same of right"
# print(['k','a','s','i'] == ['k','a','s','i'] ) # true
"it will checks the first element in left side with first element in right side collection like wise if any one not match it" \
"will raise error if the all elements present at righrt side"


"membership operator"
"in operator"
"used to find the element in the iterable"
"if the given element is found at any position it will give true"
# print('a' in ['k','a','s','i']) #true
# print(1 in ['k','a',1,256]) #True
# print(320 in ['k','a',1,256]) # false
# print('k' in {'k','a',1,256}) # true
# print('a' in {'a':320, 'b':820}) # True



"identity operaotr"
"returns true if the two variables are pointing to same memory"
a = 320
a = b
print(a is b) # true
x = 320
print(a is x) # false