'''
Created on Feb 23, 2017

@author: jackwang
'''
from sys import argv
import ConfigParser


#input_file = argv
scriptname, input_file = argv
# try:
config = ConfigParser.RawConfigParser()
config.read(input_file)
# except ConfigParser.Error as e:
#     print 'EXCEPTION: Program Configuration File - %s' % e.message

myTestToken = config.get('Avtech', 'TestToken')
print "'myTestToken' is: %s" %  myTestToken

myEndpointTest = config.get('Avtech', 'EndpointTest')
print "'myEndpointTest' is: %s" %  myEndpointTest

myUploadFileURL = config.get('Sharefile', 'url')
print "'myUploadFileURL' is: %s" %  myUploadFileURL

myUploadServerUserName = config.get('Sharefile', 'username')
print "'myUploadServerUserName' is: %s" %  myUploadServerUserName

myUploadServerPassword = config.get('Sharefile', 'password')
print "'myUploadServerPassword' is: %s" %  myUploadServerPassword

myUploadTargetDirectory = config.get('Sharefile', 'targetdirectory')
print "'myUploadTargetDirectory' is: %s" %  myUploadTargetDirectory
