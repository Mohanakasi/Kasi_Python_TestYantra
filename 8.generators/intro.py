"""generator function"""
def num():
    for num in range(1,50):
        if num % 2 == 0:
            yield num

res = num()
# print(list(res))

"""generator expression"""
even_ = (item for item in range(1,50) if item% 2 == 0)
# print(list(even_))

"""write a generator function and expression to yield names starting with vowels in the list"""
list_ = ['iam','kasi','userid']
def vow(list_):
    for item in list_:
        if item[0].lower() in 'aeiou':
            yield item

res = vow(list_)
print(list(res))

"""generator expression"""
vow_ = (item for item in list_ if item[0].lower() in 'aeiou')
print(list(vow_))


path = r"C:\Users\Hp\PycharmProjects\python_training\my_files\text files\sindhu12.txt"
with open(path) as file:
    def len_line(file_obj):
        for line in file_obj:
            if line.strip():
                yield len(line)

    res = len_line(file)

    print(list(res))
    file.seek(0)
    res = (len(line) for line in file if line.strip())
    print(list(res))
