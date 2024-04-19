numeros = []

for i in range(5):
    numero = int(input(f"Digite p {i + 1} Numeor: "))
    if numero < 0:
        numeros.append(0)
    else:
        numeros.append(numero)

print(numeros)