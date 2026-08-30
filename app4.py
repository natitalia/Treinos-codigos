#4. Exercício 4 – Manipulando uma frase
#Solicite ao usuário que digite uma frase. Depois, exiba:
#• A frase em letras maiúsculas;
#• A frase em letras minúsculas;
#• A frase com a primeira letra maiúscula.
#Utilize os métodos de string apresentados em sala.

print("\nEste programa manipula a sua frase")
frase = input("\nDigite sua frase: ")

maiusc = frase.upper()
minusc = frase.lower()
primer_maiusc = frase.capitalize()

print("\nFrase em maiúscula: ",maiusc)
print("Frase em minúscula: ",minusc)
print("Frase com a primeira letra maiúscula: ",primer_maiusc)

print("\nPrograma encerrado :D")