"""
Created on Thu May 20 15:24:40 2021

@author: Richard-Teaman l1
"""

import pandas as pd
data = pd.read_excel('C:/Work/Data/Pokname.xlsx')
data_2 = pd.read_excel('C:/Work/Data/Pdx.xlsx')

pokemon_to_find = input("Найти: ")

input_int_flag = True
try :
    int(pokemon_to_find)
except ValueError:
    input_int_flag = False
    

if (input_int_flag == False):
    for i in range(len(data)):
        temp_str = data['Pokemon'][i]
        if ((pokemon_to_find.upper() in temp_str.upper()) == True):
            found_pokemon_id = i
            print(data['Pokemon'][found_pokemon_id],":")
            print("ID: " + str(found_pokemon_id))  # Вывод лучше оставил здесь, так как если несколько покемонов нашло,то их всех нужно вывести/запомнить

if (input_int_flag == True):
    if int(pokemon_to_find) < len(data):
            found_pokemon_id = int(pokemon_to_find)-1
            print(data['Pokemon'][found_pokemon_id])