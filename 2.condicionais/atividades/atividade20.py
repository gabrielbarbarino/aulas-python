import os
os.system("clear")

def somar(n1, n2):
    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2

def divisao(n1, n2):
    return n1 / n2

def multiplicar(n1, n2):
    return n1 * n2

def logoSenai():
    os.system("clear")
    print("-----  SENAI  -----")

numero1 = int(input("Digite o primeiro Numero: "))
numero2 = int(input("Digite o segundo Numero: "))

soma = somar(numero1, numero2)
subtrairr = subtrair(numero1, numero2)
divi = divisao(numero1, numero2)
mult = multiplicar(numero1, numero2)

logoSenai()
print(f"soma = {soma}")
print(f"Subtração = {subtrairr}")
print(f"divisão = {divi}")
print(f"multiplicação = {mult}")

