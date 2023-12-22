#!/usr/bin/env python3
from rainbowio import print_rgb, input_rgb, logo
from os import system
from time import sleep

def text_format(en, pt):
    en = en.strip().lower()
    pt = pt.strip().lower()
    return f"{en}={pt}"

def add_bd(text):
    with open("bd.txt", "a") as bd:
        bd.write(f"{text}\n")

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

        if en or pt == ".exit":
            system("clear")
            break

        add_bd(text_format(en, pt))

        print_rgb("green", "added word")

        sleep(1)
        system("clear")

system("clear")
cli()