# -*- coding: utf-8 -*-
"""
Created on Mon Jul 28 16:02:34 2025

@author: skagm
"""

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_excel("./남북한발전전력량.xlsx",engine='openpyxl')
df_ns = df.iloc[[0,5],3:]
df_ns.index=['South','North']
df_ns.columns=df_ns.columns.map(int)

tdf_ns = df_ns.T
tdf_ns = tdf_ns.apply(pd.to_numeric, errors='coerce')
tdf_ns.plot(kind='hist')
plt.show()