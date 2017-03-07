'''
Created on Mar 6, 2017

@author: student
'''
import sys
from sys import argv
import urllib2
import ConfigParser

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
except:
    print "Unexpected error:", sys.exc_info()[0]



