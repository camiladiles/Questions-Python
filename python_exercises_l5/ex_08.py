"""
08. Faça um programa que leia as coordenadas de dois vetores a partir do teclado e armazene-as em listas. Exemplo:

vetor1 = [1, 4, 7]
vetor2 = [2, 3, 4]

O seu programa deverá realizar o produto escalar. No exemplo acima, ele é dado por:

produto = 1*2 + 4*3 + 7*4 = 42

Atenção: note que o produto escalar, apesar de ser uma operação entre vetores, possui como resultado um único número.
"""

#Resposta:

import random

vetor1 = [] #lista vazia 
vetor2 = [] #lista vazia

n_elementos = int(input("Digite quantidade de elementos do seu vetor: "))
print(' ')

for count1 in range (1, n_elementos + 1):
  nv1 = float(input("Digite a coordenada do vetor 1: "))
  vetor1.append(nv1)

print(' ')

for count2 in range (1, n_elementos + 1):
  nv2 = float(input("Digite a coordenada do vetor 2: "))
  vetor2.append(nv2)

print(' ')
print("Vetor 1: ", vetor1)
print(' ')
print("Vetor 2: ", vetor2)

vetor_multi = []
produto = 0

for i in range (n_elementos):
  produto = vetor1[i] * vetor2[i]
  vetor_multi.append(produto)

#print(' ')
#print(vetor_multi)

vetor_produto = 0

for i in vetor_multi:
   vetor_produto += i

print("")
print("O produto escalar é: ", vetor_produto)

print("")
print("Programa terminado!")
