#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 10:11:01 2022

@author: clockshield
"""

class Parent():
    def __init__(self):
        print("This is a parent class")
    
    def menu(dish):
        if dish == "burger":
            print("You can add the following toppings")
            print("More Cheese | More Jalapenos")
        elif dish == "iced_americano":
            print("You can add the following toppings")
            print("More Chococalate | More Caramel")
            
    def final_ammount(dish, add_ons):
        if dish == "burger" and add_ons == "cheese":
            print("You need to pay 250 USD")
        if dish == "burger" and add_ons == "jalapenos":
             print("You need to pay 350 USD")
        if dish == "iced_americano" and add_ons == "chocolate":
             print("You need to pay 250 USD")     
        if dish == "iced_americano" and add_ons == "caramel":
             print("You need to pay 450 USD")    
        
class child1(Parent):
    def __init__(self, dish):
        self.new_dish = dish
    def getMenu(self):
        Parent.menu(self.new_dish)

class child2(Parent):
    def __init__(self, dish, add_ons):
        self.new_dish = dish
        self.addons = add_ons
    def get_final_ammount(self):
        Parent.final_ammount(self.new_dish, self.addons)
child1_object = child1("iced_americano")
child1_object.getMenu()

child2_object = child2("iced_americano", "chocolate")
child2_object.get_final_ammount()
