# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 11:49:15 2018

@author: KaiwenZhu

@API

Ad{
link_Title: The detail of link
From: Where link user from
Link: The Link that user visited
Method: The way user visited the link
Time: The time
}
"""


from bs4 import BeautifulSoup
import re
import json

soup = BeautifulSoup(open("./Data/DATA/HTML/MyActivity.html"),"html.parser")

Datas = list()
Soups=soup.find_all('div','mdl-grid')
for s in range(len(Soups)):
    data={}
    data['Method']=Soups[s].find('p','mdl-typography--title').get_text()
    link_block = Soups[s].find('div','content-cell mdl-cell mdl-cell--6-col mdl-typography--body-1')
    data['Link']=link_block.a['href']
    data['Link_Title']=link_block.text
    try:
        data['Time']=re.search(r'[A-Z][a-z]{1,2} [0-9]{1,2}, 20[0-9]{1,2}, [0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2} [A-Z]{1,2} [A-Z]{1,3}',link_block.get_text()).group()
    except:
        print s
        data['Time']=''
    try:
        From=Soups[s].find('div','content-cell mdl-cell mdl-cell--12-col mdl-typography--caption').a['href']
        data['From']=From
    except:
        data['From']=''
    Datas.append(data)
print Datas
					
			