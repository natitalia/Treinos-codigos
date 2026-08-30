#5. Exercício 5 – Senha
#Crie uma variável contendo uma senha.
#Depois, solicite que o usuário digite uma senha.
#Enquanto a senha estiver incorreta, exiba:
#- Senha incorreta. Tente novamente.
#Quando estiver correta, encerre a repetição e mostre:
#- Acesso permitido.

print("\nEste programa é para você criar uma senha!")

senha = input("\nCrie uma senha: ")
tentativa = input("Digite sua senha para acessar: ")

while tentativa != senha:
    print("\nSenha incorreta, tente novamente!")
    tentativa = input("Digite sua senha para acessar: ")
print("\nAcesso permitido")
print("\nPrograma encerrado")
