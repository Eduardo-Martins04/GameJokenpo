# -*- coding: UTF-8
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print("""Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura""")
jogador = int(input("Qual é a sua jogada? "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
print("-="*11)
print("Computador jogou {} ".format(itens[computador]))
print("Jogador jogou {} ".format(itens[jogador]))
print("-="*11)
if computador == 0:#PEDRA
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print("JOGADOR VENCEU")
    elif jogador == 2:
        print("COMPUTADOR VENCEU")
    else:
        print("JOGADA INVALIDA")
elif computador == 1: #PAPEL
    if jogador == 0:
        print("COMPUTADOR VENCEU")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("JOGADOR VENCEU")
    else:
        print("JOGADA INVALIDA")
elif computador == 2:#TESOURA
    if jogador == 0:
        print("JOGADOR VENCEU")
    elif jogador == 1:
        print("COMPUTADOR VENCEU")
    elif jogador == 2:
        print("EMPATE")
    else:
        print("JOGADA INVALIDA")