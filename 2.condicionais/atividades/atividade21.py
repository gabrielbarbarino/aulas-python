import os
os.system("clear")

def logoSenai():
    os.system("clear")
    print("----- SENAI -----")

def analisePar(n1):
    if n1 % 2 == 0:
        print("O Numero é Par")
    else:
        print("O Numero é Impar")


numero = int(input("Digite um numero: "))
logoSenai()
analisePar(numero)
