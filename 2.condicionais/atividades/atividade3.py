import os
os.system("clear")

loginOk = "gabriel"
senhaOk = "7040"

senha = "11"
login = "22"

while login != loginOk or senha != senhaOk:
    login = input("Digite seu Login: ")
    senha = input("Digite sua Senha: ")
    if login == loginOk and senha == senhaOk:
        print("\nBem-vindo!")
        break
    else: 
        os.system("clear")
        print("\nTente Novamente!")