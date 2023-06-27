'''Modifique o programa anterior para, além de ler o valor final pelo teclado, ler também o valor inicial.
Ex: se os números digitados forem 5 e 10, será exibido: (5, 6, 7, 8, 9, 10)'''

#Resposta:

n_int_positivo1 = int(input("Digite um número inteiro positivo: "))
n_int_positivo2 = int(input("Digite outro inteiro positivo maior que o anterior: "))

i = n_int_positivo1
while i <= n_int_positivo2:
  print (i)
  i += 1

print("Programa terminado")

