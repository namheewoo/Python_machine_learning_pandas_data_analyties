# -*- coding: utf-8 -*-
"""
Created on Sun Jul 27 15:03:04 2025

@author: skagm
"""

import pandas as pd
import seaborn as sns

titanic=sns.load_dataset('titanic')
df=titanic.loc[:,['age','fare']]
print(df.head())
print('\n')
print(type(df))
print('\n')

add1=df+10
print(add1.head())
print('\n')
print(type(add1))