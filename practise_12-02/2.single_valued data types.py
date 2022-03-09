"""""""data types are used to know what type of data present for a particular memory location"""
"every variable holds the value and every value has a data type"
"as we know python is a dynamical language there is no need to know define data type while creating a variable"
"""interpreter implicitly binds the value with the corresponding data type"""
"""to know the data type of a variable/value we use type function"""
"""there are two types of data types are there"""
"single valued and multivalued/collection data types"
"single valued"
"integer"
a = 10
b = 3
print(type(a))
"""addition"""
print("addition","---->",a+b)
"""subtraction"""
print("substraction","---->",a-b)
"multiplication"
print("multiplication","---->",a*b)
print("multiplication","---->",a*10)
"division"
print("division","---->",a/b)  #"""gives output in the form of decimal only irrespective divisible or not divisible"""
"floor division"
print("floor division,a//b)    #"gives output without decimal values"
#"if any one of the divisor of decimal it will gives you decimal output"
# x = 10.9
# y = 2
# print(x//y)

"exponent"
# a = 10
# b = 2
# print("exponent",a**b)

"modulas"
# a = 500
# b = 50
# print(a%b) # gives you coefficient   value

"abs"
"abs will convert the negative value into positive value"
# num = -320
# print(abs(num))
"""round function will round the variable / value to the nearest integer"""
# x = 10.9
# print(round(x))
# x = 10.3
# print(round(x))

"trunc"
"trunc is used to remove the decimal value present in a number"
# a = 20.5
# from math import trunc
# print(trunc(a))
# a = 20.98
# print(trunc(a))

