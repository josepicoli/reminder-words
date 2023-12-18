from tkinter import *

def text_format(en, pt):
    en = en.strip().lower()
    pt = pt.strip().lower()
    return f"{en}={pt}"

def add_bd(text):
    with open("bd.txt", "a") as bd:
        bd.write(f"{text}\n")

def interface():
    black = "#000000"
    white = "#ffffff"

    frame = Tk()
    frame.geometry("400x200")
    frame.title("teste")
    frame.config(bg= black)

    en_label = Label(frame)
    en_label.config(text= "English")
    en_label.config(bg= black)
    en_label.config(fg= white)
    en_label.place(x= 65, y= 50)

    en_txt = Entry(frame)
    en_txt.config(bd= 0)
    en_txt.place(x= 150, y= 50)

    pt_label = Label(frame)
    pt_label.config(text= "português")
    pt_label.config(bg= black)
    pt_label.config(fg= white)
    pt_label.place(x= 65, y= 80)

    pt_txt = Entry(frame)
    pt_txt.config(bd= 0)
    pt_txt.place(x= 150, y= 80)

    add_button = Button(frame)
    add_button.config(text= "ADD")
    add_button.config(bd= 0)
    add_button.config(command= lambda: add_bd(text_format(en_txt.get(), pt_txt.get())))
    add_button.place(x= 190, y= 110)

    frame.mainloop()

interface()