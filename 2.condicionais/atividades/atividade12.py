
import os
os.system("clear")

print("S - Inserir mais uma Nota")
print("P - ver quantas notas foram inseridas")
print("N - Calcular a média aritmética das notas informadas")
contador = 0
soma = 0

while True:
    resposta = input("\nOpção:  ")
    if resposta == 'S':
        nota = float(input("Digite A nota: "))
        contador = contador + 1
        soma += nota
        media = soma / contador
    elif resposta == 'P':
        os.system("clear")
        print("---------- RESULTADOS ---------")
        print(f"\nQuantidade de Notas foi: {contador}")
        break
    elif resposta == 'N':
        os.system("clear")
        print("\n---------- RESULTADOS ---------")
        print(f"\nSua média foi: {media}")
        break

