# -*- coding: utf-8 -*-
"""
Created on Tue May  4 19:34:32 2021

@author: User
"""
import random
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import matplotlib.pyplot as plt
from plot import save,pie



data = pd.read_excel('C:/Work/Data/pdx.xlsx',sheet_name='Sheet1',index_col=0)
eggs_connection = pd.read_excel('C:/Work/Data/eggs_connection.xlsx',sheet_name='Лист1',index_col=0)
max_id = max(data.index)



# one,two=int(input("Введите 1-ое id: ")),int(input("Введите 2-ое id: "))
# kolvo=int(input("Введите количество размножений для анализа вероятностей: "))


def graphs(fig,win):
    '''
    Parameters
    ----------
    fig : TYPE list
        item of list of figures
    win : TYPE Tk
        window
    -------
    '''
    canvas = FigureCanvasTkAgg(fig, win)
    canvas.draw()
    canvas.get_tk_widget().place(x = 10, y = 10, width = 340, height = 250)

def reproduction(raz,dva,baza,kol):
    '''
    Parameters
    ----------
    raz : TYPE Integer
        id of pokemon
    dva : TYPE Integer
        id of pokemon
    baza : TYPE DataFrame
        database of pok_typelist
    kol : TYPE Integer
    ammount of cicle
    Returns array
    -------

    '''
    hidden = []
    pok_hidden = []
    abilities_pok = []
    pok_abilities = []
    typelist = []
    pok_typelist = []
    flag = True
    hidden.append(baza["Hidden Ability"][raz])
    if baza["Hidden Ability"][raz]!=baza["Hidden Ability"][dva]:
        hidden.append(baza["Hidden Ability"][dva])
    abilities_pok.append(baza["Ability I"][raz])
    if baza["Ability II"][raz]!=0:
        abilities_pok.append(baza["Ability II"][raz])
    if baza["Ability I"][dva]!=0:
        for i in abilities_pok:
            if i == baza["Ability I"][dva]:
                flag = False
        if flag:
            abilities_pok.append(baza["Ability I"][dva])
    flag = True
    if baza["Ability II"][dva]!=0:
        for i in abilities_pok:
            if i == baza["Ability II"][dva]:
                flag = False
        if flag:
            abilities_pok.append(baza["Ability II"][dva])
    for i in range(kol):
        randnum = random.randint(0,len(abilities_pok)-1)
        pok_abilities.append(abilities_pok[randnum])
        promejutok = randnum
        while randnum == promejutok:
            randnum = random.randint(0,len(abilities_pok))
        if randnum == 0:
            pok_abilities.append(abilities_pok[0])
        elif randnum == len(abilities_pok):
            pok_abilities.append(0)
        else:
            pok_abilities.append(abilities_pok[randnum])
        randnum = random.randint(0,len(hidden)-1)
        pok_hidden.append(hidden[randnum])
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
        randnum = random.randint(0,len(typelist)-1)
        pok_typelist.append(typelist[randnum])
        promejutok = randnum
        while randnum == promejutok:
            randnum = random.randint(0,len(typelist))
        if randnum == 0:
            pok_typelist.append(typelist[0])
        elif randnum == len(typelist):
            pok_typelist.append(0)
        else:
            pok_typelist.append(typelist[randnum])
    boxplot()
    return (analyze(pok_typelist,pok_abilities,pok_hidden)+
            avrstats(pok_typelist,baza)+raspredelenie(typelist))

def analyze(tipes,abilki,pryatki):
    '''
    Parameters
    ----------
    tipes : TYPE Array
        list of pok_typelist type
    Returns array
    -------

    '''
    array = []
    names = ["Ability I","Ability II","Hidden Ability","Type I","Type II"]
    colors = list('rbygkm')
    eggs_data = pd.read_excel('C:/Work/Data/Types.xlsx',sheet_name='Лист1',index_col=0)
    ability_data = pd.read_excel('C:/Work/Data/Ability.xlsx',sheet_name='Лист1',index_col=0)
    t_1 = {}
    t_2 = {}
    for i,abilki in enumerate(abilki):
        if i%2>0:
            if t_2.get(abilki) is not None:
                t_2[abilki]+=1
            else:
                t_2[abilki]=1
        else:
            if t_1.get(abilki) is not None:
                t_1[abilki]+=1
            else:
                t_1[abilki]=1
    klv = list(t_1.keys())
    for i,klvshka in enumerate(klv):
        klv[i]=ability_data["Ability"][klvshka]
    znch = list(t_1.values())
    klv2 = list(t_2.keys())
    for i,klvshka2 in enumerate(klv2):
        if  klvshka2!=0:
            klv2[i]=ability_data["Ability"][klvshka2]
        else:
            klv2[i]="No Ability"
    znch2 = list(t_2.values())

    array.append(pie(znch,klv,colors,names[0]))
    array.append(pie(znch2,klv2,colors,names[1]))

    t_1.clear()
    t_2.clear()
    for i,pryatki in enumerate(pryatki):
        if t_1.get(pryatki) is not None:
            t_1[pryatki]+=1
        else:
            t_1[pryatki]=1
    klv = list(t_1.keys())
    for i,klvshka in enumerate(klv):
        if  klvshka!=0:
            klv[i]=ability_data["Ability"][klvshka]
        else:
            klv[i]="No Hidden Ability"
    znch = list(t_1.values())

    array.append(pie(znch,klv,colors,names[2]))

    t_1.clear()
    t_2.clear()
    for i,spis in enumerate(tipes):
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
    array.append(pie(znch,klv,colors,names[3]))
    array.append(pie(znch2,klv2,colors,names[4]))

    return array
