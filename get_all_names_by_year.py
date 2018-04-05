# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 13:54:23 2018

@author: luo xi yang
"""
import urllib
import re
import csv
with open('year.txt','r') as f:
    content=f.readlines()
    print(content)
path_year=[]
for i in content:
    path_year.append(i.strip('\n'))
print(path_year)

count=0
'''
for j in path_year:
    rule=re.findall(r'([0-9]*)',j)
    xml_name=urllib.request.urlopen(j).read()
    print(xml_name)
    
    with open(rule[-5]+'_'+rule[-3]+'.txt','wb') as f:
        f.write(xml_name)
    count+=1
    '''
path1="C:\\Users\\luo xi yang\\Desktop\\temp_workspace\\python\\usi_project\\test\\test_to_get_All_USI_Project\\alpha_test\\"
dirc={}
for j in path_year:
    rule=re.findall(r'([0-9]*)',j)
    name=rule[-5]+'_'+rule[-3]
    path2=path1+name+'.txt'
    with open(path2,'r') as f1:
        PXD=f1.readlines()
        print(PXD)
    a=[]   
    for k in range(0,len(PXD)):
        rule2=re.findall(r'(PXD[0-9]*)\n',PXD[k])
        rule3=re.findall(r'(PRD[0-9]*)\n',PXD[k])
        print(rule2)
        if rule2:
            a.append(rule2[0])
        if rule3:
            a.append(rule3[0])
    dirc[name]=a
f1.close()
print(dirc)  


 
        
