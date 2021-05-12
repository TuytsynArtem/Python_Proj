# -*- coding: utf-8 -*-
"""
Created on Tue May  4 19:34:32 2021

@author: User
"""
import pandas as pd
import random
import matplotlib.pyplot as plt
# import mathplotlib as plt
#import pprint as pp
data = pd.read_excel('C:/Work/Data/pdx.xlsx',sheet_name='Sheet1',index_col=0)
eggs_connection = pd.read_excel('C:/Work/Data/eggs_connection.xlsx',sheet_name='Лист1',index_col=0)

one,two,kolvo=int(input("Введите 1-ое id: ")),int(input("Введите 2-ое id: ")),int(input("Введите количество размножений для анализа вероятностей: "))
def proverka(a_1,b_1):
    '''
    Parameters
    ----------
    a : TYPE Integer
        id of egg group
    b : TYPE Integer
        id of egg group

    Returns 1
    -------
    None.

    '''
    if eggs_connection[a_1][b_1]==1:
        return 1
    return 0
def cheker(id1,id2,d_b):
    '''
    Parameters
    ----------
    id1 : TYPE Integer
        id of pokemon
    id2 : TYPE Integer
        id of pokemon
    d_b : TYPE DataFrame
        database of pokemons
    Returns True
    -------
    False.

    '''
    if(d_b["Egg Group I"][id1]!="-" and d_b["Egg Group II"][id1]!="-"):
        print(d_b["Egg Group II"][id2])

        if(d_b["Egg Group I"][id2]!="-" and d_b["Egg Group II"][id2]!="-"):
            if((  proverka(d_b["Egg Group I"][id1],d_b["Egg Group I"][id2])
                 +proverka(d_b["Egg Group I"][id1],d_b["Egg Group II"][id2])
                 +proverka(d_b["Egg Group II"][id1],d_b["Egg Group I"][id2])
                 +proverka(d_b["Egg Group II"][id1],d_b["Egg Group II"][id2]))>0):
                return True

        elif(d_b["Egg Group I"][id2]!="-" and d_b["Egg Group II"][id2]=="-"):
            if((  proverka(d_b["Egg Group I"][id1],d_b["Egg Group I"][id2])
                 +proverka(d_b["Egg Group II"][id1],d_b["Egg Group I"][id2]))>0):
                return True

    elif(d_b["Egg Group I"][id1]!="-" and d_b["Egg Group II"][id1]=="-"):

        if(d_b["Egg Group I"][id2]!="-" and d_b["Egg Group II"][id2]!="-"):
            if((  proverka(d_b["Egg Group I"][id1],d_b["Egg Group I"][id2])
                 +proverka(d_b["Egg Group I"][id1],d_b["Egg Group II"][id2]))>0):
                return True

        elif(d_b["Egg Group I"][id2]!="-" and d_b["Egg Group II"][id2]=="-"):
            if (proverka(d_b["Egg Group I"][id1],d_b["Egg Group I"][id2]))>0:
                return True

    return False
def analyze(spisok):
    t1 = {}
    t2 = {}
    for i in range(0,len(spisok)):
        if i%2>0:
            if t1.get(spisok[i])!=None:
                t1[spisok[i]]+=1
            else:
                t1[spisok[i]]=1
        else:
            # if t2[spisok[i]].get(key[,default])!=None:
            if t2.get(spisok[i])!=None:
                t2[spisok[i]]+=1
            else:
                t2[spisok[i]]=1
    print(t1)
    klv = t1.keys()
    print(klv)
    znch = t1.values()
    print(znch)
    plt.pie(klv,labels=znch,autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('equal')
    plt.title("Percentage of Different Types of Pokemon")
    plt.plot()
    fig=plt.gcf()
    fig.set_size_inches(7,7)
    plt.show()
    
    
    
    
            
            
            
            
            
            
        
        
        
def Reproduction(raz,dva,baza,kolvo):
    for i in range(kolvo):
        typelist = []
        pokemons = []
        flag = True
        if baza["Type I"][raz]!="nan":
            typelist.append(baza["Type I"][raz])
        
        if baza["Type II"][raz]!="nan":
            typelist.append(baza["Type II"][raz])
        
        if baza["Type I"][dva]!="nan":
            for i in typelist:
                if i == baza["Type I"][dva]:
                    flag = False
            if flag:
                typelist.append(baza["Type I"][dva])
                
                    
        flag = True
                
        if baza["Type II"][dva]!="nan":
            
             for i in typelist:
                if i == baza["Type II"][dva]:
                    flag = False
             if flag:
                 typelist.append(baza["Type II"][dva])
            
        if len(typelist) == 1:
            pokemons.append(typelist[0])
            if random.random() == 1: 
                pokemons.append(typelist[0])
            else:
                pokemons.append("no Type")
                
        elif len(typelist) == 2:
            if random.random() == 1: 
                pokemons.append(typelist[0])
            else:
                pokemons.append(typelist[1])
            r = random.randint(0,2)
            if r == 0: 
                pokemons.append(typelist[0])
            elif r == 1:
                pokemons.append(typelist[1])
            elif r == 2:
                pokemons.append("no Type")
            
            
            
        elif len(typelist) == 3:
            r = random.randint(0,2)
            if r == 0: 
                pokemons.append(typelist[0])
            elif r == 1:
                pokemons.append(typelist[1])
            elif r == 2:
                pokemons.append(typelist[2])
            r = random.randint(0,3)
            if r == 0: 
                pokemons.append(typelist[0])
            elif r == 1:
                pokemons.append(typelist[1])
            elif r == 2:
                pokemons.append(typelist[2])
            elif r == 3:
                pokemons.append("no Type")
            
            
        elif len(typelist) == 4:
            r = random.randint(0,3)
            if r == 0: 
                pokemons.append(typelist[0])
            elif r == 1:
                pokemons.append(typelist[1])
            elif r == 2:
                pokemons.append(typelist[2])
            elif r == 3:
                pokemons.append("no Type")
            r = random.randint(0,3)
            if r == 0: 
                pokemons.append(typelist[0])
            elif r == 1:
                pokemons.append(typelist[1])
            elif r == 2:
                pokemons.append(typelist[2])
            elif r == 3:
                pokemons.append(typelist[3])
            elif r == 3:
                pokemons.append("no Type")
    analyze(pokemons)

            
        
        
    
    
    
    
if cheker(one,two,data):
    print("размножение возможно:")
    Reproduction(one,two,data,kolvo)

else:
    print("размножение невозможно:")
