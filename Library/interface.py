# -*- coding: utf-8 -*-
"""
Created on Thu May 20 15:06:21 2021

@author: User
"""
import tkinter as tki
import tkinter.ttk as ttk
import pandas as pd

def mk_choise():
    '''
    Parameters
    ----------    -------
    return names_id_list

    '''

    db_id = pd.read_excel('C:/Work/Data/Pdx.xlsx',sheet_name='Sheet1')
    id_list = list(db_id['Id_pokemon'])

    db_names = pd.read_excel('C:/Work/Data/Pokname.xlsx',sheet_name='Лист1')
    names_list = list(db_names['Pokemon'])

    names_id_list = [str(id_list[i])+'.'+names_list[i] for i in range(len(id_list))]
    return names_id_list



win0= tki.Tk()
win0.title('Покемоны')
win0.geometry('600x250')

lbl_1 = tki.Label(text = 'choose the first parent', font = ('Time', 10, 'italic'))
lbl_1.grid(column = 0, row = 0)
    
lbl_1 = tki.Label(text = 'choose the second parent', font = ('Time', 10, 'italic'))
lbl_1.grid(column = 1, row = 0)

list_ = mk_choise()

cmb_1 = ttk.Combobox(win0)
cmb_1['values'] = list_
cmb_1.current(0)
cmb_1.focus()
cmb_1.grid(column = 0, row = 1)

cmb_2 = ttk.Combobox(win0)
cmb_2['values'] = list_
cmb_2.current(0)
cmb_2.focus()
cmb_2.grid(column = 1, row = 1)

win0.mainloop()
