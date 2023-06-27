"""
4. Faça um programa que pergunta quantas provas a usuária fez. Em seguida, o programa deverá utilizar um laço for para ler cada uma de suas notas pelo teclado e informar sua média.
"""

#Resposta:

numero = int(input("Quantas provas você fez? "))
print("")

soma_notas = 0 #para guardar a soma das notas
for i in range (1, numero + 1):
  nota = float(input("Digite sua nota: "))
  soma_notas += nota

media = soma_notas / numero

print(" ")
print("A sua media é ", media)

print("")
print("Programa terminado")


#AQUI TEMOS O EXEMPLO COM WHILE
'''
numero = int(input("Quantas provas você fez? "))
print("")

soma_notas = 0 #para guardar a soma das notas
contador = 1

while contador <= numero:
  nota = float(input("Digite sua nota: "))
  soma_notas += nota
  contador += 1

media = soma_notas / numero

print(" ")
print("A sua media é ", media)
'''
