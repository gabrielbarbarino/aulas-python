import os
os.system("clear")

def logoSenai():
    os.system("clear")
    print("-----  SENAI  -----")

logoSenai()
numero1 = int(input("Digite o Primeiro Numero: "))
logoSenai()
numero2 = int(input("Digite o Segundo Numero: "))

def mediar(n1, n2):
    return (n1 + n2) / 2

media = mediar(numero1, numero2)

logoSenai()
print(media)

