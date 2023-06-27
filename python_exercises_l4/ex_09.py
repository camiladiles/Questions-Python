"""
9. Faça um programa que pergunta a quantidade de provas realizadas pela usuária.

O seu programa deverá ler as notas das provas pelo teclado e responder:

a média das provas
a maior nota
a menor nota
"""

#Resposta:

n_provas = int(input("Quantas provas você realizou?  "))
print("")

soma_notas = 0 #para guardar a soma das notas
maior = 0
menor = 0

for i in range(1, n_provas + 1):
  nota = float(input("Digite sua nota: "))
  soma_notas += nota
  if i == 1:
    maior = nota
    menor = nota
  else:
    if nota > maior:
      maior = nota
    if nota < menor:
      menor = nota
  
media = soma_notas / n_provas

print(" ")
print("A sua media é ", media)
print(" ")
print("O maior valor é ", maior)
print(" ")
print("O menor valor é ", menor)

print("")
print("Programa terminado")
