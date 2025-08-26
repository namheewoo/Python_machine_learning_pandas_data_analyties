# -*- coding: utf-8 -*-
"""
Created on Sat Jul 26 16:17:13 2025

@author: skagm
"""

import pandas as pd

exam_data={'이름':['서준','우현','인아'],
    '수학':[90, 80, 70], '영어' :[98, 89, 95], '음악' :[85, 95, 100], '체육' :[100, 90, 90]}
df=pd.DataFrame(exam_data)
print(df)
print('\n')
df['국어']=80
print(df)
