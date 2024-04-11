import os

os.system("clear")

valor = int(input("Digite um Numero: "))

os.system("clear")
print("----------  RESULTADOS  ----------\n")
for i in range(0, 11):
    print(f"{valor} * {i} = {i * valor}")