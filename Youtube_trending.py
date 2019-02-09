# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import csv

# pip install pyopenssl ndg-httpsclient pyasn1

url1 = "https://www.youtube.com" #+ str(page)
source_code = requests.get(url1)
plain_text = source_code.text
soup = BeautifulSoup(plain_text,"lxml") #pip install lxml
List=[]
for link1 in soup.findAll('a',{'class':'guide-item yt-uix-sessionlink yt-valign spf-link ','data-external-id':'trending'}):
    print "link1 :",link1
    href1 = link1.get('href')
    # print "href :",href
    List.append(href1)
print "List :",List

List3=[]
title_list=[]
href_list=[]
dict3={}
for link2 in List:
    url2=url1+str(link2)
    print "url2 :",url2
    for link3 in soup.findAll('a',{'class':' yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link '}):
        href3 = link3.get('href')#.encode('utf-8')
        title3=link3.get('title').encode('utf-8')
        href_list.append(url1+href3) #for adding youtube in front
        title_list.append(title3)
        final= str(title3) + " : "+ url1+href3
        List3.append(final)
        dict3[title3]=url1+href3
print "List3 :",List3
print "*"*100
print "title_list :",title_list
print "*"*100
print "href_list :",href_list
print "*"*100
print "dict3 :",dict3
print "*"*100
#   Using Pandas
#https://stackoverflow.com/questions/13437727/python-write-to-excel-spreadsheet
df = pd.DataFrame({'Video_Title': title_list,'Video_Link': href_list})
df.to_excel('Youtube_trending_csv_using_pandas.xlsx', sheet_name='sheet1',index=False)

with open('Youtube_trending_csv_using_csv.csv', 'w') as csvfile:
    fieldnames = ['Video_Title', 'Video_Link']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for x in dict3:
        writer.writerow({'Video_Title': x, 'Video_Link':dict3[x]})