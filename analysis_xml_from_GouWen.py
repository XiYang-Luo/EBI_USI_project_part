# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 14:23:15 2018

@author: luo xi yang
"""

import xml.etree.ElementTree as ET
class Analysis_Xml():
    def __init__(self,path):
        self.path=path
        #self.tree = ET.ElementTree(file='C:\\Users\\luo xi yang\\Desktop\\temp_workspace\\python\\PRIDE_Exp_Complete_Ac_27179.xml')

    def get_xml_content(self):
        Info = []
        List = []
        tree = ET.ElementTree(file=self.path)
        for elem_PeptideItem in tree.iter(tag = 'PeptideItem'):     
            for elem_SpectrumReference in elem_PeptideItem.iterfind('SpectrumReference'):
                SpectrumReference = elem_SpectrumReference.text
                #print("<SpectrumReference>",SpectrumReference,"</SpectrumReference>")
            for elem_SpectrumFile in elem_PeptideItem.iterfind('.//userParam[@name="Spectrum File"]'):
                FileValue=elem_SpectrumFile.get("value")
                #print("name = Spectrum File","     value =",FileValue)
            for elem_SpectrumTitle in elem_PeptideItem.iterfind('.//userParam[@name="Spectrum Title"]'):
                scans=elem_SpectrumTitle.get("value").split(":")[-1]
                TitleValue=elem_SpectrumTitle.get("value")
                #print("name = Spectrum Title","    value =",TitleValue)
                #print("scans =",scans)
            Info=[SpectrumReference,FileValue,scans]
            List.append(Info)
            print(Info)
        #print(List)
        return List
