#2. Exercício 2 – Calculadora simples
#Crie um programa que solicite dois números inteiros ao usuário. Em seguida, mostre:
#• Soma;
#• Subtração;
#• Multiplicação;
#• Divisão.

print("\nOlá, este programa é uma calculadora! Teste e comprove :D")

a = input("\nDigite um número: ")
b = input("Digite outro número: ")

a = int(a)
b = int(b)

soma = a + b
subt = a - b
mult = a * b
div = a / b

print("\nSoma: ",soma)
print("Subtração: ",subt)
print("Multiplicação: ",mult)
print("Divisão: ",div)