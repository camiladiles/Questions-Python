'''Faça um programa que pede para a usuária digitar, separadamente, os coeficientes a, b e c de uma equação de segundo grau.

- O programa deverá calcular o valor do discriminante (delta) e:
- Caso seja positivo, o programa deverá calcular e exibir na tela os valores de suas duas raizes reais e distintas.
- Caso seja zero, o programa deverá calcular e exibir na tela a sua única raiz.
- Caso seja negativo, o programa deverá exibir a mensagem Não possui raizes reais.'''

#Resposta:

#Pergunta ao usuario:
print("Calculando o discriminante DELTA:")
print("Quais são os coeficientes a, b, c de uma equação do segundo grau")
print("")
a = float(input("Digite o valor de a (não pode ser 0): "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

#calculando DELTA:
delta = (b**2) - (4*a*c)
print("o Valor de delta é: ", delta)

if delta > 0:
  x1 = (-b + delta**(1/2))/(2*a)
  x2 = (-b - delta**(1/2))/(2*a)
  print("As raízes são: ", x1, "e", x2)
  
if delta == 0:
  x = -b/2*a
  print(x)

else:
  print("Não possui raizes reais.")
