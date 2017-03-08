'''
Created on Mar 8, 2017

@author: jackwang
'''
s = raw_input()
words = [word for word in s.split(" ")]
print " ".join(sorted(list(set(words))))

