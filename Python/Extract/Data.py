# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 22:05:40 2018

@author: Kaiwen Zhu
"""

import os
import ExtractActivity 

file_name = "MyActivity.html"
base_path = ".\\Takeout\\My Activity\\"
Activity_Data = dict()
E_Activity = ExtractActivity.Extract_Activity()
dirs=os.listdir(base_path)
for name in range(len(dirs)):
    Activity_Data[dirs[name]] = E_Activity.Extract_Data(base_path+dirs[name]+"\\"+file_name)

