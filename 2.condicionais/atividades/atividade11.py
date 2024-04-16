import os
os.system("clear")

contador = 0
soma = 0

while True:
    resposta = input("Deseja iserir uma nota?: ")
    if resposta != 'N':
        nota = float(input("Digite A nota: "))
        contador = contador + 1
        soma += nota
        media = soma / contador
    else:
        break



print(f"\n\nSua média foi: {media}")