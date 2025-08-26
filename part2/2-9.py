# -*- coding: utf-8 -*-
"""
Created on Mon Jul 28 13:59:30 

@author: skagm
"""
import pandas as pd

data= {'name' : [ 'Jerry', 'Riah', 'Paul'],
        'algol' : [ "A", "A+", "B"],
        'basic' : [ "C", "B", "B+"],
        'c++' : [ "B+", "C", "C+"],
        }
df=pd.DataFrame(data)
df.set_index('name',inplace=True)
print(df)

df.to_excel('./df_sample.xlsx')
