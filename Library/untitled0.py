# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 19:49:57 2021

@author: User
"""
import pandas as pd
db_id = pd.read_excel('C:/Work/Data/Pdx.xlsx',sheet_name='Sheet1',index_col=0)
id_list = list(db_id.values)
print(id_list)

print("dadsadsa",id_list[0][0])

