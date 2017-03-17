'''
Created on Mar 13, 2017

@author: jackwang
'''
import urllib2  
from bs4 import BeautifulSoup
from HTMLParser import HTMLParseError
import csv  
from datetime import datetime  
import urlparse

#specify the url
bn_url = "https://www.bloomberg.com/quote/SPX:IND"
 
# query the website and return the html to the variable 'page'
page = urllib2.urlopen(bn_url)
 
# parse the html using beautiful soap and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')  
 
# Take out the <div> of name and get its value
name_box = soup.find('h1', attrs={'class': 'name'})
name = name_box.text.strip() # strip() is used to remove starting and trailing  
print name 
 
# get the index price
price_box = soup.find('div', attrs={'class':'price'})  
price = price_box.text  
print price  
 
# open a csv file with append, so old data will not be erased
with open('index.csv', 'a') as csv_file:  
    writer = csv.writer(csv_file)
    writer.writerow([name, price, datetime.now()])
csv_file.close()


# bn_watch_list_url = "https://www.bloomberg.com/markets/watchlist"
# url_elements = urlparse.urlsplit(bn_watch_list_url)
# page = urllib2.urlopen(bn_watch_list_url)
# soup = BeautifulSoup(page, 'html.parser')
# benchmarks_box = soup.find('div', attrs={'class':'benchmarks_table'})
# myurls = []
# for trow in benchmarks_box.find_all('a', href=True):
#     root_url = url_elements[0] + '://' + url_elements[1]
#     abs_url = urlparse.urljoin(root_url, trow['href'])
#     myurls.append(abs_url)
# 
# indexes = []
# 
# for eachURL in myurls:
#     try:
#         rowDictionary = {}
#         name = ''
#         price = ''
#         # query the website and return the html to the variable 'page'
#         page = urllib2.urlopen(eachURL)
#         
#         if page is not None:
#             # parse the html using beautiful soap and store in variable `soup`
#             soup = BeautifulSoup(page, 'html.parser')  
#             # Take out the <div> of name and get its value
#             name_box = soup.find('h1', attrs={'class': 'name'})
#             if name_box is not None:
#                 name = name_box.text.strip() # strip() is used to remove starting and trailing  
#                 # get the index price
#             price_box = soup.find('div', attrs={'class':'price'})  
#             if price_box is not None:
#                 price = price_box.text
#             if name and price:  
#                 rowDictionary['name'] = name
#                 rowDictionary['price'] = price
#                 indexes.append(rowDictionary)
#                 print rowDictionary
#         else:
#             print "None page content from this URL: " + eachURL
#     except HTMLParseError as e:
#         print e
#     except urllib2.URLError as e:
#         print e
#     except urllib2.HTTPError as e:
#         print e
# 
# # open a csv file with append, so old data will not be erased
# with open('indexes.csv', 'a') as csv_file:
#     for eachindex in indexes:  
#         writer = csv.writer(csv_file)
#         writer.writerow([eachindex['name'], eachindex['price'], datetime.now()])
# csv_file.close()

