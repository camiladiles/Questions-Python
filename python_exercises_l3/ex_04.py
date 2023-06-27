'''Faça um programa que pede para a usuária digitar um número. O programa deverá exibir a tabuada daquele número.

Ex: se o número digitado for 5, a saída será:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50'''

#Resposta:

numero = int(input("Digite um número: "))
print("")
print("Tabuada do ", numero)
print("")

i = 1
while i <= 10:
  print (numero, "x", i, "=",numero * i )
  i = i + 1

print("Programa terminado")
