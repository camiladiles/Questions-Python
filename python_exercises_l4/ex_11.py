"""
11. Vamos implementar uma Tabela Price.

A tabela Price é utilizada em empréstimos de longo prazo, como no financiamento de um imóvel.

Um empréstimo pelo sistema Price utiliza prestações com valor fixo, isto é, você sempre irá pagar o mesmo valor todo mês.

Porém, uma taxa de juros corrige o seu saldo devedor, sendo assim, parte do valor que você paga no mês serve apenas para pagar juros, e outra parte realmente reduz o seu sald devedor. Essa redução é a chamada amortização.

Como o saldo devedor diminui com o tempo, a parcela de juros diminui a cada mês, nos primeiros meses a maior parte do valor pago por mês serve para pagar juros, enquanto mais próximo do final, a maior parte do valor está de fato amortizando a dívida.

Você pode aprender mais sobre as colunas da tabela e o cálculo para determinar o valor das prestações neste site.: https://mundoeducacao.uol.com.br/matematica/tabela-price.htm  

Conhecendo o valor fixo, como fazemos para determinar quanto de amortização, quanto de juros e qual o novo saldo devedor a cada mês?

Primeiro aplica-se a taxa de juros sobre o saldo devedor (multiplicar por i). Esse valor é o valor de juros pagos no mês. Subtraindo-se os juros do valor da prestação, descobre-se o quanto se amortizou naquele mês. O novo saldo devedor é obtido subtraindo a amortização do valor.

Faça um programa que pergunta:

o valor de um empréstimo
a taxa de juros do empréstimo
o tempo para pagamento
O seu programa deverá imprimir na tela uma "tabela" mostrando, mês a mês, o saldo devedor, juros, amortização e o valor da prestação.

Exemplo: para 10000.0 reais em 12 meses com juros de 1%:

Parcela 1 | J: 100.00 | A: 788.49 | Pgto: 888.49 | Deve: 9211.51
Parcela 2 | J: 92.12 | A: 796.37 | Pgto: 888.49 | Deve: 8415.14
Parcela 3 | J: 84.15 | A: 804.34 | Pgto: 888.49 | Deve: 7610.80

A tabela utilizada como exemplo encontra-se neste link e você pode usá-la para validar o seu programa.: https://www.hashtagtreinamentos.com/tabela-price-e-sac-no-excel
"""

#Resposta:

#Pergunta ao usuario:
print("Por favor, informe os seguintes dados:")
print("")
PV = float(input("Quanto dinheiro você irá aplicar? PV = "))
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
  j = PV * i
  
  A = P - j
  PV = PV - A
  deve = PV


  print (f"Parcela {x} | J: R$ {j:.02f} | A: R$ {A:.02f} | Pgto: R$ {P:.02f} | Deve: R$ {deve:.02f}")

print("")
print("Programa terminado")
