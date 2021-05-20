# -*- coding: utf-8 -*-
"""
Created on Tue May  4 19:34:32 2021

@author: User
"""
import matplotlib.pyplot as plt

def save(path):
    plt.savefig(path)
def pie(value,ammount,color,name):
    
    plt.pie(value,labels=ammount,colors=color,autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('equal')
    plt.title("Percentage of Different " + str(name) + " of Pokemons")
    plt.plot()
    fig=plt.gcf()
    fig.set_size_inches(7,7)
    save("C:/Work/Graphics/"+str(name))
    plt.show()