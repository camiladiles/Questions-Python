"""
10. Vamos fazer um programa para representar uma aluna em formato amigável para salvar em uma tabela ou banco de dados.

Peça para a usuária digitar:

o nome da aluna
o número de matrícula
a quantidade de provas realizadas
a nota de cada uma das provas
o percentual de presenças
A aluna deverá ser representada em uma lista obedecendo a seguinte estrutura:

índice 0: número de matrícula
índice 1: nome
índice 2: uma lista com todas as suas notas
índice 3: sua média
índice 4: seu percentual de presenças
índice 5: um booleano indicando se a aluna foi aprovada ou reprovada
Considere como critério de aprovação nota maior ou igual a 6.0 e presença igual ou superior a 70%.

Ex:
aluna = [22042022, 'Brenda', [10.0, 9.0, 9.0, 10.0], 9.5, 80, True]
"""

#Respuesta:

aluna = []

matricula = int(input("Digite seu número de matricula: "))
aluna.append(matricula)
nome = str(input("Digite seu nome: "))
aluna.append(nome)
n_provas = int(input("Digite quantas provas realizou: "))
print(' ')

notas = []


for count in range (1, n_provas + 1):
  prova = float(input("Digite a nota da prova: "))
  notas.append(prova)

aluna.append(notas)
print(' ')

soma = 0
for i in notas:
  soma = soma + i

media = soma/len(notas)
aluna.append(media)
#print("A media é de: ", media)

presenca = int(input("Digite seu percentual de presença (%): "))
aluna.append(presenca)

x = True
y = False

if prova >= 6 and presenca >=70:
  x
  aluna.append(x)
else:
  y
  aluna.append(y)
  

print("Aluna = ", aluna)
