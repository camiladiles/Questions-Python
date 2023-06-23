'''Faça um programa que deverá pedir as 2 notas de uma aluna e calcular sua média. Considere que as notas serão de 0 a 100.

O programa deverá informar a média da aluna e seu status, obedecendo as regrinhas abaixo:

Aprovada, caso a média seja pelo menos 70.
Exame, caso a média seja pelo menos 30 e menor do que 70.
Reprovada caso a média seja inferior a 30.'''

#Resposta:

#Pergunta ao usuario:
Nota1 = float(input("Qual a sua primeira nota? "))
Nota2 = float(input("Qual a sua segunda nota? "))

media  = (Nota1 + Nota2)/2

#Formula para ver media e situação da aluna:
if 0 <= media <30:
  print("Sua média é ", media, " - Reprovada")
if 30 <= media <70:
  print("Sua média é ", media, " - Exame")
if 70 <= media <=100:
  print("Sua média é ", media, " - Aprovada")
