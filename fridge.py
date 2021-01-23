#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 12:41:51 2021

@author: adam
"""

import numpy as np
import pandas as pd
from re import search
from recipe_scrapers import scrape_me
import random
from quantulum3 import parser


data = pd.read_csv("RAW_recipes.csv",converters={'ingredients': eval, 'tags': eval, 'steps': eval, 'nutrition': eval})
ingr = data['ingredients']
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
            ID.append(data["id"][i])
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

def relevant_recipe_names(ID):
    '''Finds the names of 5 random recipes that have been identified'''
    recipe_names = np.empty((0,2))
    ID_list = random.sample(ID, min(len(ID), 5))
    for x in ID_list:
        scraper = scrape_me("https://www.food.com/" + str(x))
        recipe_names = np.append(recipe_names, np.array([[scraper.title(), x]]), axis = 0)
    return recipe_names
        
def recipe_in_detail(choice, recipe_names):
    '''Work in progress - returns the recipe of choice in more detail'''
    scraper = scrape_me("https://www.food.com/" + str(recipe_names[choice, 1]))
    return scraper

Add(['eggs', 'bacon', 'feta', 'milk', 'oil', 'onion', 'sugar', 'ground beef', 'salt', 'butter'])
Add(['apples', 'bananas', 'pepper', 'marshmallows', 'rice krispies', 'white rice', 'beef gravy'])
ID = Recipes(Fridge())
recipe_names = relevant_recipe_names(ID)
for number, name in enumerate(recipe_names[:, 0]):
    print(number, name)

choice = int(input("Pick your choice:"))

recipe = recipe_in_detail(choice, recipe_names)

def recipe_measurements(recipe):
    ingr_list = recipe.ingredients()
    for each in ingr_list:
        measurement = parser.parse(each)
        for k in Fridge():
            if search(k, each):
                print("Needs",measurement[0].value, measurement[0].unit, "of", k)