def raspredelenie(typelist):
    '''
    Parameters
    ----------
    typelist : TYPE Array
        list of type
    Returns array
    -------
    False.

    '''
    array = []

    plt.close()
    listochek = pd.read_excel('C:/Work/Data/pdx.test.xlsx',sheet_name='Sheet1',index_col=0)
    for i in range(0,max_id+1):
        for j in typelist:
            if j == data["Type I"][i] or j==data["Type II"][i]:
                stats = pd.Series([data["HP"][i],data["Atk"][i],data["Def"][i],
                                   data["SpA"][i],data["SpD"][i],data["Spe"][i]],
                index=["HP","Atk","Def","SpA","SpD","Spe"])
                listochek = listochek.append(stats,ignore_index=True)
    fig, axi = plt.subplots(figsize=(10, 10))
    axi.scatter(x = listochek['Atk'], y = listochek['Def'])
    plt.xlabel("Attack")
    plt.ylabel("Defense")
    plt.rc('xtick', labelsize=10)
    array.append(fig)
    save("C:/Work/Graphics/AtkDef")
    # plt.show()
    plt.close()
    fig, axi = plt.subplots(figsize=(10, 10))
    axi.scatter(x = listochek['SpA'], y = listochek['SpD'])
    plt.xlabel("SpA")
    plt.ylabel("SpD")
    plt.rc('xtick', labelsize=10)
    array.append(fig)
    save("C:/Work/Graphics/SpASpD")
    plt.close()
    fig, axi = plt.subplots(figsize=(10, 10))
    axi.scatter(x = listochek['HP'], y = listochek['Spe'])
    plt.xlabel("HP")
    plt.ylabel("Spe")
    plt.rc('xtick', labelsize=10)
    array.append(fig)
    save("C:/Work/Graphics/HPSpe")
    plt.close()
    # plt.show()
    return array
def avrstats(listok,b_z):
    '''
    Parameters
    ----------
    listok : TYPE Array
        list of pok_typelist type
    d_z : TYPE DataFrame
        database of pok_typelist
    Returns array
    -------

    '''
    plt.close()
    array = []
    stats = [0,0,0,0,0,0]
    avr = 0
    podhodyat = {}
    for i in range (0,max_id+1):
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
    colors = list('rgbkym')
    fig = plt.figure()
    a_x = fig.add_axes([0,0,1,1])
    a_x.bar(arr2,arr,color = colors)
    fig.set_figwidth(16)
    plt.title("Average Stats")
    plt.rc('xtick', labelsize=10)
    save("C:/Work/Graphics/Avr_stats")
    array.append(fig)
    # plt.show()
    plt.close()
    return array

def boxplot():
    '''
    Parameters
    ----------
    -------
    None.
    '''
    array=[]
    plt.close()
    fig = data.boxplot(column=["HP","Atk","Def","SpA","SpD","Spe"])#, by='Type I')
    array.append(fig)
    plt.show()

def proverka(t_1,b_1):
    '''
    Parameters
    ----------
    a : TYPE Integer
        id of egg group
    b : TYPE Integer
        id of egg group

    Returns 1
    -------
    Returns 0

    '''
    if eggs_connection[t_1][b_1]==1:
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
        database of pok_typelist
    Returns True
    -------
    False.

    '''
    if(d_b["Egg Group I"][id1]!=0 and d_b["Egg Group II"][id1]!=0):

        if(d_b["Egg Group I"][id2]!=0 and d_b["Egg Group II"][id2]!=0):
            if((  proverka(d_b["Egg Group I"][id1],d_b["Egg Group I"][id2])
                 +proverka(d_b["Egg Group I"][id1],d_b["Egg Group II"][id2])
                 +proverka(d_b["Egg Group II"][id1],d_b["Egg Group I"][id2])
                 +proverka(d_b["Egg Group II"][id1],d_b["Egg Group II"][id2]))>0):

                return True

        elif(d_b["Egg Group I"][id2]!=0 and d_b["Egg Group II"][id2]==0):
            if((  proverka(d_b["Egg Group I"][id1],d_b["Egg Group I"][id2])
                 +proverka(d_b["Egg Group II"][id1],d_b["Egg Group I"][id2]))>0):

                return True

    elif(d_b["Egg Group I"][id1]!=0 and d_b["Egg Group II"][id1]==0):
        if(d_b["Egg Group I"][id2]!=0 and d_b["Egg Group II"][id2]!=0):
            if((  proverka(d_b["Egg Group I"][id1],d_b["Egg Group I"][id2])
                 +proverka(d_b["Egg Group I"][id1],d_b["Egg Group II"][id2]))>0):

                return True

        elif(d_b["Egg Group I"][id2]!=0 and d_b["Egg Group II"][id2]==0):
            if (proverka(d_b["Egg Group I"][id1],d_b["Egg Group I"][id2]))>0:

                return True

    return False
