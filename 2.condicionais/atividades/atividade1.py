import os

os.system("clear")

nome = input("Digite su nome: ")
idade = input("Digite sua idade: ")

nota1 = float(input("Digite sua primeira Nota: "))
nota2 = float(input("Digite sua segunda Nota: "))
nota3 = float(input("Digite sua terceira Nota: "))
nota4 = float(input("Digite sua quarta Nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

os.system("clear")
print(f"\nSua média é: {media}")