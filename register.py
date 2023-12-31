#!/usr/bin/env python3
from rainbowio import print_rgb, input_rgb, logo, number_words
from os import system
from time import sleep

def text_format(en, pt):
    en = en.strip().lower()
    pt = pt.strip().lower()
    if en == '' or pt == '':
        return "="
    return f"{en}={pt}"

def add_bd(text):
    if text == "=":
        return "404"
    with open("bd.txt", "a") as bd:
        bd.write(f"{text}\n")
        return "200"

def cli():
    system("clear")
    while True:
        logo()

        print_rgb("green", f"you have {number_words()} words")

        print_rgb("blue", "-" * 20)
        en = input_rgb("green", "English: ")
        pt = input_rgb("green", "Portuguese: ")
        print_rgb("blue", "-" * 20)

        if en == ".exit" or pt == ".exit":
            system("clear")
            break

        response = add_bd(text_format(en, pt))

        match response:
            case "200":
                print_rgb("green", "added word")
            case "404":
                print_rgb("red", "word not added")

        sleep(1)
        system("clear")

cli()