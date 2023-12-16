def text_format(en, pt):
    return f"{en}#{pt}"

def add_bd(text):
    for i in range(0,5):
        with open("bd.txt", "a") as bd:
            bd.write(f"{text}\n")

t = text_format("red", "vermelho")

add_bd(t)