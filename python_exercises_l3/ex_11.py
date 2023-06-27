'''Juros de novo! :)

Pergunte para a usuária o valor que será investido em uma aplicação, a taxa de juros ao mês e o tempo que o dinheiro ficará aplicado.

Seu programa deverá exibir quanto de juros será pago e o saldo total em cada mês.

Exemplo: 10000.0 reais, 5% de juros ao mês, 3 meses.

Mês 1: Juros: 500.0 reais, saldo: 10500.0 reais
Mês 2: Juros: 525.0 reais, saldo: 11025.0 reais
Mês 3: Juros: 551.25 reais, saldo: 11576.25 reais'''

#Resposta:

#Pergunta ao usuario:
Valor_Aplicar = float(input("Quanto dinheiro você irá aplicar?  "))
Taxa_Juros = float(input("Qual é a taxa de juros (em %) ao mês?  "))
Numero_Meses = int(input("Qual a duração da aplicação em quantidade de meses?  "))
print('')

print("Você informou: R$", Valor_Aplicar, ",", Taxa_Juros, "% de juros ao mês, por", Numero_Meses, "meses." )
print('')

#Variaveis importantes
Juros_anterior = 0
i = 1

#calculos para encontrar os resultados
while i <= Numero_Meses:
  Valor_Sacado  = Valor_Aplicar*((1+(Taxa_Juros/100))**i)
  Juros = (Valor_Sacado - Valor_Aplicar) - Juros_anterior
  print (f"Mês {i}: Juros R$ {Juros:.02f}, saldo: R$ {Valor_Sacado:.02f} reais")

  Juros_anterior += Juros
  i = i + 1
