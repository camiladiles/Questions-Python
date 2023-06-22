'''Vamos fazer um programa para calcular o rendimento de uma aplicação.

Faça um programa que pergunta quanto dinheiro a usuária irá aplicar, a taxa de juros ao mês (em %) e a duração da aplicação (em meses).

Seu programa deve responder as seguintes informações:
Qual o valor total a ser sacado pela usuária ao final da aplicação?
Quantos reais a pessoa recebeu apenas de juros?
Quantos % a aplicação rendeu no total?

Atenção: ao buscar as fórmulas para utilizar no problema, busque pela fórmula de juros compostos. Não utilize a fórmula de juros simples.'''

# Resposta:

print("Rendimento de uma aplicação")

Valor_Aplicar = float(input("Quanto dinheiro você irá aplicar?  "))
Taxa_Juros = float(input("Qual é a taxa de juros (em %) ao mês?  "))
Numero_Meses = int(input("Qual a duração da aplicação em quantidade de meses?  "))


Valor_Sacado  = Valor_Aplicar*((1+(Taxa_Juros/100))**Numero_Meses)
Valor_Juros = Valor_Sacado - Valor_Aplicar
Valor_Rendeu = ((Valor_Sacado*100)/Valor_Aplicar)-100


print("O valor total a ser sacado ao final desta aplicação e de R$ ", Valor_Sacado)
print("O valor total de juros recebidos foi de R$ ", Valor_Juros)
print("Sua aplicação rendeu um total de ", Valor_Rendeu, "% ao final desta aplicação.")
