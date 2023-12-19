from tkinter import *
from random import *

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
    while True:
        word = get_words()
        if word == "404":
            print("erro")
            break

        print("-" * 20)
        print(f"question: {word[0]}")
        response = input("response: ")
        print("-" * 20)
        if response == word[1]:
            print_rgb("green", "True")
        else:
            print_rgb("red", "False")

cli()