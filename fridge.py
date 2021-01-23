#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 12:41:51 2021

@author: adam
"""

import numpy as np
import pandas as pd
from re import search

data = pd.read_csv("RAW_recipes.csv",converters={'ingredients': eval, 'tags': eval, 'steps': eval, 'nutrition': eval})
ingr = data.iloc[:,10]
#%%
fridge = []
def Fridge():
    return fridge

def Recipes(a = []):
    '''Search for recipes that use products from the fridge'''
    ID = []
    com = []
    for i in range(len(ingr)):
        for k in a:
            for g in ingr[i]:
                if search(k,g):
                    com.append(k)
        if len(com)==len(ingr[i]) and len(com) != 0:
            ID.append(data.iloc[:,1][i])
        com = []
    return ID
    
def Remove(a = []):
    '''Remove used objects from the fridge'''
    res = list(set(a)^set(Fridge()))
    return res
    
def Add(a = []):
    '''Add objects to the fridge'''
    fridge = Fridge().extend(a)
    return fridge

Add(['eggs', 'bacon', 'feta', 'milk', 'oil', 'onion', 'sugar', 'ground beef', 'salt', 'butter'])
Add(['apples', 'bananas', 'pepper', 'marshmallows', 'rice krispies', 'white rice', 'beef gravy'])
Fridge()
print(Recipes(Fridge()))


