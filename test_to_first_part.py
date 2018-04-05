# -*- coding: utf-8 -*-
"""
    Analysis_Xml is used to extract key fields from the XML file:msRun,scanNumber,reference.
    Analysis_Xml needs a detailed parameter about the XML file.
    Analysis_Xml returns a list, which consists of three parts:[[reference,msRun,scanNumber],[...],...].
    In Analysis_Xml, there is a method named:get_xml_content().
    
    Created on Thu Apr  5 16:24:12 2018
    @author: luo xi yang
"""
from analysis_xml_from_GouWen import Analysis_Xml

'''Get path of *.xml'''
pathname='C:\\Users\\luo xi yang\\Desktop\\temp_workspace\\python\\PRIDE_Exp_Complete_Ac_27179.xml'

'''Define the quantity immovable'''
project_name='PXD000021'
#Get the filename in the path
filename=pathname.split("\\")[-1]
Unique_preamble_for_USI = "mzspec"
Delimiter = ":"
collection,subfloder,msRun,indexType,scanNumber="","Control01","","scan",""

'''Parsing the XML file'''
keyfield_fixed=Analysis_Xml(pathname)
return_values=keyfield_fixed.get_xml_content()

#print(len(return_values))
'''Producing the preamble based on the return value '''
dirc={}
for i in range(len(return_values)):
    #print(return_values[i][1])
    preamble = Unique_preamble_for_USI+Delimiter+project_name+Delimiter+\
               return_values[i][1].split('.')[0]+Delimiter+indexType+Delimiter+return_values[i][2]
    #print(preamble)
    key=(project_name,filename,return_values[i][0])
    #print(key)
    dirc[key]=preamble
print('\n\n')      
print(dirc)
    
