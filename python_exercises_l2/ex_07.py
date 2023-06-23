'''Faça um programa que pergunta o comprimento de cada um dos 3 lados de um triângulo.

O programa deverá responder:
É triângulo, caso nenhum dos lados possua comprimento superior à soma dos outros dos lados.

Não é triângulo, caso um dos lados seja possua comprimento superior à soma dos outros dois lados.

Exemplos: 
- Se os lados forem 3, 4 e 5 o triângulo existe, pois:
5 < 3 + 4
4 < 3 + 5
3 < 4 + 5

- Já se os supostos lados forem 2, 5 e 2, o triângulo não existe, pois: 
5 > 2 + 2'''

#Resposta:
#Pergunta ao usuario:
print("Vamos ver se é ou não é triangulo:")
print("")
L1 = float(input("Em metros, qual o comprimento do lado 1 de um triangulo? "))
L2 = float(input("Em metros, qual o comprimento do lado 2 de um triangulo? "))
L3 = float(input("Em metros, qual o comprimento do lado 3 de um triangulo? "))


#Formula saber si é ou não triangulo:
if L1 < L2 + L3 and L2 < L1 + L3 and L3 < L1 + L2:
  print("É triângulo")
else:
  print("Não é triangulo")
