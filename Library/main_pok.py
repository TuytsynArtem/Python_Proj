import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.gridspec as gridspec
import os
import tkinter as tki
import tkinter.ttk as ttk

db_1 = pd.read_excel('C:\Work\Data\Pokname.xlsx',sheet_name='Sheet1', index_col=(0))
db_3 = pd.read_excel('C:\Work\Data\Pdx.xlsx',sheet_name='Sheet1', index_col=(0))

win0= tki.Tk()
win0.title('Анализ разможения покемонов')
win0.geometry('800x500+300+200')

f_top = tki.LabelFrame(win0, text = 'визуализация')
f_top.place(x = 10, y = 10,  width = 340, height = 180)


lbl_2 = tki.Label(win0, text = 'База данных', font = ('Times', 12))
lbl_2.place(x = 15, y = 200 )
i =0
var_3 =[]
# создание кнопки
btn = tki.Button(win0, text = 'Выполнить', font = ('Times', 12))#, command = clck)
btn.place(x = 650, y = 120 )
# создание таблицы

tree = ttk.Treeview(win0)
tree['show'] = 'headings'
col = ('Название покемона', 'Данные')
for i in db_3.columns[1:]:
    col = col + (str(i),)#.split(' ')[0]),)
    print(col)
tree['columns']=col
tree.column('Название покемона', width= 150)
tree.heading('Название покемона', text = 'Название покемона')
tree.column('Данные', width= 50)
tree.heading('Данные', text = 'HP')
for i in col[2:]:
    tree.column(i, width= 50)
    tree.heading(i, text = i)


date_list = [list(k) for k in list(db_3.values)]
print(len(date_list))
print(len(list(db_1.values)))
for i in range(len(list(db_1.values))):
    date_list[i].insert(0,db_1.values[i][0])
    
lbl_1 = tki.Label(text = 'Выберите первого родителя', font = ('Times', 12))
lbl_1.place(x = 350, y = 10)

lbl_3 = tki.Label(text = 'Выберите второго родителя', font = ('Times', 12))
lbl_3.place(x = 550, y = 10)

lbl_4 = tki.Label(text = 'Выберите количество размножений', font = ('Times', 12))
lbl_4.place(x = 400, y = 80)

list_ = [i[0] for i in list(db_1.values)]
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
tree.place(x = 15 , y = 225, width=750, height=240)

for i in date_list:
    tree.insert('', 0, values = tuple(i))
    

# создание двух скроллбаров    
scrl_x = ttk.Scrollbar(win0, command = tree.xview, orient = tki.HORIZONTAL)
scrl_x.place(x = 15, y = 465, width = 750, height = 20)
tree.configure(xscrollcommand = scrl_x.set)

scrl_y = ttk.Scrollbar(win0, command = tree.yview, orient = tki.VERTICAL)
scrl_y.place(x = 765, y = 225, width = 20, height = 240)
tree.configure(yscrollcommand = scrl_y.set)

btn_1 = tki.Button(win0, text = 'Удалить покемона', font = ('Times', 12))#, command = clck_1)
btn_1.place(x = 125, y = 190, width = 130, height = 35)

btn_2 = tki.Button(win0, text = 'Добавить покемона', font = ('Times', 12))#, command = clck_2)
btn_2.place(x = 250, y = 190, width = 130, height = 35 )

btn_3 = tki.Button(win0, text = 'Добавить характеристику', font = ('Times', 12))#, command = clck_3)
btn_3.place(x = 375, y = 190, width = 130, height = 35 )

btn_4 = tki.Button(win0, text = "Обновить таблицу", font = ('Times', 12))#, command = clck_4)
btn_4.place(x = 500, y = 190, width = 140, height = 35 )

btn_5 = tki.Button(win0, text = "Отобрать", font = ('Times', 12))#, command = clck_5)
btn_5.place(x = 640, y = 190, width = 140, height = 35 )

win0.mainloop()