#!/bin/python3

import sys

n = int(input())
n=str(format(n,'b'))
string_find = n.split("0")
result=0
for i in range(0,len(string_find)):
    if len(string_find[i])>result:
        result=len(string_find[i])
print(result)
