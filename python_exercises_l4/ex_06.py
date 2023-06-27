"""
6. Uma progressão geométrica (PG) possui uma razão e um termo inicial.
Podemos chamar o termo inicial de termo 0.
Um termo "n" qualquer pode ser obtido multiplicando a razão "n" vezes ao termo inicial.
Por exemplo, a PA com razão = 2 e termo inicial = 3 terá os seguintes termos:
3, 6, 12, 24, 48, 72...
onde 3 é o termo 0, 6 é o termo 1, 12 é o termo 2, e assim sucessivamente.
Faça um programa que pergunta para a usuária:

a razão de uma PG 
o termo inicial da PG
quantos termos ela gostaria de ver na tela
O seu programa deverá calcular e exibir os "n" termos solicitados pela usuária.
"""

#Resposta:

q = int(input("Digite a razão, q =  "))
a1 = int(input("Digite o termo inicial, a1 =  "))
n = int(input("Digite quantos termos você que ver, n =  "))
print("")

for i in range(1, n + 1):
  potencia = i - 1
  pg = a1 * q ** potencia
  print(pg)

print("")
print("Programa terminado")
