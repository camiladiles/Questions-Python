'''Faça um programa que pergunta quantas provas a usuária fez. Em seguida, o programa deverá ler cada uma de suas notas pelo teclado e informar sua média.'''

#Resposta:

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
