#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'K. Ziegler'

#w3resource.com

l1= [3,5,1]

def sumList(lis):
    sum = 0
    for i in lis:
        sum += i
    return sum

print(sumList(l1))

def multList(lis):
    mult = 1
    for i in lis:
        mult *= i
    return mult
print(multList(l1))

def largestNum(lis):
    lis.sort()
    return(lis[-1])

print(largestNum(l1))

def smallestNum(lis):
    lis.sort()
    return lis[0]

print(smallestNum(l1))

sampleList = ['abc', 'xyz', 'aba', '1221', 'abc', 'xyz']

'''def strLen(lis):
   ctr = 0
   for word in lis:
       if len(word) >1 and word[0] == word[-1]:
           ctr += 1
        return ctr

print(strLen(sampleList))'''

def removeDuplicates(lis):
    dup_items = set()
    uniq_items = []
    for x in lis:
        if x not in dup_items :
            uniq_items.append(x)
            dup_items.add(x)
            print(uniq_items,dup_items)

print(removeDuplicates(sampleList))

sampleString= '12345abcd'
def reverseString(str):
    rstr = ''
    index = len(str)

