# -*- coding: utf-8 -*-
"""
Created on Sat Jul 26 15:11:55 2025

@author: skagm
"""

import pandas as pd

exam_data={'수학':[90,80,70],'영어':[98,89,95],'음악':[85,95,100],'체육':[100,90,90]}
df=pd.DataFrame(exam_data,index=['서준','우현','인아'])
print(df)
print('\n')
df2=df[:]
df2.drop('수학',axis=1,inplace=True)
print(df2)
df3=df.drop(['영어','음악'],axis=1)
print(df3)