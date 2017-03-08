'''
Created on Mar 8, 2017

@author: jackwang
'''
tp=(1,2,3,4,5,6,7,8,9,10,13,17,19,20,21)
li=list()
for i in tp:
    if i%2==0:
        li.append(i)

tp2=tuple(li)
print tp2
