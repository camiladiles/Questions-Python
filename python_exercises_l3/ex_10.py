'''Bibliotecas ou módulos são arquivos contendo algumas funções e outros componentes de código já prontos para serem reutilizados. A linguagem Python já possui diversos módulos pré-instalados, e podemos utilizá-los através do comando import.

Ao incluir a linha abaixo (preferencialmente no topo do programa) podemos acessar as funções do módulo random, que permitem lidar com números aleatórios:

import random

Tendo importado esse módulo em nosso programa, é possível sortear números aleatórios através da função randint. No exemplo abaixo, um número aleatório entre 1 e 100 é salvo na variável "sorteio":

sorteio = random.randint(1, 100)

Faça um programa que sorteia um número aleatório entre 1 e 100. Ele deve pedir para o usuário adivinhar o número até que ele acerte.'''

#Resposta:

import random

sorteio = random.randint(1, 100)
print(sorteio)

#Pergunta ao usuario:
numero_sorteado = int(input("Qual o numero sorteado? "))
print('')

while sorteio != numero_sorteado:
    print("tente outra vez!")
    numero_sorteado = int(input("Qual o numero sorteado? "))
    print(' ')
if numero_sorteado == sorteio:
  print("Muito bem, o número é ", sorteio, ".")
