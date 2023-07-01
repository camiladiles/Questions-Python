"""
04. Faça um programa que calcula a média dos números de uma lista numérica.
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
