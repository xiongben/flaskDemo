#-*- coding=utf-8 -*-
import json
import random

# Factory method 

# class ChinaGetter:
#     def __init__(self):
#         self.trans = dict(dog="小狗",cat="小猫")

#     def get(self, msgid):
#         try:
#             return self.trans[msgid]
#         except KeyError:
#             return str(msgid)

# class EnglishGetter:
#     def get(self, msgid):
#         return str(msgid)

# def get_localizer(language="English"):
#     languages = dict(English = EnglishGetter, China = ChinaGetter)
#     return languages[language]()

# e,g = get_localizer("English"), get_localizer("China")

# for msgid in "dog parrot cat bear".split():
#     print(e.get(msgid))
#     print json.dumps(g.get(msgid),encoding="UTF-8",ensure_ascii=False)



# Abstract Factory
class PetShop:
    def __init__(self,animal_factory=None):
        self.pet_factory = animal_factory
    def show_pet(self):
        pet = self.pet_factory.get_pet()
        print("this is a lovely", str(pet))
        print("it says",pet.speak())
        print("it eats",self.pet_factory.get_food())

class Dog:
    def speak(self):
        return "woof"

    def __str__(self):
        return "Dog"

class Cat:
    def speak(self):
        return "meow"

    def __str__(self):
        return "Cat"

class CatFactory:
    def get_pet(self):
        return Cat()
    def get_food(self):
        return "cat food"

class DogFactory:
    def get_pet(self):
        return Dog()
    def get_food(self):
        return "dog food"

def get_factory():
    return random.choice([DogFactory,CatFactory])()

shop = PetShop()
for i in range(3):
    shop.pet_factory = get_factory()
    shop.show_pet()
    print("="*20)