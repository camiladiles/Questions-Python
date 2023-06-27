"""
Faça um programa que pede para a usuária digitar um número. O programa deverá utilizar um laço do tipo for para exibir a tabuada daquele número.

Ex: se o número digitado for 5, a saída será:
"""

#Resposta:

numero = int(input("Digite um número para ver sua tabuada: "))
print("")
print("Tabuada do ", numero)
print("")

for multiplicador in range (1, 11):
  produto = numero * multiplicador
  print(numero, "x", multiplicador, "=", produto)

print("")
print("Programa terminado")

#AQUI TEMOS O EXEMPLO COM WHILE
"""
i = 1
while i <= 10:
  print (numero, "x", i, "=",numero * i )
  i = i + 1

print("Programa terminado")
"""
