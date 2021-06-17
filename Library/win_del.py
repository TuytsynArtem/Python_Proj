# -*- coding: utf-8 -*-
"""
Created on Tue May  4 19:34:32 2021

@author: User
"""
import tkinter as tki
import tkinter.ttk as ttk
import pandas as pd

db_1 = pd.read_excel('C:/Work/Data/Pokname.xlsx',sheet_name='Sheet1', index_col=(0))
db_3 = pd.read_excel('C:/Work/Data/pdx.xlsx',sheet_name='Sheet1', index_col=(0))

def clck():
    '''
    Parameters
    ----------
    -------
    None.
    '''
    df_1 = pd.read_excel('C:/Work/Data/Pokname.xlsx',sheet_name='Sheet1', index_col=(0))
    df_3 = pd.read_excel('C:/Work/Data/pdx.xlsx',sheet_name='Sheet1', index_col=(0))

    df_1 = df_1.drop(db_1[db_1['Name']==cmb_1.get()].index[0])
    df_3 = df_3.drop(db_1[db_1['Name']==cmb_1.get()].index[0])

    df_1.to_excel('C:/Work/Data/Pokname.xlsx',sheet_name='Sheet1')
    df_3.to_excel('C:/Work/Data/pdx.xlsx', sheet_name='Sheet1')
    win1.destroy()

win1= tki.Tk()
win1.title('Удаление покемона из базы данных')
win1.geometry('400x250+300+200')
var_3 = []
list_id =[]
c = []
len_ = db_1["Name"]

lbl_3 = tki.Label(win1, text = 'Выберите покемона для удаления', font = ('Times', 12))
lbl_3.place(x = 0, y = 0)

cmb_1 = ttk.Combobox(win1)
cmb_1['values'] = list(len_)
cmb_1.current(0)
cmb_1.focus()
cmb_1.place(x=0, y = 30)

btn_6 = tki.Button(win1, text = "Удалить", font = ('Times', 12), command = clck)
btn_6.place(x = 250, y =0, width = 100, height = 35 )

win1.mainloop()
