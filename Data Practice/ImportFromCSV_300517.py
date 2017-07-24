# -*- coding: utf-8 -*-
"""
Created on Tue May 30 14:59:29 2017

@author: ImranH
"""

#import pandas
import pandas as pd

#import Matter Balances
balances = pd.read_excel(r"C:\Users\ImranH\Documents\Python Scripts\Matter_Balances_201712.xlsx", index_col = 0)

#show balances
print(balances)


print(balances.loc[[115024], ['CLNT_MATT_CODE','MP_CODE','MF_CODE','FEE_ESTIMATE']])



balances[20:22]


del balances


import gc
gc.collect()



