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

    lb_en = Label(frame)
    lb_en.config(text= "English")
    lb_en.config(bg= black)
    lb_en.config(fg= white)
    lb_en.place(x= 65, y= 50)

    txt_en = Entry(frame)
    txt_en.config(bd= 0)
    txt_en.place(x= 150, y= 50)

    lb_pt = Label(frame)
    lb_pt.config(text= "português")
    lb_pt.config(bg= black)
    lb_pt.config(fg= white)
    lb_pt.place(x= 65, y= 80)

    txt_pt = Entry(frame)
    txt_pt.config(bd= 0)
    txt_pt.place(x= 150, y= 80)

    add_button = Button(frame)
    add_button.config(text= "ADD")
    add_button.config(bd= 0)
    add_button.config(command= lambda: add_bd(text_format(txt_en.get(), txt_pt.get())))
    add_button.place(x= 190, y= 110)

    frame.mainloop()

interface()