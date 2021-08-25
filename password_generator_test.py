# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 19:35:00 2021

@author: wajee
"""

#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")

nr_letters= int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))

random.shuffle(letters)
random.shuffle(numbers)
random.shuffle(symbols)

letter_needed=letters[0:nr_letters]
number_needed=numbers[0:nr_numbers]
symbol_needed=symbols[0:nr_symbols]

password=letter_needed+number_needed+symbol_needed


random.shuffle(password)
final_password="".join(password)

print(f"Your password is: {final_password}")








