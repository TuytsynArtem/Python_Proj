# -*- coding: utf-8 -*-
"""
Created on Tue May  20 19:23:11 2021

@author: User
"""
import pandas as pd

data = pd.read_excel('C:/Work/Data/pdx.xlsx',sheet_name='Sheet1',index_col=0)


def database_create(filename,):
    data2 = pd.DataFrame()
    
