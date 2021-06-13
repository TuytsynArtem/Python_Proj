# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 19:00:44 2021

@author: User
"""
import pandas as pd
def new_pokemon(name,HP,Atk,Def,SpA,SpD,Spe,TypeI,TypeII,AbilityI,AbilityII,HiddenAbility,EggGroupI,EggGroupII):
    data = pd.read_excel('C:/Work/Data/pdx.xlsx',sheet_name='Sheet1',index_col=0)
    dataname =  pd.read_excel('C:/Work/Data/Pokname.xlsx',sheet_name='Sheet1',index_col=0)
    
    # pokemon = pd.DataFrame({"HP","Atk","Def","SpA","SpD","Spe","Type I","Type II","Ability I","Ability II"
    #                        ,"Hidden Ability","Mass","Color","Gender","EggGroup I","EggGroup II"})
    
    pokemon2 = pd.Series([HP,Atk,Def,SpA,SpD,Spe,TypeI,TypeII,AbilityI,AbilityII,
                          HiddenAbility,EggGroupI,EggGroupII], 
                          index=["HP","Atk","Def","SpA","SpD","Spe","Type I","Type II","Ability I","Ability II"
                          ,"Hidden Ability","Egg Group I","Egg Group II"])
    pokemon3 = pd.Series([name],index = ["Name"])
    
    dataname=dataname.append(pokemon3,ignore_index=True)
    
    data=data.append(pokemon2,ignore_index=True)
    dataname.to_excel("C:/Work/Data/Pokname.xlsx")
    data.to_excel("C:/Work/Data/pdx.xlsx")
    
def delete_pokemon(name):
    data = pd.read_excel('C:/Work/Data/pokname.xlsx',sheet_name='Sheet1',index_col=0)
    a = data.index[data.Name == name]
    print(a)
    # data = data.drop(data[data.score == name].index)
    # data = data.drop(index = [a])
    

