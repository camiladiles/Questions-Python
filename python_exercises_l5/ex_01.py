"""
01. Faça um programa que pede para a usuária digitar dois números, inicio e fim.

O seu programa deverá preencher uma lista com todos os números no intervalo (inclusive os valores inicial e final) e exibi-la na tela.
"""

#Resposta:

lista = [] #lista vazia
numeroi = int(input("Digite um número inicial: "))
lista.append(numeroi)
numerof = int(input("Digite um número final:"))
lista.append(numerof)
print("")

for contador in range (numeroi, numerof+1):
  print(contador)

print("")
print("Programa terminado!")
