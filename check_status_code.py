# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 10:24:45 2018

@author: luo xi yang
"""

import requests
'''判断网页状态：200/404/401等'''
code=requests.get("https://www.ebi.ac.uk:443/pride/ws/archive/file/list/project/PXD000036").status_code
print(code) 

'''获得网页上的txt文件内容'''
import urllib
#a=urllib.request.urlopen("ftp://ftp.pride.ebi.ac.uk/pride/data/archive/2013/01/PXD000021/README.txt").read()
a=urllib.request.urlopen("ftp://ftp.pride.ebi.ac.uk/pride/data/archive/").read()
 
print(a)

with open('readme_test.txt','wb') as f:
    f.write(a)
