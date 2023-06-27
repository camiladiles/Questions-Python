'''Modifique o programa anterior para perguntar também o "passo", ou seja, de quantas em quantas unidades a contagem irá saltar.

Ex: se forem digitados o valor inicial 5, o valor final 20 e o passo 3, serão exibidos: 
5
8
11
14
17
20'''

#Resposta:

n_int_positivo1 = int(input("Digite um número inteiro positivo: "))
n_int_positivo2 = int(input("Digite outro inteiro positivo maior que o anterior: "))
saltos = int(input("De quantos em quantos números vai saltar?  "))


i = n_int_positivo1
while i <= n_int_positivo2:
  print (i)
  i += saltos

print("Programa terminado")
