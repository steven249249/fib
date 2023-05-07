# -*- coding: utf-8 -*-
"""
Created on Sun May  7 01:07:27 2023

@author: user
"""

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
    
n = 2970
try:
    fib(n)
except RecursionError:
    print("Maximum n before a crash:", n)
    
    

def dynamic_fib(n):
    f = [0, 1]    
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    return f[n]
     
print(dynamic_fib(2970))