# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 15:59:44 2018

@author: luo xi yang
"""

import xml.etree.ElementTree as ET
#import xml.dom.minidom
import csv
import re
class Analysis_Xml():
    def __init__(self,path):
        self.path=path
    
    def get_xml_content(self):
        number=0
        row=[]
        trees = ET.parse(self.path)
        #root = trees.getroot()
        GelNode= trees.getiterator('GelFreeIdentification')
        filename = 'C:\\Users\\luo xi yang\\Desktop\\pro.csv'
        return_values=[]
        with open(filename, 'w', newline='') as f:
            headers = ['SpectrumReference', 'Spectrum File', 'Spectrum Title']
            writer = csv.writer(f)
            writer.writerow(headers)
            for i in GelNode:
                for x in i:
                    if(x.tag=='PeptideItem'):
                        row = []
                        for j in x:
                            if(j.tag=='SpectrumReference' and j!=0):
                                row.append(j.text)
                       
                            if(j.tag=='additional'):
                                for userParam in j:
                                    number=number+1
                                    if(number==1):
                                        row.append(userParam.attrib['value'])
                             
                                    if(number==2):
                                        two=re.findall(r'scans: (\d+)',userParam.attrib['value'])
                                        row.append(two[0])
                                    
                                    if(number==2):
                                        break
                        #print(row)
                        number=0
                        return_values.append(row)
        #print(return_values)
        return return_values
    def cd_write(self,row):
        filename = 'C:\\Users\\luo xi yang\\Desktop\\pro.csv'
        with open(filename, 'w', newline='') as f:
            #headers = ['SpectrumReference', 'Spectrum File', 'Spectrum Title']
            writer = csv.writer(f)
            #writer.writerow(headers)
            writer.writerow(row)
        #PepNode=GelNode.findall('PeptideItem')
        #print(PepNode)
'''
if __name__ == '__main__':
    pathname='C:\\Users\\luo xi yang\\Desktop\\temp_workspace\\python\\PRIDE_Exp_Complete_Ac_27179.xml'
    get_xml_content(pathname)
'''
