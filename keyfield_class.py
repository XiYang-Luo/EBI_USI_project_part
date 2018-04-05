# -*- coding: utf-8 -*-
#keyfield_class.py
import re
class Keyfield():
    def __init__(self):
        pass
    
    def Keyword_of_collection(self):
        return "PXD000561"
    
    def Keyword_of_subfloder(self):
        return "Control01"
    
    def Keyword_of_msRun(self):
        return "Adult_Frontalcortex_bRP_Elite_85_f09"
    
    def Keyword_of_indexType(self):
        return "scan"
    
    def Keyword_of_scanNumber(self):
        return "17555"
        
class Validity_Checking():
    def __init__(self,preamble):
        self.preamble=preamble
        self.Unique_preamble_for_USI = "mzspec"
        self.indexType="scan"
        
    def number_of_keyfield(self):
        matching_rule=re.findall(r'(:)*',self.preamble)
        #print(matching_rule)
        Delimiter_number =[x for x in matching_rule if x==":"]
        if len(Delimiter_number)==4:
            return True
        else:
            return False
        
    def keyfield_fixed(self):
        fixed_keyfield1=self.preamble
        rule_for_fixed_keyfield1=re.findall(r'(mzspec)(.*)(scan)',fixed_keyfield1)
        #print(rule_for_fixed_keyfield1)
        if rule_for_fixed_keyfield1:
            if list(rule_for_fixed_keyfield1[0])[0]==self.Unique_preamble_for_USI and list(rule_for_fixed_keyfield1[0])[2]==self.indexType:
                return True
            else:
                return False
        else:
            return False
        
    def keyfield_Variable(self):
        rule_for_collection=re.findall(r'.*:PXD(\w*):.*',self.preamble)
        print(rule_for_collection)
        rule_for_scanNumber=re.findall(r'.*:(\w*)',self.preamble)
        #print(rule_for_scanNumber)
        '''Whether it is an integer or not'''
        if rule_for_scanNumber and rule_for_collection:
            if rule_for_scanNumber[0].isdigit() and rule_for_collection[0].isdigit():
                return True
            else:
                return False
        else:
            return False
