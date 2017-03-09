'''
Created on Mar 9, 2017

@author: jackwang
'''
values = raw_input('Please enter a sequence of comma-separated numbers: ')
numbers = [x for x in values.split(",") if int(x)%2!=0]
print ",".join(numbers)
