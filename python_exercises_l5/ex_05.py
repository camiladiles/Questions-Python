"""
05. Faça um programa que percorre uma lista de números. Os números abaixo da média dos valores deverão ser inseridos em uma lista, e os valores acima da média deverão ser inseridos em outra lista.
"""

#Resposta:

import random
lista = [] #lista vazia

for contador in range(0, 20):
  sorteio = random.randint(0, 100)
  lista.append(sorteio)
print("Lista: ", lista)
print("")
print("Quantidade de números da lista: ", len(lista))
print("")

soma = 0

for i in lista:
  soma = soma + i

media = soma/len(lista)
print("A media é de: ", media)

print("")
print("Programa terminado!")

abaixo_media = []
acima_media = []

for nlista in lista:
  if nlista >= media:
    acima_media.append(nlista)
  else:
    abaixo_media.append(nlista)
    
print("Valores abaixo da media: ", abaixo_media)
print("")
print("Valores acima da media: ", acima_media)
print("")
print("Programa terminado!")

print("")
print("Programa terminado!")
