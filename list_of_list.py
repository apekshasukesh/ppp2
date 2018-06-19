import os
import sys

mylist = [['a','b','c'],['d','a','f'],['c','d']]
filList = []
for x in mylist:
    for y in x:
        if y=='a':
            filList.append(x)
            print filList
            
