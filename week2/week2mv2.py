'''
Created on Feb 23, 2017

@author: jackwang
'''
from sys import argv
import ConfigParser
import logging

logging.basicConfig(format='[%(asctime)s] - %(levelname)s: %(message)s')
logging.getLogger().setLevel(logging.INFO)


scriptname, input_file = argv
try:
    config = ConfigParser.SafeConfigParser()
    config.read(input_file)
    myTestToken = config.get('Avtech', 'TestToken')
    logging.info("'myTestToken' is: %s" %  myTestToken)
    
    myEndpointTest = config.get('Avtech', 'EndpointTest')
    logging.info("'myEndpointTest' is: %s" %  myEndpointTest)
    
    myUploadFileURL = config.get('Sharefile', 'url')
    logging.info("'myUploadFileURL' is: %s" %  myUploadFileURL)
    
    myUploadServerUserName = config.get('Sharefile', 'username')
    logging.info("'myUploadServerUserName' is: %s" %  myUploadServerUserName)
    
    myUploadServerPassword = config.get('Sharefile', 'password')
    logging.info("'myUploadServerPassword' is: %s" %  myUploadServerPassword)
    
    myUploadTargetDirectory = config.get('Sharefile', 'targetdirectory')
    logging.info("'myUploadTargetDirectory' is: %s" %  myUploadTargetDirectory)
except (ConfigParser.NoSectionError, 
        ConfigParser.MissingSectionHeaderError,
        ConfigParser.ParsingError,
        ConfigParser.NoOptionError,
        ConfigParser.DuplicateSectionError
        ) as e:
    logging.exception("Configuration File %s", e.message)
    
exit(0)
