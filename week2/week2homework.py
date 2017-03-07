'''
Created on Feb 24, 2017

@author: jackwang
'''
# Import the module
import urllib2

# Ask the user for input
host = raw_input("Enter a host to ping: ")    

# Set up the echo command and direct the output to a pipe
f = urllib2.urlopen(host)

print f.read()

