from tkinter import *
from random import choice
from os import system
from time import sleep

def print_rgb(color, text):
    match color:
        case "red":
            print(f"\033[91m{text}\033[0m")
        case "green":
            print(f"\033[92m{text}\033[0m")
        case "blue":
            print(f"\033[94m{text}\033[0m")

def get_words():
    try:
        with open("bd.txt", "r") as bd:
            words = bd.readlines()
    except:
        return "404"

    words = choice(words)
    words = words.split("=")
    words[1] = words[1].replace("\n", "")
    return words

def interface():
    black = "#000000"
    white = "#ffffff"

    frame = Tk()
    frame.geometry("400x200")
    frame.title("teste")
    frame.config(bg= black)

    lb_ask = Label(frame)
    lb_ask.config(text= "ask")
    lb_ask.config(font= "Arial 18 bold")
    lb_ask.config(bg= black)
    lb_ask.config(fg= white)
    lb_ask.place(x= 175, y= 20)

    frame.mainloop()

def cli():
    xp = 0
    while True:
        print_rgb("blue", "-" * 20)
        print_rgb("green", "|  reminder-words  |")
        print_rgb("blue", "-" * 20)

        word = get_words()
        if word == "404":
            print("erro")
            break
        print_rgb("green", f"XP = {xp}")
        print_rgb("blue", "-" * 20)
        print(f"question: {word[0]}")
        response = input("response: ")
        print_rgb("blue", "-" * 20)

        if response == word[1]:
            print_rgb("green", "True")
            print_rgb("green", "+10 XP")
            xp = xp + 10
        else:
            print_rgb("red", "False")
            print_rgb("red", "-10 XP")
            xp = xp - 10
        
        sleep(1)
        system("clear")

system("clear")
cli()