# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 13:58:46 2018

@author: Kaiwen Zhu
"""

import re
from bs4 import BeautifulSoup




class Extract_Activity:
    
        def __init___(self):
            self.amount = 0
            
        
        def Extract_Data(self, path, Datas):
            soup = BeautifulSoup(open(path),"html.parser")
            Soups = soup.find_all('div','outer-cell mdl-cell mdl-cell--12-col mdl-shadow--2dp')
            for s in range(len(Soups)):
                data = dict()
    
                ## 0: The Devcie name or Website Name
                try:
                    data["type"] = Soups[s].find('p','mdl-typography--title').get_text().strip(' ')
                except:
                    data["type"] = None
    
                link_block = Soups[s].find('div','content-cell mdl-cell mdl-cell--6-col mdl-typography--body-1')
    
    
                ## 1: The website link, some items don't have link
                try:
                    data["link"] = link_block.a['href'].strip(' ')
                except:
                    data["link"] = None
        
    
                ## 2: The Time
                try:
                    Time = re.search(r'[A-Z][a-z]{1,2} [0-9]{1,2}, 20[0-9]{1,2}, [0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2} [A-Z]{1,2} [A-Z]{1,3}',link_block.get_text()).group()
                    data["time"] = Time
                except:
                    data["time"] = None
    
    
                ## 3: The Action or the title of the link
                try:
                    data["content"] = link_block.text.strip(Time)
                except:
                    data["content"] = None
                try:
                    Detail = Soups[s].find('div','content-cell mdl-cell mdl-cell--12-col mdl-typography--caption')
    
                    ## 4: The detail
                    Items = Detail.find_all('b')
                    Txt = Detail.text
                    NowTxt = Txt
    
                    for i in range(len(Items)):
                        First = NowTxt.strip(Items[i].text).strip(u'\u2003')
                        if i == len(Items)-2:
                            Array = First.split(Items[i+1].text)
                            Array[0] = Array[0].strip(u'\u2003')
                            Array[1] = Array[1].strip(u'\u2003')
                            data["last_link"] = data["last_link"] + Array
                            break
                        else:
                            Array = First.split(Items)
                            data["last_link"] = data["last_link"] + Array[0].strip(u'\u2003')
                            NowTxt = Array[1]
                except:
                    data["last_link"] = None

                Datas.append(data)
            return Datas
