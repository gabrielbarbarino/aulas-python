import os

os.system("clear")

numero1 = int(input("Digite o Primeiro Numero: "))
numero2 = int(input("Digite o Segundo Numero: "))

soma = numero1 + numero2
media = soma / 2
produto = numero1 * numero2

if numero1 > numero2:
    maiorNumero = numero1
    menorNumero = numero2
else:
    maiorNumero = numero2
    menorNumero = numero1


if numero1 == numero2:
    print(f"\nVocê digiotu o n {numero1} Repetido!")
else:
    print("\nSão Numeros diferentes!")

print(f"\n\nA Média foi: {media}")
print(f"\nA Soma foi: {soma}")
print(f"\nO Produto foi: {produto}")
print(f"\nO Menor Valor foi: {menorNumero}\n\n")
