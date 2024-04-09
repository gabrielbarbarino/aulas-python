import os
os.system("clear")

loginOk = "gabriel"
senhaOk = 7040

login = input("Digite seu Usuário: ")
senha = input("Digite sua Senha: ")

if login == loginOk or senha == senhaOk:
    print("Bem-vindo!")
else:
    print("Login ou Senha inválidos!")