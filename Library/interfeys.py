import tkinter as tki
import tkinter.ttk as ttk
import pandas as pd
from pokemons_reproduction import reproduction,cheker


db_id = pd.read_excel('C:/Work/Data/Pdx.xlsx',sheet_name='Sheet1',index_col=0)
id_list = list(db_id.index)


db_names = pd.read_excel('C:/Work/Data/Pokname.xlsx',sheet_name='Лист1',index_col=0)
names_list = list(db_names['Pokemon'])


def mk_choise():
    names_id_list = [str(id_list[i])+'.'+names_list[i] for i in range(len(id_list))]
    return names_id_list



def clck():
    id_1 = str(cmb_1.get())
    id_1 = id_1.split('.')[0]
    id_2 = str(cmb_2.get())
    id_2 = id_2.split('.')[0]
    # print(id_1,"|",id_2,"|",int(txt.get()))
    if cheker(int(id_1),int(id_2),db_id):
        print("размножение возможно:")
        reproduction(int(id_1),int( id_2),db_id,int(txt.get()))
    else:
        print("размножение невозможно:")
    
win0= tki.Tk()
win0.title('Pokemons')

win0.geometry('600x250')

lbl_1 = tki.Label(text = 'Choose the first parent', font = ('Time', 10, 'italic'))
lbl_1.grid(column = 0, row = 0)
    
lbl_1 = tki.Label(text = 'Choose the second parent', font = ('Time', 10, 'italic'))
lbl_1.grid(column = 2, row = 0)

lbl_3 = tki.Label(text = 'Choose the amount of parents', font = ('Times', 10, 'italic'))
lbl_3.grid(row = 2)

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
cmb_2.grid(column = 2, row = 1)

txt = ttk.Entry(win0)
txt.focus()
txt.grid(row = 3)

btn = tki.Button(win0, text = 'Выполнить скрещивания!', font = ('Arial', 12), command = clck)
btn.grid(column = 2, row = 4)

win0.mainloop()
