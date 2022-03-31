"""write a generator function and expression to yield names starting with vowels in the list"""
list_ = ['iam','kasi','userid','entrance']
def vow_names(l):
    for item in l:
        if item[0].lower() in 'aeiou':
            yield item
            # yield l

a = vow_names(list_) # like instance creation
print(next(a))
print(next(a))
print(next(a))
print(list(vow_names(list_)))
print(dir(a))


"""write a generator expression that yileds 1-50 even numbers"""
even_gene_ = (item for item in range(1,51) if item  % 2 == 0)
print(next(even_gene_))
print(next(even_gene_))
print(next(even_gene_))
print(next(even_gene_))
print(next(even_gene_))
print(next(even_gene_))
print(list(even_gene_))

"""write a generator expression tha yields 1 -50 prime numbers"""
def prime_series(start, end):
    for num in range(start, end+1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            yield num
a = prime_series(1,50)
# print(list(a))
print(next(a)) # if we used above statement here it will raise error because it will traverse through entire
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(list(a)) # it wont start from zero again it will start from where next stopped

temp_num = 1008

"""multiple error handling"""
"in this in try block if any one got error it will go to except block and prints error messge and it wont handle " \
"next line in the try block"
try:
    print(len(str(temp_num)))
    print(len(temp_num))
    print(temp_num)
    print(temp_num / 0)
except SyntaxError:
    print("syntax error")
except TypeError:
    print("len function is only for iterables or collections")
except ZeroDivisionError:
    print("zero is not a divisor")


"""generic exception handling"""
"""here also it will handles statements from first if any got error it wont handle next statement
but the difference is we dont need to define error type in the except block and it prints default msg as erro_msg"""
a = 'kasi'
num = 1008
try:
    print(a[100])
    print(len(num))
    print(num / 0)
except BaseException as error_msg:
    print(error_msg)


"""printing our own error messeges as error messeges"""
string_ = 'kasi is king'
l = [1,2,3]
try:
    if isinstance(l, str):
        print(l.split())
    else:
        raise TypeError("enter string only")
except BaseException as ereror_msg:
    print(ereror_msg)

"""finally block"""
"""finally block excecutes at end even any try block or except or else block executes or not"""
string_ = 'kasi is king'
l = 'kasi is king'
try:
    if isinstance(l, str):
        print(l.split())
    else:
        raise TypeError("enter string only")
except BaseException as ereror_msg:
    print(ereror_msg)
finally:
    print("no errors")

import re
print(re.findall("[^0-9]+", 'hai hello 123'))
print(re.findall(r"\b\d{2}\b", 'hai hello 12'))
print((re.findall(r"\b[a-z]{4,6}\b", "hai hello how is python coninuity")))
print((re.findall(r"\b\d{6}\b", '522003 is kasi 8886213059'))) # here checks condition
print((re.findall(r"\d+", '522003 is kasi 8886213059')))
print(re.findall(r"\D", 'hai hello 123 #$%%')) # matches all apart from numbers
print(re.findall(r"\D+", 'hai hello 123 #$%%'))
print(re.findall('\d{6}','Hello KASI  560001 and 8886213059 and 090'))

"sum of individual numbers in a string using regular expresssions"
sum = 0
for item in re.findall(r"\d", 'hello 1008,560021, kasi98'):
    sum += int(item)
print(sum)

"sum of multiple numbers in a string using regular expressions"
total_ = 0
for num in re.findall(r"\d+", 'hello 1008,560021, kasi98'):
    total_ += int(num)
print(total_)

"to find total spaces in a string using regular expressions"
total_spaces = 0
for item in re.findall(r"\s", 'kasi from bangalore'):
    total_spaces += 1
print(total_spaces)

"to count the number of occurences of each non special characters (only alphabets)"
from collections import defaultdict
d = defaultdict(int)
for item in re.findall(r"[a-zA-Z]", 'hai hello @#%#@, 123'):
    d[item] += 1
print(d)

"count the characters in each word and ignore special characters"
res_2 = re.findall(r"\w+", "hai12 opi7 _issegsdgdsgo*&")
for item in res_2:
    print(item, len(item))

"count the upper case characters in string using regular expressions"
upp_chrs = re.findall(r"[A-Z]", "HAI HELLO Kasi")
count_up = 0
for char in upp_chrs:
    count_up += 1
print(count_up)

"finding valid phone numbers from a list"
l = ['123-4567-890', '888-621-3059']
for word in l:
    match = re.findall(r"\d{3}-\d{3}-\d{4}", word)
    # if match:
    #     print(match)

"finding phone numbers startiwith 8 or 9 followed by 00 ex(800 or 900)"
l = ['123-4567-890', '800-621-3059', '901-789-4568','900-745-3214']
for word in l:
    match = re.findall(r"[89]00-\d{3}-\d{4}", word)
    if match:
        print(match)


"finding vowel words in a list"
l = ['iam', 'king', 'user$$$']
for word in l:
    match = re.findall(r"\b[aeiou]\w+\b", word)
    if match:
        print(match)
