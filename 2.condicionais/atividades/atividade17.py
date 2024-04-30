import os

def somar(n1, n2): # Função somar - Pegando 2 valores
    return n1 + n2    # Retornando a função, com o valor da Soma 

os.system("clear")
numero1= int(input("Digite um numero: "))
numero2 = int(input("Digite um numero: "))

soma = somar(numero1, numero2) # Chamando a função
print(f"resulatado = {soma}")