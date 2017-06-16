#  coffee csv file

import csv
#/home/mikeh/eca/ECA/ECA running costs.csv
f = open("/home/mikeh/eca/ECA/ECA running costs.csv")
#f = open("coffee.csv")
for row in csv.reader(f):
    print(row)


print("separator\n=======")
#f = open("coffee.csv")
f = open("/home/mikeh/eca/ECA/ECA running costs.csv")
#f=open("D:\FromLexarUSB\ClassLists\FormList-20120528-142931.csv")
for row in csv.reader(f):
    print(row[4])
