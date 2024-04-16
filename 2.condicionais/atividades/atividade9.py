import os
os.system("clear")

media = 0
nota = []

for i in range(1, 3):
    notas = float(input(f"Digite sua {i}º Nota: "))
    nota.append(notas)
    while notas < 0 or notas > 10:
        notas = float(input(f"Digite sua {i}º Nota: "))
        nota.append(notas)
    media += notas
    mediar = media / 2
    
print(f"\nSua média é: {mediar}")