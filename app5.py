#5. Exercício 5 – Calculando a média
#Crie um programa que solicite o nome de um aluno e suas duas notas. Calcule a
#média das notas e apresente o resultado utilizando uma mensagem formatada.
#Exemplo:
#O aluno João obteve média 8.0.

print("\nEste programa calcula a média dos alunos!")
aluno = input("\nDigite o nome do aluno: ")

not1 = input("\nDigite a primeira nota: ")
not2 = input("Digite a segunda nota: ")

not1 = float(not1)
not2 = float(not2)

media = (not1 + not2) / 2

print("\nA média do(a) aluno(a)",aluno,"foi: ",media)

