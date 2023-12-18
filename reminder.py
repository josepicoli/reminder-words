from tkinter import *
from random import *

def get_words():
    try:
        with open("bd.txt", "r") as bd:
            words = bd.readlines()
    except:
        return print("error reading the file")

    words = choice(words)
    words = words.split("=")
    words[1] = words[1][:-1]
    return words

def interface():
    black = "#000000"
    white = "#ffffff"

    frame = Tk()
    frame.geometry("400x200")
    frame.title("teste")
    frame.config(bg= black)

    lb_ask = Label(frame)
    lb_ask.config(text= choose(get_bd()))
    lb_ask.config(font= "Arial 18 bold")
    lb_ask.config(bg= black)
    lb_ask.config(fg= white)
    lb_ask.place(x= 175, y= 20)

    frame.mainloop()

def cli():
    while True:
        word = get_words()
        print(f"question: {word[0]}")
        response = input("response: ")
        if response == word[1]:
            print("T")
        else:
            print("F")

cli()