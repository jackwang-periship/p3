'''
Created on Mar 14, 2017

@author: jwang02
'''
# Write,a,program,that,accepts,a,comma,separated,sequence,of,words,as,input,and,prints,the,words,in,a,comma-separated,sequence,after,sorting,them,alphabetically
items=[x for x in raw_input().split(',')]
items.sort()
print ','.join(items)
