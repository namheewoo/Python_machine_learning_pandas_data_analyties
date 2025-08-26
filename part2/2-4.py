# -*- coding: utf-8 -*-
"""
Created on Sun Jul 27 16:12:10 2025

@author: skagm
"""

import pandas as pd

url='./sample.html'
tables=pd.read_html(url)

print(len(tables))
print('\n')

for i in range(len(tables)):
    print(f"tables[{i}]")
    print(tables[i])
    print('\n')    

df=tables[1]
df.set_index(['name'],inplace=True)
print(df)