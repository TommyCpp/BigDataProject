# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 14:01:34 2018

@author: Kaiwen

This factory is for storing the method that extract data from document.

Method:
    ExtractAdData
    ExtractSearchData

"""

from bs4 import BeautifulSoup
import re
from ExtractActivity import Extract_Activity

class Extract_Data_Factory:
    
    def __init__(self):
        self.get_data = Extract_Activity
    
        


