'''Modifique o programa dos triângulos do exercício anterior da seguinte maneira:

- Caso o programa tenha determinado que o triângulo existe, informe também o seu tipo:

- Equilátero, caso os 3 lados sejam iguais
- Isósceles, caso apenas 2 lados sejam iguais
- Escaleno, caso todos os lados sejam diferentes entre si'''

#Resposta:

#Pergunta ao usuario:
print("Vamos ver se é ou não é triangulo:")
print("")
L1 = float(input("Em metros, qual o comprimento do lado 1 de um triangulo? "))
L2 = float(input("Em metros, qual o comprimento do lado 2 de um triangulo? "))
L3 = float(input("Em metros, qual o comprimento do lado 3 de um triangulo? "))


#Formula saber tipo de triangulo:
if L1 < L2 + L3 and L2 < L1 + L3 and L3 < L1 + L2:
  print("É triângulo")
  if L1 == L2 == L3:
    print("Equilatéro")
  if (L1 == L2 and L1 != L3) or (L1 == L3 and L1 != L2) or (L2 == L3 and L2 != L1):
    print("Isósceles")
  elif L1 != L2 and L1 != L2 and L2 != L3:
    print("Escaleno")
else:
  print("Não é triangulo")
