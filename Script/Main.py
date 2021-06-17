# -*- coding: utf-8 -*-
"""
Created on Tue May  4 19:34:32 2021

@author: User
"""
import os
import tkinter.ttk as ttk
import tkinter as tki
from playsound import playsound
import pandas as pd
os.chdir('C:/Work/Library')
from pokemons_reproduction import reproduction,cheker,graphs





i = 0
F = []
def clck2():
    '''
    Parameters
    ----------
    -------
    None.
    '''
    global F
    global i
    if i+1 <= len(F)-1:
        i+=1
        graphs(F[i],win0)

def clck3():
    '''
    Parameters
    ----------
    -------
    None.
    '''
    global F
    global i
    if i-1>=0:
        i-=1
        graphs(F[i],win0)
def clck():
    '''
    Parameters
    ----------
    -------
    None.
    '''
    global F
    global i

    try:
        ammount = int(txt.get())
        if cheker(db_1.loc[db_1["Name"]==cmb_1.get()].index.values[0],
                  db_1.loc[db_1["Name"]==cmb_2.get()].index.values[0],db_3):
            F = reproduction(db_1.loc[db_1["Name"]==cmb_1.get()].index[0],
                               db_1.loc[db_1["Name"]==cmb_2.get()].index[0],
                               db_3,ammount)
            graphs(F[i],win0)
            lbl_100 = tki.Label(text = 'Размножение возможно', font = ('Times', 12))
            playsound('C:/Work/Data/pika.mp3')
            lbl_100.place(x = 420, y = 150)
            btn67.place(x = 350, y = 150 )
            btn76.place(x = 350, y = 190 )

        else:
            lbl_100 = tki.Label(text = 'Размножение невозможно', font = ('Times', 12))
            lbl_100.place(x = 420, y = 150)
            btn67.place_forget()
            btn76.place_forget()
    except ZeroDivisionError:
        lbl_100 = tki.Label(text = 'Введите корректное число', font = ('Times', 12))
        lbl_100.place(x = 420, y = 150)

db_1 = pd.read_excel('C:/Work/Data/Pokname.xlsx',sheet_name='Sheet1', index_col=(0))
db_3 = pd.read_excel('C:/Work/Data/Pdx.xlsx',sheet_name='Sheet1', index_col=(0))

win0= tki.Tk()
win0.title('Анализ разможения покемонов')
win0.geometry('800x555+400+200')
win0.resizable(False, False)

f_top = tki.LabelFrame(win0, text = 'Графики')
f_top.place(x = 10, y = 10,  width = 340, height = 250)

btn67 = tki.Button(win0, text = 'Далее', font = ('Times', 12),command= clck2)
btn76 = tki.Button(win0, text = 'Назад', font = ('Times', 12),command= clck3)

btn = tki.Button(win0, text = 'Размножить', font = ('Times', 12))
btn.place(x = 650, y = 120 )


lbl_2 = tki.Label(win0, text = 'База данных', font = ('Times', 12))
lbl_2.place(x = 15, y = 265 )
j =0
var_3 =[]


tree = ttk.Treeview(win0)
tree['show'] = 'headings'
col = ('Название покемона', 'Данные')
for j in db_3.columns[1:]:
    col = col + (str(j),)
tree['columns']=col
tree.column('Название покемона', width= 150)
tree.heading('Название покемона', text = 'Название покемона')
tree.column('Данные', width= 50)
tree.heading('Данные', text = 'HP')
for j in col[2:]:
    tree.column(j, width= 50)
    tree.heading(j, text = j)


date_list = [list(k) for k in list(db_3.values)]
for j in range(len(list(db_1.values))):
    date_list[j].insert(0,db_1.values[j][0])

lbl_1 = tki.Label(text = 'Первый родитель', font = ('Times', 12))
lbl_1.place(x = 350, y = 10)

lbl_3 = tki.Label(text = 'Второй родитель', font = ('Times', 12))
lbl_3.place(x = 550, y = 10)

lbl_4 = tki.Label(text = '     Количество размножений', font = ('Times', 12))
lbl_4.place(x = 400, y = 80)

list_ = [j[0] for j in list(db_1.values)]
cmb_1 = ttk.Combobox(win0)
cmb_1['values'] = list_
cmb_1.current(0)
cmb_1.focus()
cmb_1.place(x = 350, y = 40)

