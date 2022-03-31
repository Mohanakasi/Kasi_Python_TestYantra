path = r"C:\Users\Hp\PycharmProjects\Kasi_Python_TestYantra\my_files\text files\sindhu12.txt"
# with open(path) as file:
#     print(next(file))
#     print(next(file))
#     print(next(file))
#     print(next(file))
#     print(next(file))
#     print(dir(file))


l = ['kasi','user','iam','jmr']
def g_vow(l):
    for item in l:
        if item[0].lower() in 'aeiou':
            yield  item

result = g_vow(l)
print(next(result))
print(next(result))
# print(next(result)) # generator function exhusted as it doesn have any values to yield have to re-initialize


result  =g_vow(l)
print(next(result))
"""or you can traverse through it"""

result = g_vow(l)
for vowel in result:
    print(vowel)


