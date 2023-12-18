from tkinter import *
from random import *

def get_bd():
    try:
        with open("bd.txt", "r") as bd:
            return bd.readlines()
    except:
        print("error reading the file")
        return "404"

def choose(words):
    return choice(words)

def interface():
    frame = Tk()
    frame.geometry("400x200")
    frame.mainloop()

print(choose(get_bd()))
interface()