cmb_2 = ttk.Combobox(win0)
cmb_2['values'] = list_
cmb_2.current(0)
cmb_2.focus()
cmb_2.place(x = 550, y = 40)

txt = ttk.Entry(win0)
txt.focus()
txt.place(x=450, y= 120 )

date_list.reverse()
tree.place(x = 15 , y = 295, width=750, height=240)


# создание кнопки
btn = tki.Button(win0, text = 'Размножить', font = ('Times', 12),command = clck)
btn.place(x = 650, y = 120 )
# создание таблицы

for j in date_list:
    tree.insert('', 0, values = tuple(j))


# создание двух скроллбаров
scrl_x = ttk.Scrollbar(win0, command = tree.xview, orient = tki.HORIZONTAL)
scrl_x.place(x = 15, y = 535, width = 750, height = 20)
tree.configure(xscrollcommand = scrl_x.set)

scrl_y = ttk.Scrollbar(win0, command = tree.yview, orient = tki.VERTICAL)
scrl_y.place(x = 765, y = 295, width = 20, height = 240)
tree.configure(yscrollcommand = scrl_y.set)
def clck5():
    '''
    Parameters
    ----------
    -------
    None.
    '''
    os.system("python C:/Work/Library/win_del.py")
btn_1 = tki.Button(win0, text = 'Удалить покемона', font = ('Times', 12),command = clck5)
btn_1.place(x = 125, y = 260, width = 195, height = 35)
def clck4():
    '''
    Parameters
    ----------
    -------
    None.
    '''
    os.system("python C:/Work/Library/add_win.py")
btn_2 = tki.Button(win0, text = 'Добавить покемона', font = ('Times', 12),command = clck4)
btn_2.place(x = 315, y = 260, width = 195, height = 35 )

# btn_3 = tki.Button(win0, text = 'Добавить характеристику', font = ('Times', 10))
# btn_3.place(x = 375, y = 190, width = 130, height = 35 )
def clck7():
    '''
    Parameters
    ----------
    -------
    None.
    '''
    dbdb = pd.read_excel('C:/Work/Data/Pokname.xlsx',sheet_name='Sheet1', index_col=(0))
    dbdb3 = pd.read_excel('C:/Work/Data/Pdx.xlsx',sheet_name='Sheet1', index_col=(0))
    treet = ttk.Treeview(win0)
    treet['show'] = 'headings'
    colol = ('Название покемона', 'Данные')
    for m_m_m in dbdb3.columns[1:]:
        colol = colol + (str(m_m_m),)
    treet['columns']=colol
    treet.column('Название покемона', width= 150)
    treet.heading('Название покемона', text = 'Название покемона')
    treet.column('Данные', width= 50)
    treet.heading('Данные', text = 'HP')
    for m_m_m in colol[2:]:
        treet.column(m_m_m, width= 50)
        treet.heading(m_m_m, text = m_m_m)
    date_listt = [list(k) for k in list(dbdb3.values)]
    for m_m_m in range(len(list(dbdb.values))):
        date_listt[m_m_m].insert(0,dbdb.values[m_m_m][0])
    date_listt.reverse()
    treet.place(x = 15 , y = 295, width=750, height=240)
    for m_m_m in date_listt:
        treet.insert('', 0, values = tuple(m_m_m))
    scrl_xl = ttk.Scrollbar(win0, command = treet.xview, orient = tki.HORIZONTAL)
    scrl_xl.place(x = 15, y = 535, width = 750, height = 20)
    treet.configure(xscrollcommand = scrl_xl.set)
    scrl_yl = ttk.Scrollbar(win0, command = treet.yview, orient = tki.VERTICAL)
    scrl_yl.place(x = 765, y = 295, width = 20, height = 240)
    treet.configure(yscrollcommand = scrl_yl.set)
btn_4 = tki.Button(win0, text = "Обновить таблицу", font = ('Times', 12),command = clck7)
btn_4.place(x = 500, y = 260, width = 140, height = 35 )
def clck6():
    '''
    Parameters
    ----------
    -------
    None.
    '''
    os.system("python C:/Work/Library/otbor.py")
btn_5 = tki.Button(win0, text = "Отобрать", font = ('Times', 12),command = clck6)
btn_5.place(x = 640, y = 260, width = 140, height = 35 )

win0.mainloop()
