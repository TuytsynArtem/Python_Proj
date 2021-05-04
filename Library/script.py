# -*- coding: utf-8 -*-
"""
Created on Tue May  4 21:49:40 2021

@author: User
"""
import pandas as pd
db = pd.read_excel('C:/Work/Data/pdx.xlsx',sheet_name='Sheet1',index_col=0)
ab = pd.read_excel('C:/Work/Data/Types.xlsx',sheet_name='Лист1',index_col=0)

for i in range (1,664):
    for j in range(1,19):
        if  db["Type I"][i]==ab["Type_name"][j]:
           
            db["Type I"][i]=j
        if  db["Type II"][i]==ab["Type_name"][j]:
           
            db["Type II"][i]=j
            
db.to_excel('C:/Work/Data/pdx.xlsx')
   