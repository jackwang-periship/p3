'''
Created on Mar 9, 2017

@author: jackwang
'''

netAmount = 0
while True:
    s = raw_input('Please enter transaction type and amount in the format D/W ????: ')
    if not s:
        break
    values = s.split(" ")
    operation = values[0]
    amount = int(values[1])
    if operation=="D":
        netAmount+=amount
    elif operation=="W":
        netAmount-=amount
    else:
        pass
print netAmount
