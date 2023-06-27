'''Faça um programa que pede para a usuária digitar um número inteiro positivo. O programa deve exibir todos os números inteiros de 0 até o número digitado.

Ex: se o número for 5, será exibido:'''
#Resposta:

n_int_positivo = int(input("Digite um número inteiro positivo: "))

i = 0 
while i <= n_int_positivo:
  print (i)
  i += 1

print("Programa terminado")
