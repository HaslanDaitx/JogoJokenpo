#Crie um programa que faça o computsdor jogar JOKENPÔ com você.
'''import random
import time
while True:
    itens = ("Pedra", "Papel", "Tesoura")
    computador = random.randint(0, 2)
    #print("O computador escolheu {}".format(itens[computador]))
    print("""Suas opções:
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA
    [ 3 ] SAIR""")
    jogador = int(input("Qual a sua jogada?"))
    if jogador == 3:
        print("-=" * 12)
        print("Obrigado por jogar!")
        print("-=" * 12)
        break
    print("JO")
    time.sleep(1)
    print("KEN")
    time.sleep(1)
    print("PÔ!!!")
    print("-=" * 12)
    print("Computador Jogou {}".format(itens[computador]))
    print("Você jogou {}".format(itens[jogador]))
    print("-=" * 12)
    if computador == 0: # computador jogou PEDRA
        if jogador == 0:
            print("EMPATE")
        elif jogador == 1:
            print("VOCÊ VENCEU")
        elif jogador == 2:
            print("COMPUTADOR VENCEU")
        else:
            print("JOGADA INVÁLIDA!")
    elif computador == 1: # computador jogou PAPEL
        if jogador == 0:
            print("COMPUTADOR VENCEU")
        elif jogador == 1:
            print("EMPATE")
        elif jogador == 2:
            print("VOCÊ VENCEU")
        else:
            print("JOGADA INVÁLIDA!")
    elif computador == 2: # computador jogou TESOURA
        if jogador == 0:
            print("VOCÊ VENCEU")
        elif jogador == 1:
            print("COMPUTADOR VENCEU")
        elif jogador == 2:
            print("EMPATE")
        else:
            print("JOGADA INVÁLIDA!")
    else:
        print("Insira um número diferente!!!")'''

'''import random
import tkinter as tk
from tkinter import messagebox

def jogar(jogador):
    itens = ["Pedra", "Papel", "Tesoura"]
    computador = random.choice(itens)

    resultado = ""
    if jogador == computador:
        resultado = "EMPATE"
    elif (jogador == "Pedra" and computador == "Tesoura") or \
         (jogador == "Papel" and computador == "Pedra") or \
         (jogador == "Tesoura" and computador == "Papel"):
        resultado = "VOCÊ VENCEU"
    else:
        resultado = "COMPUTADOR VENCEU"

    messagebox.showinfo("Resultado", f"Computador jogou: {computador}\nVocê jogou: {jogador}\n{resultado}")

def sair():
    root.destroy()

root = tk.Tk()
root.title("JOKENPÔ")

frame = tk.Frame(root)
frame.pack(pady=20)

label = tk.Label(frame, text="Escolha sua jogada:", font=("Helvetica", 14))
label.pack()

buttons_frame = tk.Frame(frame)
buttons_frame.pack(pady=10)

btn_pedra = tk.Button(buttons_frame, text="Pedra", width=10, command=lambda: jogar("Pedra"))
btn_pedra.grid(row=0, column=0, padx=5)

btn_papel = tk.Button(buttons_frame, text="Papel", width=10, command=lambda: jogar("Papel"))
btn_papel.grid(row=0, column=1, padx=5)

btn_tesoura = tk.Button(buttons_frame, text="Tesoura", width=10, command=lambda: jogar("Tesoura"))
btn_tesoura.grid(row=0, column=2, padx=5)

btn_sair = tk.Button(frame, text="Sair", width=10, command=sair)
btn_sair.pack(pady=10)

root.mainloop()'''


import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def jogar(jogador):
    itens = ["Pedra", "Papel", "Tesoura"]
    computador = random.choice(itens)

    resultado = ""
    if jogador == computador:
        resultado = "EMPATE"
    elif (jogador == "Pedra" and computador == "Tesoura") or \
         (jogador == "Papel" and computador == "Pedra") or \
         (jogador == "Tesoura" and computador == "Papel"):
        resultado = "VOCÊ VENCEU"
    else:
        resultado = "COMPUTADOR VENCEU"

    messagebox.showinfo("Resultado", f"Computador jogou: {computador}\nVocê jogou: {jogador}\n{resultado}")

def sair():
    root.destroy()

root = tk.Tk()
root.title("JOKENPÔ")
root.geometry("400x400")
root.resizable(False, False)

# Carregar imagens
img_pedra = ImageTk.PhotoImage(Image.open("pedra.png").resize((80, 80)))
img_papel = ImageTk.PhotoImage(Image.open("papel.png").resize((80, 80)))
img_tesoura = ImageTk.PhotoImage(Image.open("tesoura.png").resize((80, 80)))

# Título
title_frame = tk.Frame(root)
title_frame.pack(pady=20)

title_label = tk.Label(title_frame, text="JOKENPÔ", font=("Helvetica", 24, "bold"))
title_label.pack()

# Instruções
frame = tk.Frame(root)
frame.pack(pady=20)

label = tk.Label(frame, text="Escolha sua jogada:", font=("Helvetica", 16))
label.pack()

# Botões de jogo
buttons_frame = tk.Frame(frame)
buttons_frame.pack(pady=10)

btn_pedra = tk.Button(buttons_frame, image=img_pedra, command=lambda: jogar("Pedra"))
btn_pedra.grid(row=0, column=0, padx=10, pady=10)

btn_papel = tk.Button(buttons_frame, image=img_papel, command=lambda: jogar("Papel"))
btn_papel.grid(row=0, column=1, padx=10, pady=10)

btn_tesoura = tk.Button(buttons_frame, image=img_tesoura, command=lambda: jogar("Tesoura"))
btn_tesoura.grid(row=0, column=2, padx=10, pady=10)

# Botão de sair
btn_sair = tk.Button(frame, text="Sair", width=10, font=("Helvetica", 12), bg="red", fg="white", command=sair)
btn_sair.pack(pady=20)

root.mainloop()
