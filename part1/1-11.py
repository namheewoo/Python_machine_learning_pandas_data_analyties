# -*- coding: utf-8 -*-
"""
Created on Sat Jul 26 15:48:37 2025

@author: skagm
"""

import pandas as pd

exam_data={'이름':['서준','우현','인아'],
    '수학':[90,80,70],'영어':[98,89,95],'음악':[85,95,100],'체육':[100,90,90]}
df=pd.DataFrame(exam_data)
df.set_index('이름',inplace=True)
print(df)
print('\n')
a=df.loc['서준','음악']
b=df.iloc[0,2]
print(a)
print(b)
c=df.loc['서준',['음악','체육']]
print(c)
d=df.iloc[0,[2,3]]
print(d)
e=df.loc['서준','음악':'체육']
print(e)
f=df.iloc[0,2:]
print(f)
g=df.loc[['서준','우현'],['음악','체육']]
print(g)
h=df.iloc[[0,1],[2,3]]
print(h)
i=df.loc['서준':'우현','음악':'체육']
print(i)
j=df.iloc[0:2,2:]
print(j)