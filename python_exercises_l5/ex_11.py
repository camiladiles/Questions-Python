"""
11. Nesta questão, reaproveite o código da questão avaliada da lista de exercícios anterior!

Modifique seu código para, ao invés de exibir a tabela Price na tela, armazenar a tabela utilizando uma lista de listas.

Cada "lista interna" deve conter juros daquele mês, amortização daquele mês, valor da prestação e saldo devedor.

Todas essas listas deverão ser adicionadas, na ordem correta, em uma lista geral, que será nossa tabela.

Uma vez criada e calculada toda a tabela, pergunte (em loop) para a usuária qual mês ela deseja consultar e mostre para ela quanto de juros serão pagos, quanto será amortizado e qual será o seu saldo devedor naquele mês. Caso ela digite um mês inválido, informe para ela que aquele mês não existe. Caso ela digite um mês negativo, encerre o programa.
"""

#Resposta:

tebela_price = []

#Pergunta ao usuario:
print("Por favor, informe os seguintes dados:")
print("")
PV = float(input("Valor do emprestimo? PV = "))
i = float(input("Qual é a taxa de juros (em %) ao mês? i = "))
n = int(input("Qual a duração da aplicação em quantidade de meses? n =  "))
print('')

print("Você informou: R$", PV, ",", i, "% de juros ao mês, por", n, "meses." )
print('')

#Variaveis importantes
i = i/100
a = (1+i)**n*i
b = (1+i)**n-1
P  = PV*a/b


#calculos para encontrar os resultados
for x in range(1, n+1):
  lista = []
  j = PV * i
  
  A = P - j
  PV = PV - A
  deve = PV
  lista.append(x)
  lista.append(j)
  lista.append(A)
  lista.append(P)
  lista.append(deve)
  print(lista)
  print("")


tebela_price.append(lista)
print(tebela_price)

print("")
mes_consulta = float(input("Qual mês você deseja consultar: "))



#print (f"Parcela {x} | J: R$ {j:.02f} | A: R$ {A:.02f} | Pgto: R$ {P:.02f} | Deve: R$ {deve:.02f}")

print("")
print("Programa terminado")

