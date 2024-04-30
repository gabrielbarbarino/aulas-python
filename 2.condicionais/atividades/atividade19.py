import os
os.system("clear")

def tabuada(n1):
    for i in range(11):
        print(f"{n1} x {i} = {n1 * i}")

numeroPedido = int(input("Digite um Numero Para ser Calculado: "))

tabuadaN = tabuada(numeroPedido)