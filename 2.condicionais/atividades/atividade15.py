import os
os.system("clear")

notas = []

for i in range(6):
    numero = int(input("Digite um numero: "))
    
    while numero < 0 or numero % 2 == 1:
        print("Opção invalida!")
        numero = int(input("Digite um numero: "))
        

    notas.append(numero)

os.system("clear")
print("---------  resultados  ---------")
for i in range(5, -1, -1):
    print(f"{notas[i]}")