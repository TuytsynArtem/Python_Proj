# -*- coding: utf-8 -*-
"""
Created on Tue May  4 19:34:32 2021

@author: User
"""
import tkinter as tki
import tkinter.ttk as ttk
import pandas as pd


db_1 = pd.read_excel('C:/Work/Data/Pokname.xlsx',sheet_name='Sheet1', index_col=(0))
db_2 = pd.read_excel('C:/Work/Data/Types.xlsx',sheet_name='Лист1', index_col=(0))
db_3 = pd.read_excel('C:/Work/Data/pdx.xlsx',sheet_name='Sheet1', index_col=(0))
db_4 = pd.read_excel('C:/Work/Data/Ability.xlsx',sheet_name='Лист1', index_col=(0))
db_5 = pd.read_excel('C:/Work/Data/eggs.xlsx',sheet_name='Лист1', index_col=(0))

def clck():
    '''
    Parameters
    ----------
    -------
    None.
    '''
    name = entry.get()
    h_p = var[0].get()
    a_tk = var[1].get()
    d_ef = var[2].get()
    s_pa = var[3].get()
    s_pd = var[4].get()
    s_pe = var[5].get()
    type_1 = db_2[db_2['Type_name']==cmb[0].get()].index[0]
    type_2 = db_2[db_2['Type_name']==cmb[1].get()].index[0]
    ability_1 = db_4[db_4['Ability']==cmb[2].get()].index[0]
    ability_2 = db_4[db_4['Ability']==cmb[3].get()].index[0]
    ability_h = db_4[db_4['Ability']==cmb[4].get()].index[0]
    e_g_1 = db_5[db_5['Egg Type']==cmb[5].get()].index[0]
    e_g_2 = db_5[db_5['Egg Type']==cmb[6].get()].index[0]
    if type_1==type_2:
        lbl_type.place(x  = 50, y = 290)
        lbl_abl12.place_forget()
        lbl_abl23.place_forget()
        lbl_abl13.place_forget()
        lbl_egg.place_forget()
    elif ability_1==ability_2:
        lbl_abl12.place(x  = 50, y = 370)
        lbl_abl23.place_forget()
        lbl_abl13.place_forget()
        lbl_egg.place_forget()
        lbl_type.place_forget()
    elif ability_h==ability_2:
        lbl_abl23.place(x  = 50, y = 410)
        lbl_abl13.place_forget()
        lbl_egg.place_forget()
        lbl_type.place_forget()
        lbl_abl12.place_forget()
    elif ability_h==ability_1:
        lbl_abl13.place(x  = 50, y = 410)
        lbl_egg.place_forget()
        lbl_type.place_forget()
        lbl_abl12.place_forget()
        lbl_abl23.place_forget()
    elif e_g_1==e_g_2:
        lbl_egg.place(x  = 50, y = 450)
        lbl_type.place_forget()
        lbl_abl12.place_forget()
        lbl_abl23.place_forget()
        lbl_abl13.place_forget()
    else:
        new_pokemon(name,h_p,a_tk,d_ef,s_pa,s_pd,s_pe,type_1,type_2,
                    ability_1,ability_2,ability_h,e_g_1,e_g_2)
        win1.destroy()
def new_pokemon(name,h_p,a_tk,d_ef,s_pa,s_pd,s_pe,
                type_1,type_2,ability_1,ability_2,
                ability_h,e_g_1,e_g_2):
    '''
    Parameters
    ----------
    name,h_p,
    a_tk,d_ef,
    s_pa,s_pd,
    s_pe,type_1,
    type_2,ability_1,
    ability_2,
    ability_h,e_g_1,
    e_g_2: TYPE Integer string
    -------
    None.
    '''
    data = pd.read_excel('C:/Work/Data/pdx.xlsx'
                         ,sheet_name='Sheet1',index_col=0)
    dataname = pd.read_excel('C:/Work/Data/Pokname.xlsx',
                             sheet_name='Sheet1',index_col=0)
    pokemon2 = pd.Series([h_p,a_tk,d_ef,s_pa,s_pd,s_pe,
                type_1,type_2,ability_1,ability_2,
                ability_h,e_g_1,e_g_2],
index=["HP","Atk","Def","SpA","SpD","Spe","Type I","Type II",
       "Ability I","Ability II","Hidden Ability","Egg Group I","Egg Group II"])
    pokemon3 = pd.Series([name],index = ["Name"])
    dataname=dataname.append(pokemon3,ignore_index=True)
    data=data.append(pokemon2,ignore_index=True)
    dataname.to_excel("C:/Work/Data/Pokname.xlsx")
    data.to_excel("C:/Work/Data/pdx.xlsx")

win1 = tki.Tk()
win1.title('Добавление покемона')
win1.geometry('600x600+300+200')
lbl_3 = tki.Label(win1, text = 'Введите название покемона', font = ('Times', 12))
lbl_3.place(x = 10, y = 0)
entry = tki.Entry(win1)
entry.focus()
entry.place(x = 230, y = 2)

lbl_type = tki.Label(win1, text = 'TypeI и TypeII не должны совпадать!',
                     font = ('Times', 10), fg='red')
lbl_abl12 = tki.Label(win1, text = 'AbilityI и AbilityII не должны совпадать!',
                      font = ('Times', 10), fg='red')
lbl_abl23 = tki.Label(win1, text = 'HiddenAbility и AbilityII не должны совпадать!',
                      font = ('Times', 10), fg='red')
lbl_abl13 = tki.Label(win1, text = 'HiddenAbility и AbilityI не должны совпадать!',
                      font = ('Times', 10), fg='red')
lbl_egg = tki.Label(win1, text = 'Egg Group I и Egg Group II не должны совпадать!',
                    font = ('Times', 10), fg='red')
L=0
for i in db_3.columns:
    lbl_5 = tki.Label(win1, text = i, font = ('Times', 12))
    lbl_5.place(x = 10, y = 30+40*L)
    L+=1

var = []

for i in range(len(db_3.columns[:6])):
    scale = tki.Scale(win1, orient= tki.HORIZONTAL,
                      from_=min(list(db_3[db_3.columns[i]])),
                      to=max(list(db_3[db_3.columns[i]])), resolution= 1)
    var.append(scale)
    scale.place(x = 230, y = 20+40*i, width = 200, height = 50)

cmb = []
cmb_1 = ttk.Combobox(win1)
cmb_1['values'] = list(db_2['Type_name'])
cmb_1.current(0)
cmb_1.focus()
cmb_1.place(x=230, y = 270)
cmb.append(cmb_1)
cmb_2 = ttk.Combobox(win1)
cmb_2['values'] = list(db_2['Type_name'])
cmb_2.current(0)
cmb_2.focus()
cmb_2.place(x=230, y = 310)
cmb.append(cmb_2)

for i in range(3):
    cmb_ = ttk.Combobox(win1)
    cmb_['values'] = list(db_4['Ability'])
    cmb_.current(0)
    cmb_.focus()
    cmb_.place(x=230, y = 310+40*(i+1))
    cmb.append(cmb_)

for i in range(2):
    cmb_ = ttk.Combobox(win1)
    cmb_['values'] = list(db_5['Egg Type'])
    cmb_.current(0)
    cmb_.focus()
    cmb_.place(x=230, y = 430+40*(i+1))
    cmb.append(cmb_)

btn_7 = tki.Button(win1, text = "Сохранить!",
                   font = ('Times', 12), command = clck)
btn_7.place(x = 340, y = 540, width =200, height = 35)

win1.mainloop()
    