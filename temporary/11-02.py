import os
import csv
from collections import *
""""""
path = r"C:\Users\Hp\PycharmProjects\Alpha_3\files_directory\csv_files\vaccination_data.csv"
# with open(path) as csv_file:
#     row_object = csv.DictReader(csv_file)
#     next(row_object)
#     for row in row_object:
#         if row['TOTAL_VACCINATIONS']:
#             if int(row['TOTAL_VACCINATIONS']) < 7000:
#                 print(row['COUNTRY'])

with open(path) as csv_file:
    row_obj = csv.DictReader(csv_file)
    next(row_obj)
    dd = defaultdict(list)
    for row in row_obj:
        dd[row['DATE_UPDATED']] += [(row['COUNTRY'],row['TOTAL_VACCINATIONS'])]

