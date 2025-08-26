# -*- coding: utf-8 -*-
"""
Created on Sun Jul 27 15:48:07 2025

@author: skagm
"""

import pandas as pd

df1=pd.read_excel('./남북한발전전력량.xlsx', engine='openpyxl')
df2=pd.read_excel('./남북한발전전력량.xlsx', engine='openpyxl',header=None)

print(df1)
print('\n')
print(df2)
