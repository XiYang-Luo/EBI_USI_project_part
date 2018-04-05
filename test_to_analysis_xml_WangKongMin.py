# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 16:08:48 2018

@author: luo xi yang
"""

from analysis_xml_from_WangKongMin import Analysis_Xml
pathname='C:\\Users\\luo xi yang\\Desktop\\temp_workspace\\python\\PRIDE_Exp_Complete_Ac_27179.xml'
test=Analysis_Xml(pathname)
a=test.get_xml_content()
print(a)
