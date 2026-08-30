#3. Exercício 3 – Calculando a idade
#Crie um programa que solicite o nome e o ano de nascimento de uma pessoa. Em
#seguida, calcule a idade que ela completa em 2026 e exiba:
#Maria completa 30 anos em 2026.

print("\nOlá, este programa é uma calculadora de idade, vamos descobrir quantos anos você fará em...")
print("...2026!")

nasc = input("\nDigite o ano do seu nascimento: ")
nasc = int(nasc)
soma2026 = 2026 - nasc 

print("\nVocê terá:",soma2026,"em 2026!")

print("\nMuito daora né?! Quer testar mais?")
decisao = input("Digite [S] para sim ou [N] para não: ").lower()

while decisao == "s":
    ano = input("\nDigite um ano: ")
    ano = int(ano)
    soma = ano - nasc
    print("\nVocê terá:",soma,"em",ano,"!")

    
    decisao = input("Digite [S] para sim ou [N] para não: ").lower()

print("Programa encerrado")