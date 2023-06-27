"""
Faça um programa que pede para a usuária digitar um número inteiro positivo. Seu programa deverá utilizar um laço do tipo for para responder a soma de do número com todos os seus antecessores positivos.

Ex: se o número digitado for 5, a conta a ser realizada será 5 + 4 + 3 + 2 + 1, e o resultado na tela será "15".
"""

#Resposta:

numero = int(input("Digite um número inteiro positivo: "))
print("")

suma = 0
for i in range (1, numero + 1):
  suma = suma + i
print("A soma dos", numero, "primeiros inteiros positivos é", suma)

print("")
print("Programa terminado")


#AQUI TEMOS O EXEMPLO COM WHILE
'''
numero = int(input("Digite um número inteiro positivo: "))
print("")

resultado_suma = 0
contador = 1

while contador <= numero:
    resultado_suma += contador
    contador = contador + 1

print("A soma dos", numero, "primeiros inteiros positivos é", resultado_suma)
'''
