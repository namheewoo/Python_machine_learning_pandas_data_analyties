# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 15:17:17 2025

@author: skagm
"""

import pandas as pd

list_data=['2019-01-02', 3.14, 'ABC', 100, True]
sr=pd.Series(list_data)
print(sr)

idx=sr.index
val=sr.values
print('\n')
print(val)