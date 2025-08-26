# -*- coding: utf-8 -*-
"""
Created on Sun Jul 27 16:59:36 2025

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

df.to_csv("./df_sample.csv")
