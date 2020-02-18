# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 13:05:23 2019

@author: Talib
"""
class Pets(Dog):
    
    def __init__(self,dogs):
        self.dogs = dogs


# Parent class
class Dog:

    # Class attribute
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)
    
my_dogs = [Bulldog("Tom",6),
           RussellTerrier("Larry",10),
           Dog("Fletcher",9)]

print("i have {} dogs".format(len(my_dogs)))

for dogs in my_dogs:
    print("{} is {}".format(dogs.name,dogs.age))
    
print("And they are all {} ofcourse".format(Dog.species))