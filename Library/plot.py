# -*- coding: utf-8 -*-
"""
Created on Tue May  4 19:34:32 2021

@author: User
"""
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from playsound import playsound

def save(path):
    plt.savefig(path)
def pie(value,ammount,color,name):
    plt.close()
    plt.pie(value,labels=ammount,colors=color,autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('equal')
    plt.title("Percentage of Different " + str(name) + " of Pokemons")
    plt.plot()
    fig=plt.gcf()
    plt.rc('xtick', labelsize=7)
    fig.set_size_inches(7,7)
    save("C:/Work/Graphics/"+str(name))
    plt.close()
    return fig
    # plt.show()