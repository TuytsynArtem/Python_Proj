# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 17:36:07 2021

@author: User
"""
import pandas as pd

db = pd.read_excel('C:/Work/Data/pdx.xlsx',sheet_name='Pokedex')

a = []
i=0
j=0
b=[]
FLAG = False
while len(db['Type I']) > i:
    FLAG = False
    if len(a) != 0 and not FLAG:
        FLAG2 = False
        j=0
        while j < len(a) and not FLAG:
            if a[j] == db['Type I'][i]:
                b[j] += 1
                FLAG2 = True
                print(a[j],b[j])
                j+=1
            else:
                j+=1
        if j==len(a) and not FLAG2:
            a.append(db['Type I'][i])
            b.append(1)
    else:
        a.append(db['Type I'][i])
        b.append(1)
        print(a[0],b[0])
    i+=1
    