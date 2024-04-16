import os
os.system("clear")

def mediarr(mediar):
    if mediar >= 7:
        print("Aprovado!")
    elif media < 5:
        print("Recuperação!")
    else:
        print("Reprovado!")

media = 0
nota = []

for i in range(1, 4):
    notas = float(input(f"Digite sua {i}º Nota: "))
    nota.append(notas)
    while notas < 0 or notas > 10:
        notas = float(input(f"Digite sua {i}º Nota: "))
        nota.append(notas)
    media += notas
    mediar = media / 2
        
print(f"\nSua média é: {mediar}")
mediarr(mediar)