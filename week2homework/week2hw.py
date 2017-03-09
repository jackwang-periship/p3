'''
Created on Mar 6, 2017

@author: student
'''
import sys
from sys import argv
import urllib2
import ConfigParser
import ftplib

config = ConfigParser.RawConfigParser()

try:
    script, inifilename = argv
    config.read(inifilename)
    mySavedFileName = config.get('Location', 'DownloadFileName')
    url2bcaptured = raw_input("Please enter the website URL: ")
    f = urllib2.urlopen(url2bcaptured)
    webpageContent = f.read()
    target = open(mySavedFileName, 'w')
    target.write(webpageContent)
    target.close()

    #upload the file to ftp server     
    myUploadFileURL = config.get('Sharefile', 'url')
    myUploadServerUserName = config.get('Sharefile', 'username')
    myUploadServerPassword = config.get('Sharefile', 'password')
    myUploadTargetDirectory = config.get('Sharefile', 'targetdirectory')
    myUploadTargetFilename = config.get('Sharefile', 'targetfilename')    
    ftp = ftplib.FTP(myUploadFileURL)
    ftp.login(myUploadServerUserName, myUploadServerPassword)
    ftp.cwd(myUploadTargetDirectory)
    fh = open(mySavedFileName, 'rb')
    myResult = ftp.storbinary('STOR ' + myUploadTargetFilename, fh)
    fh.close() 
    print "INFO: %s" % myResult
    ftp.quit()
    
    print "Web page has being saved!"
except ConfigParser.Error as e:
    print 'EXCEPTION: Program Configuration File - %s' % e.message
except IOError as (errno, strerror):
    print "I/O error({0}): {1}".format(errno, strerror)
except ValueError as e:
    print 'EXCEPTION: Invalid URL - %s' % e.message
except urllib2.HTTPError  as e:
    print 'EXCEPTION: HTTPError - %s' % e.message
except urllib2.URLError  as e:
    print 'EXCEPTION: URLError - %s' % e.message
except ftplib.all_errors, e:
    print 'EXCEPTION: FTP Error - %s' % e.message
except Exception, e:
    print "Unexpected Error  - %s" % e.message



