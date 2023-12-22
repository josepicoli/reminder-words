#!/usr/bin/env python3
from random import choice
from os import system
from time import sleep
from rainbowio import print_rgb, input_rgb, logo

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
            print("erro")
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