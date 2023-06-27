"""
7. A sequência de Fibonacci é definida da seguinte maneira:

Termo(0) = 1
Termo(1) = 1
Termo(n) = Termo(n-1) + Termo(n-2)
Ou seja, temos 2 termos iniciais que valem 1, e o restante dos termos é definido pela soma dos dois antecessores. Os primeiros termos da sequência são:

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...

Note que qualquer termo da sequência equivale à soma dos dois antecessores.

Faça um programa que pergunta para a usuária quantos termos da sequência de Fibonacci ela gostaria de ver. O seu programa deverá calcular e exibir a quantidade de termos desejada por ela.
"""

#Resposta:

n = int(input("Digite quantos termos da sequência de Fibonacci você que ver, n =  "))
print("")

a1 = 1
a2 = 1
soma = 0

for i in range(1, n + 1):
  print(soma)
  a1 = a2
  a2 = soma
  soma = a1 + a2

print("")
print("Programa terminado")
