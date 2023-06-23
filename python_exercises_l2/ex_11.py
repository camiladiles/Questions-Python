'''Um banco oferece as seguintes opções de aplicação de renda fixa:

Fundo A: aceita aplicações a partir de 50 reais, não possui tempo mínimo de aplicação e rende 10% ao ano.
Fundo B: aceita aplicações a partir de 100 reais, possui tempo mínimo de aplicação de 1 ano e rende 12% ao ano.
Fundo C: aceita aplicações a partir de 500 reais, possui tempo mínimo de aplicação de 2 anos e rende 13% ao ano.
Fundo D: aceita aplicações a partir de 1000 reais, possui tempo mínimo de aplicação de 3 anos e rende 15% ao ano.
Fundo E: aceita aplicações a partir de 3000 reais, possui tempo mínimo de aplicação de 5 anos e rende 18% ao ano.

- Faça um programa que pergunta para a usuária em qual fundo ela deseja aplicar seu dinheiro, quanto dinheiro ela possui e o tempo que ela pretende deixar o dinheiro aplicado (em anos).

Caso o valor e o tempo estejam adequados às regras do fundo selecionado, utilize a fórmula dos juros compostos para informar para ela o valor total que ela irá sacar ao final do período informado por ela.

Caso contrário, exiba a mensagem Não é possível realizar essa aplicação.'''

#Resposta:
#Pergunta ao usuario:
print("Aplicação de renda fixa")
print("")
fundo = str(input("Em que fundo você gostaria de aplicar seu dinheiro? (Digite: A, B, C, D ou E): "))
Valor_Aplicar = float(input("Quantos reais você gostaria de aplicar? "))
tempo = int(input("Quanto tempo você gostaria de deixar seu dinheiro aplicado (em anos)? "))

#resultados:
if fundo == 'A' and Valor_Aplicar >= 50:
  Valor_Sacado  = Valor_Aplicar*((1+(0.1))**tempo)
  print("O valor total a ser sacado ao final desta aplicação e de R$ ", Valor_Sacado)

if fundo == 'B' and Valor_Aplicar >= 100 and tempo >= 1:
  Valor_Sacado  = Valor_Aplicar*((1+(0.12))**tempo)
  print("O valor total a ser sacado ao final desta aplicação e de R$ ", Valor_Sacado)

if fundo == 'C' and Valor_Aplicar >= 500 and tempo >= 2:
  Valor_Sacado  = Valor_Aplicar*((1+(0.13))**tempo)
  print("O valor total a ser sacado ao final desta aplicação e de R$ ", Valor_Sacado)

if fundo == 'D' and Valor_Aplicar >= 1000 and tempo >= 3:
  Valor_Sacado  = Valor_Aplicar*((1+(0.15))**tempo)
  print("O valor total a ser sacado ao final desta aplicação e de R$ ", Valor_Sacado)

if fundo == 'E' and Valor_Aplicar >= 3000 and tempo >= 5:
  Valor_Sacado  = Valor_Aplicar*((1+(0.18))**tempo)
  print("O valor total a ser sacado ao final desta aplicação e de R$ ", Valor_Sacado)

else: 
  print("Não é possível realizar essa aplicação")
