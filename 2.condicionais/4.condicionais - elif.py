import os

os.system("clear")

nota = float(input("Digite sua nota: "))

if nota >= 7:
    print("Aprovado!")
elif nota >=5:
    print("Recuperação")
else:
    print("Reprovado!")


print("\n\n---------- FIM ----------")