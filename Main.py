#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 05:50:59 2021

@author: adam
"""


import pandas as pd
from fridge import Fridge

data = pd.read_csv("RAW_recipes_updated.csv",converters={'ingredients': eval, 'tags': eval, 'steps': eval})
ingr = data['ingredients']
ids = data['id']

F = Fridge()
F.Add(
    [
        "eggs",
        "bacon",
        "feta",
        "milk",
        "oil",
        "onion",
        "sugar",
        "ground beef",
        "salt",
        "butter",
        "apples",
        "bananas",
        "pepper",
        "marshmallows",
        "rice krispies",
        "white rice",
        "beef gravy",
    ]
)
ID = F.Recipes(F.Contents(), ingr, ids)
recipe_names = F.relevant_recipe_names(ID)
print("Here are your options for the recipes:")
print("")
for number, name in enumerate(recipe_names[:, 0]):
    print(number, name)

choice = int(input("Pick your choice:"))

recipe = F.recipe_choice(choice, recipe_names)
F.recipe_in_detail(recipe)
