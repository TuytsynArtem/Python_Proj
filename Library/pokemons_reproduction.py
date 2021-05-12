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

def avrstats(listok,bz):
    print("hfersguyvfgjivgbhiewb")
    HP=0
    aHP=0
    Atk=0
    aAtk=0
    Def=0
    aDef=0
    SpA =0
    aSpA=0
    SpD=0
    aSpD=0
    Spe=0
    aSpe=0

    podhodyat = {}
    for i in range (1,664):
        j=0
        while j<len(listok):
            if bz["Type I"][i]==listok[j] and bz["Type II"][i]==listok[j+1]:
                if podhodyat.get(i)==None:
                    podhodyat[i]=0
            j+=2
    for i in list(podhodyat):
        HP += bz["HP"][i]
        aHP +=1
        aHP =HP/aHP
        
        Atk += bz["Atk"][i]
        aAtk +=1
        aAtk =Atk/aAtk
        
        Def += bz["Def"][i]
        aDef +=1
        aDef =Def/aDef
        
        SpA += bz["SpA"][i]
        aSpA +=1
        aSpA =SpA/aSpA
        
        SpD += bz["SpD"][i]
        aSpD +=1
        aSpD =SpD/aSpD
        
        Spe += bz["Spe"][i]
        aSpe +=1
        aSpe =Spe/aSpe
    arr = [aHP,aAtk,aDef,aSpA,aSpD,aSpe]
    arr2 = ["aHP","aAtk","aDef","aSpA","aSpD","aSpe"]
    
    fig = plt.figure()
    a_x = fig.add_axes([0,0,1,1])
    a_x.bar(arr2,arr)
    fig.set_figwidth(16)
    plt.show()
     
        
      
        
        
            
def analyze(spisok):
    t1 = {}
    t2 = {}
    for i in range(0,len(spisok)):
        if i%2>0:
            if t2.get(spisok[i])!=None:
                t2[spisok[i]]+=1
            else:
                t2[spisok[i]]=1
        else:
            if t1.get(spisok[i])!=None:
                t1[spisok[i]]+=1
            else:
                t1[spisok[i]]=1
    eggs_data = pd.read_excel('C:/Work/Data/Types.xlsx',sheet_name='Лист1',index_col=0)
    
    klv = list(t1.keys())
    for i in range(0,len(klv)):
        # print(i)
        klv[i]=eggs_data["Type_name"][klv[i]]
        
    znch = list(t1.values())
    
    klv2 = list(t2.keys())
    for i in range(0,len(klv2)):
        if  klv2[i]!=0:
            klv2[i]=eggs_data["Type_name"][klv2[i]]
        else:
            klv2[i]="No Type"
         
        
    znch2 = list(t2.values())
    # print(t1)
    # print(t2)
    
    # print(klv)
    
    # print(znch)
    plt.pie(znch,labels=klv,autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('equal')
    plt.title("Percentage of Different Types I of Pokemon")
    plt.plot()
    fig=plt.gcf()
    fig.set_size_inches(7,7)
    plt.show()
    
    plt.pie(znch2,labels=klv2,autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('equal')
    plt.title("Percentage of Different Types II of Pokemon")
    plt.plot()
    fig=plt.gcf()
    fig.set_size_inches(7,7)
    plt.show()
    
    
    
    
            
            
            
            
            
            
        
        
        
def Reproduction(raz,dva,baza,kolvo):   
    
    typelist = []
    pokemons = []
    flag = True
    # print(baza["Type I"][raz])
    # print(baza["Type II"][raz])
    # print(baza["Type I"][dva])
    # print(baza["Type II"][dva])
    
    typelist.append(baza["Type I"][raz])
    
    if baza["Type II"][raz]!=0:
        typelist.append(baza["Type II"][raz])
    
    if baza["Type I"][dva]!=0:
        for i in typelist:
            if i == baza["Type I"][dva]:
                flag = False
        if flag:
            typelist.append(baza["Type I"][dva])
            
                
    flag = True
            
    if baza["Type II"][dva]!=0:
        
         for i in typelist:
            if i == baza["Type II"][dva]:
                flag = False
         if flag:
             typelist.append(baza["Type II"][dva])
                 
    for i in range(kolvo):    
        if len(typelist) == 1:
            pokemons.append(typelist[0])
            r = random.randint(0,1)
            if r == 1: 
                pokemons.append(typelist[0])
            else:
                pokemons.append(0)
                
        elif len(typelist) == 2:
            r = random.randint(0,1)
            if  r == 1: 
                pokemons.append(typelist[0])
            else:
                pokemons.append(typelist[1])
                
                
            r = random.randint(0,2)
            
            if r == 0: 
                pokemons.append(typelist[0])
            elif r == 1:
                pokemons.append(typelist[1])
            elif r == 2:
                pokemons.append(0)
                
            
            
            
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
                pokemons.append(0)
            
            
        elif len(typelist) == 4:
            r = random.randint(0,3)
            if r == 0: 
                pokemons.append(typelist[0])
            elif r == 1:
                pokemons.append(typelist[1])
            elif r == 2:
                pokemons.append(typelist[2])
            elif r == 3:
                pokemons.append(typelist[3])
                
            r = random.randint(0,4)
            if r == 0: 
                pokemons.append(typelist[0])
            elif r == 1:
                pokemons.append(typelist[1])
            elif r == 2:
                pokemons.append(typelist[2])
            elif r == 3:
                pokemons.append(typelist[3])
            elif r == 4:
                pokemons.append(0)
    # print(typelist)
    # print(pokemons)
    analyze(pokemons)
    avrstats(pokemons,baza)

            
        
        
    
    
    
    
if cheker(one,two,data):
    print("размножение возможно:")
    Reproduction(one,two,data,kolvo)

else:
    print("размножение невозможно:")
