import pandas as pd
import tkinter as tki
import tkinter.ttk as ttk

db_1 = pd.read_excel('C:\Work\Data\Pokname.xlsx',sheet_name='Sheet1', index_col=(0))
db_2 = pd.read_excel('C:\Work\Data\Types.xlsx',sheet_name='Лист1', index_col=(0))
db_3 = pd.read_excel('C:\Work\Data\pdx.xlsx',sheet_name='Sheet1', index_col=(0))
db_4 = pd.read_excel('C:\Work\Data\Ability.xlsx',sheet_name='Лист1', index_col=(0))
db_5 = pd.read_excel('C:\Work\Data\eggs.xlsx',sheet_name='Лист1', index_col=(0))

def clck():
    HP_1 = var[0].get()
    HP_2 = var[1].get()
    Atk_1 = var[2].get()
    Atk_2 = var[3].get()
    Def_1 = var[4].get()
    Def_2 = var[5].get()
    SpA_1 = var[6].get()
    SpA_2 = var[7].get()
    SpD_1 = var[8].get()
    SpD_2 = var[9].get()
    Spe_1 = var[10].get()
    Spe_2 = var[11].get()
    TypeI = db_2[db_2['Type_name']==cmb[0].get()].index[0]
    TypeII = db_2[db_2['Type_name']==cmb[1].get()].index[0]
    AbilityI = db_4[db_4['Ability']==cmb[2].get()].index[0]
    AbilityII = db_4[db_4['Ability']==cmb[3].get()].index[0]
    HiddenAbility = db_4[db_4['Ability']==cmb[4].get()].index[0]
    EggGroupI = db_5[db_5['Egg Type']==cmb[5].get()].index[0]
    EggGroupII = db_5[db_5['Egg Type']==cmb[6].get()].index[0]
    if HP_1>=HP_2:
        lbl_HI.place(x = 550, y = 30)
        lbl_type.place_forget()
        lbl_abl12.place_forget()
        lbl_abl23.place_forget()
        lbl_abl13.place_forget()
        lbl_egg.place_forget()
    elif Atk_1>=Atk_2:
        lbl_HI.place(x = 550, y = 70)
        lbl_type.place_forget()
        lbl_abl12.place_forget()
        lbl_abl23.place_forget()
        lbl_abl13.place_forget()
        lbl_egg.place_forget()
    elif Def_1>=Def_2:
        lbl_HI.place(x = 550, y = 110)
        lbl_type.place_forget()
        lbl_abl12.place_forget()
        lbl_abl23.place_forget()
        lbl_abl13.place_forget()
        lbl_egg.place_forget()
    elif SpA_1>=SpA_2:
        lbl_HI.place(x = 550, y = 150)
        lbl_type.place_forget()
        lbl_abl12.place_forget()
        lbl_abl23.place_forget()
        lbl_abl13.place_forget()
        lbl_egg.place_forget()
    elif SpD_1>=SpD_2:
        lbl_HI.place(x = 550, y = 190)
        lbl_type.place_forget()
        lbl_abl12.place_forget()
        lbl_abl23.place_forget()
        lbl_abl13.place_forget()
        lbl_egg.place_forget()
    elif Spe_1>=Spe_2:
        lbl_HI.place(x = 550, y = 230)
        lbl_type.place_forget()
        lbl_abl12.place_forget()
        lbl_abl23.place_forget()
        lbl_abl13.place_forget()
        lbl_egg.place_forget()
    elif TypeI==TypeII:
        lbl_type.place(x  = 50, y = 290)
        lbl_HI.place_forget()
        lbl_abl12.place_forget()
        lbl_abl23.place_forget()
        lbl_abl13.place_forget()
        lbl_egg.place_forget()
    elif AbilityI==AbilityII:
        lbl_abl12.place(x  = 50, y = 370)
        lbl_HI.place_forget()
        lbl_abl23.place_forget()
        lbl_abl13.place_forget()
        lbl_egg.place_forget()
        lbl_type.place_forget()
    elif HiddenAbility==AbilityII:
        lbl_abl23.place(x  = 50, y = 410)
        lbl_HI.place_forget()
        lbl_abl13.place_forget()
        lbl_egg.place_forget()
        lbl_type.place_forget()
        lbl_abl12.place_forget()
    elif HiddenAbility==AbilityI:
        lbl_abl13.place(x  = 50, y = 410)
        lbl_egg.place_forget()
        lbl_HI.place_forget()
        lbl_type.place_forget()
        lbl_abl12.place_forget()
        lbl_abl23.place_forget()
    elif EggGroupI==EggGroupII:
        lbl_egg.place(x  = 50, y = 490)
        lbl_HI.place_forget()
        lbl_type.place_forget()
        lbl_abl12.place_forget()
        lbl_abl23.place_forget()
        lbl_abl13.place_forget()
    else:
        lbl_egg.place_forget()
        lbl_HI.place_forget()
        lbl_type.place_forget()
        lbl_abl12.place_forget()
        lbl_abl23.place_forget()
        lbl_abl13.place_forget()
        sortirovka(HP_1, HP_2,Atk_1, Atk_2,Def_1, Def_2,SpA_1, SpA_2, SpD_1, SpD_2,Spe_1, Spe_2,TypeI,TypeII,AbilityI,AbilityII,HiddenAbility,EggGroupI,EggGroupII)
        win1.destroy()


