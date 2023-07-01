"""
03. Faça um programa que percorre uma lista de números aleatórios (ver exercício 2) e exibe na tela apenas os números pares.
"""

#Resposta:

import random
lista = [] #lista vazia

for contador in range(0, 20):
  sorteio = random.randint(0, 100)
  lista.append(sorteio)
print("Lista: ", lista)
print("")
print("")

lista_par = []

for npar in lista:
  if npar % 2 == 0:
    lista_par.append(npar)
print("Números pares da lista: ", lista_par)

print("")
print("Programa terminado!")
