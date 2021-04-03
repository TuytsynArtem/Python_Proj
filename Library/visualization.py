# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 17:36:07 2021

@author: User
"""
import matplotlib.pyplot as plt
from analyze import a,b
def add(tipe,kolvo):
    '''
    Parameters
    ----------
    tipe : TYPE String
        Type of pokemons
    kolvo : TYPE Integer
        Amount pokemons of each types

    Returns None
    -------
    None.

    '''
    fig = plt.figure()
    a_x = fig.add_axes([0,0,1,1])
    a_x.bar(tipe,kolvo)
    fig.set_figwidth(12)
    plt.show()
add(a,b)
