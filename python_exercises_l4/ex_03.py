"""
Faça um programa que pede para a usuária digitar um número inteiro positivo. O programa deverá utilizar um laço do tipo for para calcular e exibir na tela o fatorial do número digitado.

Lembrete: o fatorial de um número "n", denotado por "n!", é o produto dele com todos os seus antecessores inteiros positivos.

Ex: 5! = 1 x 2 x 3 x 4 x 5
"""

#Resposta:

numero = int(input("Digite um número inteiro positivo: "))
print("")

fatorial = 1
for i in range (1, numero + 1):
  fatorial = fatorial * i
print("O fatorial do número ", numero, " representado por: ", numero, "! = ", fatorial)

print("")
print("Programa terminado")

#AQUI TEMOS O EXEMPLO COM WHILE
'''
numero = int(input("Digite um número inteiro positivo: "))
print("")

resultado_fatorial = 1
contador = 1

while contador <= numero:
    resultado_fatorial *= contador
    contador += 1

print("O fatorial do número ", numero, " representado por: ", numero, "! = ", resultado_fatorial)

'''
