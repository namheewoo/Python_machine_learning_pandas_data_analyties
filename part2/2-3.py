# -*- coding: utf-8 -*-
"""
Created on Sun Jul 27 16:09:46 2025

@author: skagm
"""

import pandas as pd

df=pd.read_json('./read_json_sample.json')
print(df)
print('\n')
print(df.index)
