# -*- coding: utf-8 -*-
"""
Created on Mon Jul 28 15:07:02 2025

@author: skagm
"""

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_excel("./남북한발전전력량.xlsx",engine='openpyxl')
df_ns = df.iloc[[0,5],3:]
df_ns.index=['South','North']
df_ns.colunms=df_ns.columns.map(int)
print(df_ns.head())
print('\n')

df_ns.plot()

tdf_ns = df_ns.T
print(tdf_ns.head())
print('\n')
tdf_ns.plot()
plt.show()

