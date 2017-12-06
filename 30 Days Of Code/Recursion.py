#!/bin/python3
import sys
def factorial(n):
    for i in range(1,n):
        n=n*i;  
    return n
if __name__ == "__main__":
    n = int(input().strip())
    result = factorial(n)
    print(result)