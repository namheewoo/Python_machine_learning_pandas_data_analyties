# -*- coding: utf-8 -*-
"""
Created on Sun Jul 27 15:11:19 2025

@author: skagm
"""

import pandas as pd
import seaborn as sns

titanic=sns.load_dataset('titanic')
df=titanic.loc[886:,['age','fare']]
print(df.head())
print('\n')
print(type(df))
print('\n')

addition=df+10
subtraction=addition-df

print(addition.head())
print('\n')
print(type(addition))
print('\n')

print(subtraction.head())
print('\n')
print(type(subtraction))