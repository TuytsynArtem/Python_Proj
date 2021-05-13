# -*- coding: utf-8 -*-
"""
Created on Tue May  4 19:34:32 2021

@author: User
"""
import random
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel('C:/Work/Data/pdx.xlsx',sheet_name='Sheet1',index_col=0)
eggs_connection = pd.read_excel('C:/Work/Data/eggs_connection.xlsx',sheet_name='Лист1',index_col=0)

one,two=int(input("Введите 1-ое id: ")),int(input("Введите 2-ое id: "))
kolvo=int(input("Введите количество размножений для анализа вероятностей: "))
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
def avrstats(listok,b_z):
    '''
    Parameters
    ----------
    listok : TYPE Array
        list of pokemons type
    d_z : TYPE DataFrame
        database of pokemons
    Returns True
    -------
    False.

    '''
    stats = [0,0,0,0,0,0]
    avr = 0
    podhodyat = {}
    for i in range (1,664):
        j=0
        while j<len(listok):
            if b_z["Type I"][i]==listok[j] and b_z["Type II"][i]==listok[j+1]:
                if podhodyat.get(i) is None:
                    podhodyat[i]=0
            j+=2
    for i in list(podhodyat):
        stats[0] += b_z["HP"][i]
        stats[1] += b_z["Atk"][i]
        stats[2] += b_z["Def"][i]
        stats[3] += b_z["SpA"][i]
        stats[4] += b_z["SpD"][i]
        stats[5] += b_z["Spe"][i]
        avr +=1
    arr = [stats[0]/avr,stats[1]/avr,stats[2]/avr,stats[3]/avr,stats[4]/avr,stats[0]/avr]
    arr2 = ["HP","Atk","Def","SpA","SpD","Spe"]
    fig = plt.figure()
    a_x = fig.add_axes([0,0,1,1])
    a_x.bar(arr2,arr)
    fig.set_figwidth(16)
    plt.title("Average Stats")
    plt.show()
def analyze(spisisok):
    '''
    Parameters
    ----------
    spisisok : TYPE Array
        list of pokemons type
    Returns True
    -------
    False.

    '''
    t_1 = {}
    t_2 = {}
    for i,spis in enumerate(spisisok):
        if i%2>0:
            if t_2.get(spis) is not None:
                t_2[spis]+=1
            else:
                t_2[spis]=1
        else:
            if t_1.get(spis) is not None:
                t_1[spis]+=1
            else:
                t_1[spis]=1
    eggs_data = pd.read_excel('C:/Work/Data/Types.xlsx',sheet_name='Лист1',index_col=0)
    klv = list(t_1.keys())
    for i,klvshka in enumerate(klv):
        klv[i]=eggs_data["Type_name"][klvshka]
    znch = list(t_1.values())
    klv2 = list(t_2.keys())
    for i,klvshka2 in enumerate(klv2):
        if  klvshka2!=0:
            klv2[i]=eggs_data["Type_name"][klvshka2]
        else:
            klv2[i]="No Type"
    znch2 = list(t_2.values())
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
def reproduction(raz,dva,baza,kol):
    '''
    Parameters
    ----------
    raz : TYPE Integer
        id of pokemon
    dva : TYPE Integer
        id of pokemon
    baza : TYPE DataFrame
        database of pokemons
    kol : TYPE Integer
    ammount of cicle
    Returns True
    -------
    False.

    '''
    typelist = []
    pokemons = []
    flag = True
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
    for i in range(kol):
        r_r = random.randint(0,len(typelist)-1)
        pokemons.append(typelist[r_r])
        promejutok = r_r
        while r_r == promejutok:
            r_r = random.randint(0,len(typelist))
        if r_r == 0:
            pokemons.append(typelist[0])
        elif r_r == len(typelist):
            pokemons.append(0)
        else:
            pokemons.append(typelist[r_r])
    analyze(pokemons)
    avrstats(pokemons,baza)
if cheker(one,two,data):
    print("размножение возможно:")
    reproduction(one,two,data,kolvo)
else:
    print("размножение невозможно:")
