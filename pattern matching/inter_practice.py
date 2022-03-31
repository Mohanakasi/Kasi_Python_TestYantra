"Write a program to count the number of occurrences of each word in a file."
import re

path = r"C:\Users\Hp\PycharmProjects\Kasi_Python_TestYantra\my_files\text files\sindhu12.txt"
from collections import defaultdict
d = defaultdict(int)
with open(path) as file:
    for line in file:
        l = line.split()
        for word in l:
            d[word] += 1
    # print(d)

"Write a program to count the number of occurrences of vowels in a file."
from collections import defaultdict
d = defaultdict(int)
with open(path) as file:
    for line in file:
        if line.strip():
            l = line.split()
            for word in l:
                if word[0].lower() in 'aeiou':
                    d[word] += 1
    print(d)

"""Write a program to print all numeric values in a list"""
items = ['apple', 1.2, 'google', '12.6', 26, '100']
for item in items:
    if isinstance(item, str):
        if item.isnumeric():
            print(int(item))
    elif isinstance(item, (int, float, complex)):
            print(item)

"""left justified triangle"""
for i in range(1,6):
    print(f"{'* '*i: <5}")

"""Write a program count the occurrence of a particular word in the file"""
w = 'Sindhu'
c = 0
with open(path) as file:
    for line in file:
        if line.strip():
            print(re.findall(w, line))
            # print(re.findall('is', line))
            c += len(re.findall(w, line))
    print(c)

"""Write a program to map a product to a company and build a dictionary with company and list of products pair"""
all_products = ['iPhone', 'Mac', 'Gmail', 'Maps', 'iWatch', 'Windows',
	                'iOS', 'Google Drive', 'One Drive']
# Pre-defined products for different companies
apple_products = {'iPhone', 'Mac', 'iWatch'}
google_products = {'Gmail', 'Maps', 'Google Drive'}
msft_products = {'Windows', 'One Drive'}
d = defaultdict(list)
for product in all_products:
    if product in apple_products:
        d['apple_products'].append(product)
    elif product in google_products:
        d['google_products'].append(product)
    elif product in msft_products:
        d['msft_products'].append(product)
print(d)

"""Write a program to rotate items of the list"""
names = ["apple", "google", "yahoo", "gmail", "facebook", "flipkart", "amazon"]
def rotat_el_(list_, n):
    for i in range(n):
        res = names.pop()
        names.insert(0, res)
    return names
print(rotat_el_(names, 3))





