import os
os.system("clear")

par = 0; positivo = 0
impar = 0; negativo =  0
contador = 0

for i in range(5):
    numero = int(input("Digite um Numero: "))

    contador += 1
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1

    if numero > 0:
        positivo += 1
    else:
        negativo += 1

print(f"Par: {par}, Impar: {impar}")
print(f"Positivos: {positivo}, Negativos: {negativo}")
print(f"QTD Inseridos: {contador}")