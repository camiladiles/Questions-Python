"""
09. Crie uma tabela de preços (pode ser fixa no seu código) usando lista de listas.

Ela pode ser implementada da seguinte maneira: cada "lista interna" é uma lista de 2 elementos: na posição 0 temos o nome do produto, na posição 1 temos o preço.

Ex:
produtos = [
    ['Chocolate', 5.12],
    ['Doritos', 15.25],
    ['Fandangos', 7.54],
]

Faça um programa que permita consultar valores na lista.

Ele deverá perguntar para a usuária o nome do produto que ela deseja consultar. Caso o produto exista na lista, seu preço será exibido. Caso contrário, a mensagem "produto não encontrado" será exibida.

O programa deverá repetir a pergunta após mostrar o resultado, até que a usuária digite "sair".
"""
#Resposta: (En construção)

'''IDEIA 9: 

produtos=[['Chocolate', 5.12],['Doritos', 15.25],['Fandangos', 7.54]]

nome=input('Boa tarde. Digite seu nome')
i=0
x=True

while x==True:
  prod=input('Qual produto deseja consultar?'
  if prod in produtos:
      i+=1
      print('O valor de ', prod,'é', produtos[i])
    else:
      print(nome,'Infelizmente não temos esse produto')
  s=input('Deseja consultar novamente? Se não, digite SAIR')
  if s=='SAIR':
    x=False
'''

