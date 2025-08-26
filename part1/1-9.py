# -*- coding: utf-8 -*-
"""
Created on Sat Jul 26 15:22:34 2025

@author: skagm
"""

import pandas as pd

exam_data={'수학':[90,80,70],'영어':[98,89,95],'음악':[85,95,100],'체육':[100,90,90]}
df=pd.DataFrame(exam_data,index=['서준','우현','인아'])
print(df)
label1=df.iloc[0]
position1=df.loc['서준']
print(label1)
print(position1)
label2=df.iloc[[0,1]]
position2=df.loc[['서준','우현']]
print(label2)
print(position2)
label3=df.iloc[0:1]
position3=df.loc['서준':'우현']
print(label3)
print(position3)