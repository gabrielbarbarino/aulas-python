import os
os.system("clear")

idade = int(input("Digite sua idade: "))

if idade < 18 or idade >= 65:
    print("\nNão precisa votar!")
else: 
    print("\nObrigado a votar!")


print("\n\n---------- FIM ---------")