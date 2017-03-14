'''
Created on Mar 13, 2017

@author: jackwang
'''
import requests
from bs4 import BeautifulSoup
import pandas as pd


nws_weather_by_zip = "http://forecast.weather.gov/zipcity.php?inputstring="

page = requests.get(nws_weather_by_zip+'07436')
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]
period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()

# print(period)
# print(short_desc)
# print(temp)

img = tonight.find("img")
desc = img['title']

# print(desc)

period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
# print periods

short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]

# print(short_descs)
# print(temps)
# print(descs)

# pd.set_option('display.max_colwidth', 265)
weather = pd.DataFrame({
        "period": periods, 
        "short_desc": short_descs, 
        "temp": temps, 
        "desc":descs
    })

temp_nums = weather["temp"].str.extract("(?P<temp_num>\d+)")
weather["temp_num"] = temp_nums.astype('int')

print weather

# mydes = []
# mydes = weather["desc"]
# for i in mydes:
#     print i

current_weather = soup.find(id="current_conditions-summary")
currentCondition = current_weather.find('p')
for i in currentCondition:
    print i


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

