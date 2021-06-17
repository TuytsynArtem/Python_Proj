
import pandas as pd
data = pd.read_excel('C:/Work/Data/Pdx.xlsx',sheet_name='Sheet1')
def sortirovka(temp_hp_1,temp_hp_2,temp_atk_1,temp_atk_2,temp_def_1,temp_def_2,
               temp_spa_1,temp_spa_2,temp_spd_1,temp_spd_2,temp_spe_1,
               temp_spe_2,temp_type1_1,temp_type2_1,
               temp_ability1_1,temp_ability2_1,
               temp_hidden_ability_1,temp_egg1_1,temp_egg2_1):
    # print("Введите диапазон HP")
    # temp_hp_1=input()
    # temp_hp_2=input()
    # print("Введите диапазон Atk")
    # temp_atk_1=input()
    # temp_atk_2=input()
    # print("Введите диапазон Def")
    # temp_def_1=input()
    # temp_def_2=input()
    # print("Введите диапазон SpA")
    # temp_spa_1=input()
    # temp_spa_2=input()
    # print("Введите диапазон SpD")
    # temp_spd_1=input()
    # temp_spd_2=input()
    # print("Введите диапазон Spe")
    # temp_spe_1=input()
    # temp_spe_2=input()
    # print("Введите диапазон Type I")
    # temp_type1_1=input()
    temp_type1_2=temp_type1_1
    # print("Введите диапазон Type II")
    # temp_type2_1=input()
    temp_type2_2=temp_type2_1
    # print("Введите диапазон Ability I")
    # temp_ability1_1=input()
    temp_ability1_2=temp_ability1_1
    # print("Введите диапазон Ability II")
    # temp_ability2_1=input()
    temp_ability2_2=temp_ability2_1
    # print("Введите  диапазон Hidden Ability")
    # temp_hidden_ability_1=input()
    temp_hidden_ability_2=temp_hidden_ability_1
    # print("Введите диапазон Egg  Group I")
    # temp_egg1_1=input()
    temp_egg1_2= temp_egg1_1
    # print("Введите диапазон Egg Gruop II")
    # temp_egg2_1=input()
    temp_egg2_2=temp_egg2_1
    
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
                       
    print(suitable_id)
    
    
        
    temp_data_pd = pd.DataFrame()
    print("введи название файла для вывода ")
    output_file_name ="C:/Work/Data/" + input() +".xlsx"
    
    print(output_file_name)
    
    db_id = pd.read_excel('C:/Work/Data/Pdx.xlsx',sheet_name='Sheet1',index_col=0)
    id_list = list(db_id.values)
    
    if (len(suitable_id)!= 0):
        for element in suitable_id:
            
            pokemon2 = pd.Series([id_list[element][0],id_list[element][1],id_list[element][2],id_list[element][3],id_list[element][4],id_list[element][5],id_list[element][6],id_list[element][7],id_list[element][8],id_list[element][9],id_list[element][10],id_list[element][11],id_list[element][12]], index=["HP","Atk","Def","SpA","SpD","Spe","Type I","Type II","Ability I","Ability II","Hidden Ability","Egg Group I","Egg Group II"])
            temp_data_pd=temp_data_pd.append(pokemon2,ignore_index=True)
            
        temp_data_pd.to_excel(output_file_name)
    


