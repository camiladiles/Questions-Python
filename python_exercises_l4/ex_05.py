"""
5. Uma progressão aritmética (PA) possui uma razão e um termo inicial.
Podemos chamar o termo inicial de termo 0.

Um termo "n" qualquer pode ser obtido somando a razão "n" vezes ao termo inicial.

Por exemplo, a PA com razão = 4 e termo inicial = 1 terá os seguintes termos:
1, 5, 9, 13, 17, 21, 25...
onde 1 é o termo 0, 5 é o termo 1, 9 é o termo 2, e assim sucessivamente.

Faça um programa que pergunta para a usuária:

a razão de uma PA
o termo inicial da PA
quantos termos ela gostaria de ver na tela
O seu programa deverá calcular e exibir os "n" termos solicitados pela usuária.
"""


#Resposta:

r = int(input("Digite a razão, r =  "))
a1 = int(input("Digite o termo inicial, a1 =  "))
n = int(input("Digite quantos termos você que ver, n =  "))
print("")

#forumla dos n terminos de uma PA
an = a1 + (n-1)*r

for i in range (a1, an + 1, r):
  print(i) 

print("")
print("Programa terminado")
