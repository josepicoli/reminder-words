def text_format(en, pt):
    en = en.strip()
    pt = pt.strip()
    return f"{en}#{pt}"

def add_bd(text):
    with open("bd.txt", "a") as bd:
        bd.write(f"{text}\n")

t = text_format("red", "vermelho")

add_bd(t)