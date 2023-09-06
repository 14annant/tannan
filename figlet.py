'''
Written by: Tom Annan, HW for CS50
FIGlet, named after Frank, Ian, and Glen’s letters, is a program from the early 1990s for making large letters out of ordinary text, a form of ASCII art:

This program displays user input in a supported font type. It can use a randon font if no argument is given to begin with, or it can use a specific font used by the pyfiglet package

'''

from pyfiglet import Figlet
from sys import argv
from random import choice

figlet = Figlet()

if len(argv[1:]) == 0:
    ui = input("Input: ")
    rf = choice(figlet.getFonts())
    sf = figlet.setFont(font = rf)
    print(figlet.renderText(ui))
elif (argv[1] in ["--font", "-f"]) and (argv[2] in figlet.getFonts()) and len(argv[1:]) == 2:
    ui = input("Input: ")
    sf = figlet.setFont(font = argv[2])
    print(figlet.renderText(ui))
else:
    print("Invalid usage")