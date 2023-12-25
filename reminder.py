#!/usr/bin/env python3
from random import choice
from os import system
from time import sleep
from rainbowio import print_rgb, input_rgb, logo, number_words

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

def cli(mode = 0):
    system("clear")
    match mode:
        case 0:
            A = 0
            B = 1
        case 1:
            A = 1
            B = 0

    xp = 0
    while True:
        logo()

        word = get_words()
        if word == "404":
            print_rgb("red", "erro: words not found")
            sleep(3)
            system("clear")
            break

        print_rgb("green", f"XP = {xp}")

        print_rgb("blue", "-" * 20)
        print_rgb("green", f"question: {word[A]}")
        response = input_rgb("green", "response: ")
        print_rgb("blue", "-" * 20)

        if response == ".exit":
            system("clear")
            break

        if response == word[B]:
            print_rgb("green", "right answer")
            print_rgb("green", "+10 XP")
            xp = xp + 10
        else:
            print_rgb("red", f"wrong answer, the answer is {word[B]}")
            print_rgb("red", "-10 XP")
            xp = xp - 10
        
        sleep(1.3)
        system("clear")

def start():
    system("clear")
    logo()

    print_rgb("green", f"you have {number_words()} words")

    print_rgb("blue", "-" * 20)

    print_rgb("green", "#Reminder has two different game modes, enter the number to play in specific mode")
    print_rgb("green", "#questions in English answer in Portuguese type (0)")
    print_rgb("green", "#questions in Portuguese answers in English type (1)")
    print_rgb("green", "#type (.exit) at any time to close the program\n")

    print_rgb("green", "Which mode do you want to use?")
    res = input_rgb("green", "> ")

    print_rgb("blue", "-" * 20)

    match res:
        case "0":
            cli(0)
        case "1":
            cli(1)
        case ".exit":
            system("clear")
            return 0
        case _:
            print_rgb("red", "invalid command")
            sleep(1)
            start()

start()