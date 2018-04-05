# -*- coding: utf-8 -*-
#main_for_producing_preamble.py
from keyfield_class import Keyfield as KF
from keyfield_class import Validity_Checking as VC



"""@@@ @@@ @@@  生成ID部分 @@@ @@@ @@@"""
'''&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&  Basic Definition  &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&'''
Unique_preamble_for_USI = "mzspec"
Delimiter = ":"
collection,subfloder,msRun,indexType,scanNumber="","Control01","","scan",""

'''&&&&&&&&&&&&&&&&&&&&  Producing the basic form based on the return value   &&&&&&&&&&&&&&&&&&&&&&'''
kf=KF()
preamble = Unique_preamble_for_USI+Delimiter+kf.Keyword_of_collection()+Delimiter+\
           kf.Keyword_of_msRun()+Delimiter+indexType+Delimiter+kf.Keyword_of_scanNumber()

print("One of the examples of Basic Form for USI was :\n\n\t",str(preamble))



"""@@@ @@@ @@@  检查ID合法性部分 @@@ @@@ @@@"""
'''&&&&&&&&&&&&&&&&&&&&  Validation of the legitimacy for key fields   &&&&&&&&&&&&&&&&&&&&&&&&&&&&&'''
vc=VC(preamble)
#vc.number_of_keyfield()
#vc.keyfield_Variable()
print('check')
if vc.number_of_keyfield():
    if vc.keyfield_fixed():
        if vc.keyfield_Variable():
            print('PASS')
        else:
            print("Sorry,please check whether 'scanNumber','collection' and 'msRun' are valid")
    else:
        print("Sorry,the key field should be 'mzspec' or 'scan',please check your text")
else:
    print("Sorry,maybe Missing a key field")
    
