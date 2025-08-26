# -*- coding: utf-8 -*-
"""
Created on Mon Jul 28 14:18:00 2025

@author: skagm
"""

import pandas as pd

df=pd.read_csv('./auto-mpg.csv',header=None)
df.columns=['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']
print(df.head())
print('\n')
print(df.head())

print(df.shape)
print(df.info())

print(df.dtypes)
print(df.mpg.dtypes)

print(df.describe())
print('\n')
print(df.describe(include='all'))