def sortirovka(temp_hp_1,temp_hp_2,temp_atk_1,temp_atk_2,temp_def_1,temp_def_2,
               temp_spa_1,temp_spa_2,temp_spd_1,temp_spd_2,temp_spe_1,
               temp_spe_2,temp_type1_1,temp_type1_2,temp_type2_1,temp_type2_2,
               temp_ability1_1,temp_ability1_2,temp_ability2_1,temp_ability2_2,
               temp_hidden_ability_1,temp_hidden_ability_2,temp_egg1_1,
               temp_egg1_2,temp_egg2_1,temp_egg2_2):
    data = pd.read_excel('C:/Work/Data/Pdx.xlsx',sheet_name='Sheet1')
    suitable_id = []
    temp_suitable_id = []
    stop_flag = False
    
    
    if (stop_flag == False):
        if ((int(temp_hp_1) !=0) and (int(temp_hp_2) !=0) ):#check
            if (len(suitable_id) != 0): 
                   temp_suitable_id = suitable_id.copy()
                   suitable_id.clear()
                   for j in range(len(temp_suitable_id)):  
                       if ((int(temp_hp_1) <= data['HP'][temp_suitable_id[j]]) and (int(temp_hp_2) >= data['HP'][temp_suitable_id[j]])) :#check
                               suitable_id.append(temp_suitable_id[j])
                       if (len(suitable_id) ==0):
                           stop_flag = True
            else:
                for i in range(len(data)):
                    if ((int(temp_hp_1) <= int(data['HP'][i])) and (int(temp_hp_2) >= int(data['HP'][i])))   :  #check               
                        suitable_id.append(i)
                if (len(suitable_id) ==0):
                          stop_flag = True   
                          3                  
    if (stop_flag == False):
        if ((int(temp_atk_1) !=0) and (int(temp_atk_2) !=0) ):
            if (len(suitable_id) != 0): 
                    temp_suitable_id = suitable_id.copy()
                    suitable_id.clear()
                    for j in range(len(temp_suitable_id)):
                       if ((int(temp_atk_1) <= data['Atk'][temp_suitable_id[j]]) and (int(temp_atk_2) >= data['Atk'][temp_suitable_id[j]])) :
                                suitable_id.append(temp_suitable_id[j])         
                    if (len(suitable_id) ==0):
                        stop_flag = True        
            else:
                for i in range(len(data)):
                    if ((int(temp_atk_1) <= int(data['Atk'][i])) and (int(temp_atk_2) >= int(data['Atk'][i]))) :
                        suitable_id.append(i)
                if (len(suitable_id) ==0):
                       stop_flag = True        
        
    if (stop_flag == False):
        if ((int(temp_def_1) !=0) and (int(temp_def_2) !=0) ):
            if (len(suitable_id) != 0):
                    temp_suitable_id.clear()
                    temp_suitable_id = suitable_id.copy()
                    suitable_id.clear()
                    for j in range(len(temp_suitable_id)):
                        if ((int(temp_def_1) <= data['Def'][temp_suitable_id[j]]) and (int(temp_def_2) >= data['Def'][temp_suitable_id[j]])) :
                                suitable_id.append(temp_suitable_id[j])       
                    if (len(suitable_id) ==0):
                        stop_flag = True        
            else:
                for i in range(len(data)):
                    if ((int(temp_def_1) <= int(data['Def'][i])) and (int(temp_def_2) >= int(data['Def'][i]))) :
                        suitable_id.append(i)            
                if (len(suitable_id) ==0):
                       stop_flag = True
    
    if (stop_flag == False):
        if ((int(temp_spa_1) !=0) and (int(temp_spa_2) !=0) ):
            if (len(suitable_id) != 0):
                    temp_suitable_id.clear()
                    temp_suitable_id = suitable_id.copy()
                    suitable_id.clear()
                    for j in range(len(temp_suitable_id)):
                        if ((int(temp_spa_1) <= data['SpA'][temp_suitable_id[j]]) and (int(temp_spa_2) >= data['SpA'][temp_suitable_id[j]])) :
                                suitable_id.append(temp_suitable_id[j])       
                    if (len(suitable_id) ==0):
                        stop_flag = True        
            else:
                for i in range(len(data)):
                    if ((int(temp_spa_1) <= int(data['SpA'][i])) and (int(temp_spa_2) >= int(data['SpA'][i]))) :
                        suitable_id.append(i)            
                if (len(suitable_id) ==0):
                       stop_flag = True
    
    if (stop_flag == False):
        if ((int(temp_spd_1) !=0) and (int(temp_spd_2) !=0) ):
            if (len(suitable_id) != 0):
                    temp_suitable_id.clear()
                    temp_suitable_id = suitable_id.copy()
                    suitable_id.clear()
                    for j in range(len(temp_suitable_id)):
                        if ((int(temp_spd_1) <= data['SpD'][temp_suitable_id[j]]) and (int(temp_spd_2) >= data['SpD'][temp_suitable_id[j]])) :
                                suitable_id.append(temp_suitable_id[j])        
                    if (len(suitable_id) ==0):
                        stop_flag = True        
            else:
                for i in range(len(data)):
                    if ((int(temp_spd_1) <= int(data['SpD'][i])) and (int(temp_spd_2) >= int(data['SpD'][i]))) :
                        suitable_id.append(i)            
                if (len(suitable_id) ==0):
                       stop_flag = True
                       
    if (stop_flag == False):
        if ((int(temp_spe_1) !=0) and (int(temp_spe_2) !=0) ):
            if (len(suitable_id) != 0):
                    temp_suitable_id.clear()
                    temp_suitable_id = suitable_id.copy()
                    suitable_id.clear()
                    for j in range(len(temp_suitable_id)):
                        if ((int(temp_spe_1) <= data['Spe'][temp_suitable_id[j]]) and (int(temp_spe_2) >= data['Spe'][temp_suitable_id[j]])) :
                                suitable_id.append(temp_suitable_id[j])       
                    if (len(suitable_id) ==0):
                        stop_flag = True        
            else:
                for i in range(len(data)):
                    if ((int(temp_spe_1) <= int(data['Spe'][i])) and (int(temp_spe_2) >= int(data['Spe'][i]))) :
                        suitable_id.append(i)            
                if (len(suitable_id) ==0):
                       stop_flag = True
                       
    if (stop_flag == False):
        if ((int(temp_type1_1) !=0) and (int(temp_type1_2) !=0) ):
            if (len(suitable_id) != 0):
                    temp_suitable_id.clear()
                    temp_suitable_id = suitable_id.copy()
                    suitable_id.clear()
                    for j in range(len(temp_suitable_id)):
                        if ((int(temp_type1_1) <= data['Type I'][temp_suitable_id[j]]) and (int(temp_type1_2) >= data['Type I'][temp_suitable_id[j]])) :
                                suitable_id.append(temp_suitable_id[j])       
                    if (len(suitable_id) ==0):
                        stop_flag = True        
            else:
                for i in range(len(data)):
                    if ((int(temp_type1_1) <= int(data['Type I'][i])) and (int(temp_type1_2) >= int(data['Type I'][i]))) :
                        suitable_id.append(i)            
                if (len(suitable_id) ==0):
                       stop_flag = True      
    
    if (stop_flag == False):
        if ((int(temp_type2_1) !=0) and (int(temp_type2_2) !=0) ):
            if (len(suitable_id) != 0):
                    temp_suitable_id.clear()
                    temp_suitable_id = suitable_id.copy()
                    suitable_id.clear()
                    for j in range(len(temp_suitable_id)):
                        if ((int(temp_type2_1) <= data['Type II'][temp_suitable_id[j]]) and (int(temp_type2_2) >= data['Type II'][temp_suitable_id[j]])) :
                                suitable_id.append(temp_suitable_id[j])       
                    if (len(suitable_id) ==0):
                        stop_flag = True        
            else:
                for i in range(len(data)):
                    if ((int(temp_type2_1) <= int(data['Type II'][i])) and (int(temp_type2_2) >= int(data['Type II'][i]))) :
                        suitable_id.append(i)            
                if (len(suitable_id) ==0):
                       stop_flag = True     
    
    if (stop_flag == False):
        if ((int(temp_ability1_1) !=0) and (int(temp_ability1_2) !=0) ):
            if (len(suitable_id) != 0):
                    temp_suitable_id.clear()
                    temp_suitable_id = suitable_id.copy()
                    suitable_id.clear()
                    for j in range(len(temp_suitable_id)):
                        if ((int(temp_ability1_1) <= data['Ability I'][temp_suitable_id[j]]) and (int(temp_ability1_2) >= data['Ability I'][temp_suitable_id[j]])) :
                                suitable_id.append(temp_suitable_id[j])       
                    if (len(suitable_id) ==0):
                        stop_flag = True        
            else:
                for i in range(len(data)):
                    if ((int(temp_ability1_1) <= int(data['Ability I'][i])) and (int(temp_ability1_2) >= int(data['Ability I'][i]))) :
                        suitable_id.append(i)            
                if (len(suitable_id) ==0):
                       stop_flag = True       
                          
    if (stop_flag == False):
        if ((int(temp_ability2_1) !=0) and (int(temp_ability2_2) !=0) ):
            if (len(suitable_id) != 0):
                    temp_suitable_id.clear()
                    temp_suitable_id = suitable_id.copy()
                    suitable_id.clear()
                    for j in range(len(temp_suitable_id)):
                        if ((int(temp_ability2_1) <= data['Ability II'][temp_suitable_id[j]]) and (int(temp_ability2_2) >= data['Ability II'][temp_suitable_id[j]])) :
                                suitable_id.append(temp_suitable_id[j])        
                    if (len(suitable_id) ==0):
                        stop_flag = True        
            else:
                for i in range(len(data)):
                    if ((int(temp_ability2_1) <= int(data['Ability II'][i])) and (int(temp_ability2_2) >= int(data['Ability II'][i]))) :
                        suitable_id.append(i)            
                if (len(suitable_id) ==0):
                       stop_flag = True    
                                          
    if (stop_flag == False):
        if ((int(temp_hidden_ability_1) !=0) and (int(temp_hidden_ability_2) !=0) ):
            if (len(suitable_id) != 0):
                    temp_suitable_id.clear()
                    temp_suitable_id = suitable_id.copy()
                    suitable_id.clear()
                    for j in range(len(temp_suitable_id)):
                        if ((int(temp_hidden_ability_1) <= data['Hidden Ability'][temp_suitable_id[j]]) and (int(temp_hidden_ability_2) >= data['Hidden Ability'][temp_suitable_id[j]])) :
                                suitable_id.append(temp_suitable_id[j])        
                    if (len(suitable_id) ==0):
                        stop_flag = True        
            else:
                for i in range(len(data)):
                    if ((int(temp_hidden_ability_1) <= int(data['Hidden Ability'][i])) and (int(temp_hidden_ability_2) >= int(data['Hidden Ability'][i]))) :
                        suitable_id.append(i)            
                if (len(suitable_id) ==0):
                       stop_flag = True               
                       
    if (stop_flag == False):
        if ((int(temp_egg1_1) !=0) and (int(temp_egg1_2) !=0) ):
            if (len(suitable_id) != 0):
                    temp_suitable_id.clear()
                    temp_suitable_id = suitable_id.copy()
                    suitable_id.clear()
                    for j in range(len(temp_suitable_id)):
                        if ((int(temp_egg1_1) <= data['Egg Group I'][temp_suitable_id[j]]) and (int(temp_egg1_2) >= data['Egg Group I'][temp_suitable_id[j]])) :
                                suitable_id.append(temp_suitable_id[j])        
                    if (len(suitable_id) ==0):
                        stop_flag = True        
            else:
                for i in range(len(data)):
                    if ((int(temp_egg1_1) <= int(data['Egg Group I'][i])) and (int(temp_egg1_2) >= int(data['Egg Group I'][i]))) :
                        suitable_id.append(i)            
                if (len(suitable_id) ==0):
                       stop_flag = True   
                                       
    if (stop_flag == False):
        if ((int(temp_egg2_1) !=0) and (int(temp_egg2_2) !=0) ):
            if (len(suitable_id) != 0):
                    temp_suitable_id.clear()
                    temp_suitable_id = suitable_id.copy()
                    suitable_id.clear()
                    for j in range(len(temp_suitable_id)):
                        if ((int(temp_egg2_1) <= data['Egg Group II'][temp_suitable_id[j]]) and (int(temp_egg2_2) >= data['Egg Group II'][temp_suitable_id[j]])) :
                                suitable_id.append(temp_suitable_id[j])       
                    if (len(suitable_id) ==0):
                        stop_flag = True        
            else:
                for i in range(len(data)):
                    if ((int(temp_egg2_1) <= int(data['Egg Group II'][i])) and (int(temp_egg2_2) >= int(data['Egg Group II'][i]))) :
                        suitable_id.append(i)            
                if (len(suitable_id) ==0):
                       stop_flag = True
        temp_data_pd = pd.DataFrame()
    output_file_name ="C:/Work/Output/" + entry.get()
    
    db_id = pd.read_excel('C:/Work/Data/Pdx.xlsx',sheet_name='Sheet1',index_col=0)
    id_list = list(db_id.values)
    
    if (len(suitable_id)!= 0):
        for element in suitable_id:
            
            pokemon2 = pd.Series([id_list[element][0],id_list[element][1],id_list[element][2],id_list[element][3],id_list[element][4],id_list[element][5],id_list[element][6],id_list[element][7],id_list[element][8],id_list[element][9],id_list[element][10],id_list[element][11],id_list[element][12]], index=["HP","Atk","Def","SpA","SpD","Spe","Type I","Type II","Ability I","Ability II","Hidden Ability","Egg Group I","Egg Group II"])
            temp_data_pd=temp_data_pd.append(pokemon2,ignore_index=True)
            
        temp_data_pd.to_excel(output_file_name)
    
