'''Faça um programa que pergunta o nome e o gênero da pessoa que está utilizando. O programa deverá responder:

Seja bem-vindo, [nome]! caso o gênero seja igual a 'M'
Seja bem-vinda, [nome]! caso o gênero seja igual a 'F'
Sej@ bem-vind@, [nome]! caso o gênero seja 'Neutro' ou 'Outro'
Opção inválida caso gênero não possua um dos 3 valores descritos acima.'''

#Resposta:

#Pergunta ao usuario:
nome = input("Qual o seu nome? ")
genero = str(input("Qual o seu genero (Use: M - Masculino, F - Feminino, N - Neutro?"))

#Formula para ver se é M F ou N
if genero == 'M':
  print("Seja bem-vindo, ", nome, "!")
if genero == 'F':
  print("Seja bem-vinda, ", nome, "!")
if genero == 'N':
  print("Sej@ bem-vind@, ", nome, "!")
