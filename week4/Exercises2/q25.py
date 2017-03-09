'''
Created on Mar 8, 2017

@author: jackwang
'''
value = []
items=[x for x in raw_input('Enter a sequence of comma separated 4 digit binary numbers: ').split(',')]
for p in items:
    intp = int(p, 2)
    if not intp%5:
        value.append(p)

print ','.join(value)