win1 = tki.Tk()
win1.title('Добавление покемона')
win1.geometry('800x600+300+200')
lbl_3 = tki.Label(win1, text = 'Введите характеристики для отбора покемонов', font = ('Times', 12))
lbl_3.place(x = 10, y = 0)
lbl_7 = tki.Label(win1, text = 'Введите название файла для вывода :', font = ('Times', 12))
lbl_7.place(x = 400, y = 280)

entry = tki.Entry(win1)
entry.focus()
entry.place(x = 400, y = 300)

lbl_type = tki.Label(win1, text = 'TypeI и TypeII не должны совпадать!', font = ('Times', 10), fg='red')
lbl_abl12 = tki.Label(win1, text = 'AbilityI и AbilityII не должны совпадать!', font = ('Times', 10), fg='red')
lbl_abl23 = tki.Label(win1, text = 'HiddenAbility и AbilityII не должны совпадать!', font = ('Times', 10), fg='red')
lbl_abl13 = tki.Label(win1, text = 'HiddenAbility и AbilityI не должны совпадать!', font = ('Times', 10), fg='red')
lbl_egg = tki.Label(win1, text = 'Egg Group I и Egg Group II не должны совпадать!', font = ('Times', 10), fg='red')
lbl_HI =  tki.Label(win1, text = 'Неверный интервал значений!', font = ('Times', 10), fg='red')
l=0
for i in db_3.columns[:6]:
    lbl_5 = tki.Label(win1, text = i+' от ', font = ('Times', 12))
    lbl_5.place(x = 10, y = 30+40*l)
    lbl_6 = tki.Label(win1, text =' до ', font = ('Times', 12))
    lbl_6.place(x = 280, y = 30+40*l)
    l+=1
    
for i in db_3.columns[6:]:
    lbl_5 = tki.Label(win1, text = i, font = ('Times', 12))
    lbl_5.place(x = 10, y = 30+40*l)
    l+=1
    
var = []

for i in range(len(db_3.columns[:6])):
    scale = tki.Scale(win1, orient= tki.HORIZONTAL, from_=min(list(db_3[db_3.columns[i]])), to=max(list(db_3[db_3.columns[i]])), resolution= 1)
    var.append(scale)
    scale.place(x = 100, y = 20+40*i, width = 150, height = 50)
    scale_ = tki.Scale(win1, orient= tki.HORIZONTAL, from_=min(list(db_3[db_3.columns[i]])), to=max(list(db_3[db_3.columns[i]])), resolution= 1)
    var.append(scale_)
    scale_.place(x = 350, y = 20+40*i, width = 150, height = 50)



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

btn_7 = tki.Button(win1, text = "Сохранить!", font = ('Times', 12), command = clck)
btn_7.place(x = 540, y = 540, width =200, height = 35)

win1.mainloop()