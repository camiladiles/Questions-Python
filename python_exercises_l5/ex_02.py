"""
02. Faça um programa que preenche uma lista inicialmente vazia com 20 números aleatórios entre 0 e 100.

Você pode utilizar a biblioteca random para isso. Comece importando-a no início de seu código:

import random
Para sortear um número, você pode usar a linha abaixo:

sorteio = random.randint(0, 100)

DICA: em todos os programas desta lista de exercícios onde você tiver que trabalhar com uma lista numérica onde os números não serão digitados pela usuária, você pode replicar o código deste exercício para partir de uma lista já preenchida com valores aleatórios. Isso facilitará os seus testes!
"""

#Resposta:

import random
lista = [] #lista vazia

for contador in range(0, 20):
  sorteio = random.randint(0, 100)
  lista.append(sorteio)
print(lista)
  
print("")
print("Programa terminado!")
