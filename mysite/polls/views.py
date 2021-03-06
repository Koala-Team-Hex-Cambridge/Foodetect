from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import numpy as np
from re import search
from recipe_scrapers import scrape_me
import random
from quantulum3 import parser


class Fridge:

    def __init__(self, fridge = []):
        self._fridge = fridge

    def Contents(self):
        return self._fridge


    def Recipes(self, a=[], ingr=[], ids=[]):
        """Search for recipes that use products from the fridge"""
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
        recipe_names = np.empty((0, 2))
        ID_list = random.sample(ID, min(len(ID), 5))
        for x in ID_list:
            scraper = scrape_me("https://www.food.com/" + str(x))
            recipe_names = np.append(recipe_names, np.array([[scraper.title(), x]]), axis=0)
        return recipe_names


    def recipe_in_detail(self, choice, recipe_names):
        """Work in progress - returns the recipe of choice in more detail"""
        scraper = scrape_me("https://www.food.com/" + str(recipe_names[choice, 1]))
        return scraper


    def recipe_measurements(self, recipe):
        ingr_list = recipe.ingredients()
        for each in ingr_list:
            measurement = parser.parse(each)
            for k in Fridge():
                if search(k, each):
                    print("Needs",measurement[0].value, measurement[0].unit, "of", k)

with open('~/Desktop/Hex/Foodetect/mysite/polls/RAW_recipes.csv') as f:
        reader = csv.reader(f)
        for column in reader:
            _, created = Teacher.objects.get_or_create(
                ingr=reader["ingredients"],
		ids = reader['id']
                )

def index(request):
    F = Fridge()
    F.Add([
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
    "beef gravy",])
    HttpResponse(F.Add(input('Whats in your fridge:')))
    ID = F.Recipes(F.Contents(), ingr, ids)
    recipe_names = F.relevant_recipe_names(ID)
    for number, name in enumerate(recipe_names[:, 0]):
        HttpResponse(print(number, name))

    HttpResponse(choice = int(input("Pick your choice:")))

    recipe = F.recipe_in_detail(choice, recipe_names)
    return HttpResponse("Hello, world. You're at the polls index.")
