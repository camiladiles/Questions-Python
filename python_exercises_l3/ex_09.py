'''Faça um programa que pergunta o nome e o gênero da pessoa que está utilizando. O programa deverá responder:

Seja bem-vindo, [nome]! caso o gênero seja igual a 'M'
Seja bem-vinda, [nome]! caso o gênero seja igual a 'F'
Sej@ bem-vind@, [nome]! caso o gênero seja 'Neutro' ou 'Outro'

Caso uma opção diferente das listadas acima seja digitada, o programa deverá repetir a pergunta até que uma das opções válidas seja digitada.'''


#Resposta:

#Pergunta ao usuario:
nome = input("Qual o seu nome? ")
print('')
print("Use: M - Masculino, F - Feminino, N - Neutro ou Outro.")
genero = str(input("Qual o seu genero: "))
print("")

#Formula para ver se é M F ou N
while genero == 'M' or "F" or 'N' or 'Outro':

  if genero == 'M':
    print("Seja bem-vindo, ", nome, "!")
    break
  if genero == 'F':
    print("Seja bem-vinda, ", nome, "!")
    break
  if genero == 'N' or genero == 'Outro':
    print("Sej@ bem-vind@, ", nome, "!")
    break
  if genero != 'M' and genero != "F" and genero != 'N' and genero != 'Outro':
    genero = str(input("Qual o seu genero (Use: M - Masculino, F - Feminino, N - Neutro ou Outro."))
    print(" ")
