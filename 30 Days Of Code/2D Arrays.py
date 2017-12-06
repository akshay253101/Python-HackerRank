#!/bin/python3

import sys

arr = []
sum_,result =0,0
flag=1
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)
for i in range(0,len(arr)//2+1):
    for j in range(0,len(arr[i])//2+1):
        sum_=arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
        if sum_>result or flag==1:
            result=sum_
            flag=0
print(result)