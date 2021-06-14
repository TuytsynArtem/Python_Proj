# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 17:12:36 2021

@author: User
"""

import random
import pandas as pd
import matplotlib.pyplot as plt
from plot import save,pie
data = pd.read_excel('C:/Work/Data/pdx.xlsx',sheet_name='Sheet1',index_col=0)
eggs_connection = pd.read_excel('C:/Work/Data/eggs_connection.xlsx',sheet_name='Лист1',index_col=0)
data = pd.read_excel('C:/Work/Data/pdx.xlsx',sheet_name='Sheet1',index_col=0)
def boxplot():
    data.boxplot(column='Spe', by='Type I')
    plt.show() 
 
boxplot()