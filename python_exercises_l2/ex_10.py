'''Faça um programa que pergunta um ano para a usuária e responde se ele é bissexto ou não.

- A regra geral para determinar se um ano é bissexto é: todo ano divisível por 4, a princípio, é bissexto: 2016, 2020, 2024...

- Porém existe uma exceção: anos divisíveis por 100 não são bissextos. O ano 2100, por exemplo, é divisível por 4, mas como também é divisível por 100, ele não pode ser bissexto.

- A exceção possui uma exceção: anos divisíveis por 400 são bissextos. O ano 2000, por exemplo, é divisível por 100. Porém, como ele também é divisível por 400, ele torna-se bissexto.'''

#Resposta:
#Significa que se o ano é multiplo de 4 e não de 100 ou se é multiplo de 400 será bissexto, os demais casos serão falsos.

#Pergunta ao usuario:
print("Descobrindo se o ano é ou não")
print("BISSEXTO")
print("")
ano = int(input("Digite um ano: "))

#resultados:
if (ano%4==0 and ano%100!=0) or (ano%400==0):
  print("Este ano ", ano, " é BISSEXTO: ")

else:
  print("O ano ", ano, " não é BISSEXTO")
