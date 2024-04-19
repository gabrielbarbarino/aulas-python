import os
os.system("clear")

numeros = []
quantidadeN = 0


for i in range(5):
    numero = float(input(f"Digite o {i + 1}º Numero: "))
    numeros.append(numero)

    if numero < 0:
        quantidadeN += 1
    else:
        soma = sum(numeros)

os.system("clear")
print("----------  RESULTADOS  ----------")
print(f"Quantidade numeros negativos: {quantidadeN}")
print(f"Soma valor Positivos: {soma}")
print(numeros)