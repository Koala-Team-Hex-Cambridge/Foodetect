#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 12:41:51 2021

@author: adam
"""

import numpy as np
from re import search
from recipe_scrapers import scrape_me
import random
from quantulum3 import parser


class Fridge:

    def __init__(self, fridge = [], quantities = {}):
        self._fridge = fridge
        self._quantities = quantities

    def Contents(self):
        return self._fridge


    def Recipes(self, a=[], ingr=[], ids=[]):
        """Search for recipes that use products from the fridge"""
        print("Searching your fridge for available recipes:")
        ID = []
        com = []
        for i in range(len(ingr)):
            for k in a:
                for g in ingr[i]:
                    if search(k, g):
                        com.append(k)

            if len(com)==len(ingr[i]) and len(com) != 0:
                ID.append(ids[i])
            com = []
        return ID


    def Remove(self, a=[]):
        """Remove used objects from the fridge"""
        self._fridge = list(set(a) ^ set(self._fridge))
        return self._fridge


    def Add(self, a=[]):
        """Add objects to the fridge"""
        self._fridge.extend(a)
        return self._fridge


    def relevant_recipe_names(self, ID):
        """Finds the names of 5 random recipes that have been identified"""
        print("Finding 5 random recipes you can make out of 230 thousand recipes")
        recipe_names = np.empty((0, 2))
        ID_list = random.sample(ID, min(len(ID), 5))
        for x in ID_list:
            scraper = scrape_me("https://www.food.com/" + str(x))
            recipe_names = np.append(recipe_names, np.array([[scraper.title(), x]]), axis=0)
        return recipe_names

    def recipe_choice(self, choice, recipe_names):
        """Work in progress - returns the recipe of choice in more detail"""
        scraper = scrape_me("https://www.food.com/" + str(recipe_names[choice, 1]))
        return scraper
    
    def recipe_in_detail(self, recipe):
        print(recipe.title())
        print("")
        print("A recipe that takes {} minutes to make, and yields {}.".format(recipe.total_time(), recipe.yields()))
        print("")
        print("{:s}\n{:s}\n".format("Ingredients:", len("Ingredients:") * "-"))
        print(*recipe.ingredients(), sep = '\n')
        print("")
        print("{:s}\n{:s}\n".format("Instructions:", len("Instructions:") * "-"))
        ins = recipe.instructions()
        ins = ins.replace('\n', '')
        ins2 = ins.split('.')
        for number, ins in enumerate(ins2):
            print(ins)
            print("")
        print("{:s}\n{:s}\n".format("Nutrients:", len("Nutrients:") * "-"))
        for key in recipe.nutrients():
            print(key, ':', recipe.nutrients()[key])

# =============================================================================
#     def recipe_measurements(self, recipe):
#         ingr_list = recipe.ingredients()
#         for each in ingr_list:
#             measurement = parser.parse(each)
#             for k in self._fridge:
#                 if search(k, each):
#                     if measurement[0].unit.name == "pound-mass":
#                         measurement[0].value *= 453
#                         measurement[0].unit = "grams"
#                     elif measurement[0].unit.name == "tablespoon":
#                         measurement[0].value *= 15
#                         measurement[0].unit = "millilitres"
#                     elif measurement[0].unit.name == "teaspoon":
#                         measurement[0].value *= 5
#                         measurement[0].unit = "millilitres"
#                     elif measurement[0].unit.name == "inch":
#                         measurement[0].value *= 2.54
#                         measurement[0].unit = "centimetres"
#                     elif measurement[0].unit.name == "ounce":
#                         measurement[0].value *= 28
#                         measurement[0].unit = "grams"
#                     elif measurement[0].unit.name == "gallon":
#                         measurement[0].value *= 3.7
#                         measurement[0].unit = "litres"
#                     elif measurement[0].unit.name == "quart":
#                         measurement[0].value *= 0.946
#                         measurement[0].unit = "litres"
#                     elif measurement[0].unit.name == "pint":
#                         measurement[0].value *= 0.473
#                         measurement[0].unit = "litres"
#                     elif measurement[0].unit.name == "cup":
#                         measurement[0].value *= 237
#                         measurement[0].unit = "millilitres"
#                     print("Needs",measurement[0].value, measurement[0].unit, "of", k)
# =============================================================================
            
    def AssignQuant(self, index=0, value=0):
        "Assign quantities to the products in the fridge"
        self._index = self._fridge.index(input("Type of food:"))
        self._value = input("Quantity of food:")
        self._quantities[self._fridge[self._index]] = {self._value}
        return self._quantities