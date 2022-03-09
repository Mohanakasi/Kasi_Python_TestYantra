"to print 1 to 10 numbers"
# for i in range(1,11):
#     print(i, end = ' ')
# print()
"to print 10 to 1 numbers"
# for i in range(10,0,-1):
#     print(i, end = ' ')
# print()
"to print -1 to -10 numbers"
# for i in range(-1, -11, -1):
#     print(i, end = ' ')
# print()
"to print -10 to -1 numbers"
# for i in range(-10,0,1):
#     print(i, end=' ')

"packing and unpacking"
"packing or unpacking is done at left side only"

"packing"
var1 = 1,2,3
print(var1) # it will be in the form of tuple

var2 = 589,68,9,8
print(var2) # in the form of tuple
var3 = 'kasi',[1,2,3],1007
print(var3)

"unpacking"
list_ = [1,2,3]
i1,i2,i3 = list_ # works if lef side variables equals to list elements no
print(i1)
print(i2)
print(i3)
"if the iterable has more numbers"
list_ = [1,2,3,'kasi',458,89,28,969,'jmr']
i1,*res,i3 = list_
print(i1)
print(res)
print(i3)
