"""
O programa deverá exibir:

a menor nota
a maior nota
a média calculada desconsiderando a maior e a menor nota
"""

#Resposta:

import random
notas = [] #lista vazia

act_avaliadas = int(input("Quantas atividades você avaliou? (Mínimo 4): "))
print(' ')

for count in range (1, act_avaliadas + 1):
  nota = float(input("Digite a nota: "))
  notas.append(nota)

print(' ')
print("Todas as notas: ", notas)

soma = 0

for i in notas:
  soma = soma + i

print(' ')
maior = max(notas)
notas.remove(maior)
menor = min(notas)
notas.remove(menor)

new_soma = 0
for j in notas:
  new_soma = new_soma + j

print(new_soma)

print("A maior nota é: ", maior)
print(' ')
print("A menor nota é: ", menor)
print(' ')
print("Notas para a media: ", notas)

print(' ')
print("Quantidade de notas usadas: ", len(notas))

media = new_soma/len(notas)

print(' ')
print("A media é de: ", media)

print("")
print("Programa terminado!")
