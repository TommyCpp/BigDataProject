# -*- coding: utf-8 -*-
"""
Created on Thu Nov 01 19:44:23 2018

@author: KaiwenZhu
"""
import json

base_path = ".\\Takeout\\My Activity\\"
f = open("ActivityData.txt",'r')
Data = json.loads(f.read())

