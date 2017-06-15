#  coffee csv file

import csv
f=open("coffee.csv")
for row in csv.reader(f):
    print(row)


print("separator\n=======")
#f=open("coffee.csv")
f=open("D:\FromLexarUSB\ClassLists\FormList-20120528-142931.csv")
for row in csv.reader(f):
    print(row[5])

    
