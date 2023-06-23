'''Faça um programa que pede para a usuária digitar um número e responde se o número é par ou ímpar.'''

#Resposta:
#Pergunta ao usuario:
numero = int(input("Digite um número inteiro positivo:  "))

#Formula para ver se é impar ou par
if (numero%2) == 0:
  print("Par")
else:
  print ("Impar")
