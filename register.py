#!/usr/bin/env python3
from rainbowio import print_rgb, input_rgb, logo
from os import system
from time import sleep

def text_format(en, pt):
    en = en.strip().lower()
    pt = pt.strip().lower()
    return f"{en}={pt}"

def add_bd(text):
    if text == "=":
        return "404"
    with open("bd.txt", "a") as bd:
        bd.write(f"{text}\n")
        return "200"

def number_words():
    try:
        with open("bd.txt", "r") as words:
            return len(words.readlines())
    except:
        return "I couldn't find your words"

def cli():
    while True:
        logo()

        print_rgb("green", f"words = {number_words()}")

        print_rgb("blue", "-" * 20)
        en = input_rgb("green", "English: ")
        pt = input_rgb("green", "Portuguese: ")
        print_rgb("blue", "-" * 20)

        if (en or pt) == ".exit":
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

system("clear")
cli()