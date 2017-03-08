'''
Created on Mar 8, 2017

@author: jackwang
'''
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

x=int(raw_input('Enter the number to calculate the factorial: '))
print fact(x)

