'''Vai um cupom de desconto aí?

Faça um programa que pergunta o preço de um produto, o desconto a ser aplicado (em %) e responde o valor total a ser pago.'''

# Resposta:

Celular = float(input("Qual custa este celular?  "))
Desconto = float(input("Quantos % de desconto tem?  "))
valor_final  = (Celular*(100-Desconto))/100
print("O valor a ser pago desse celular com o desconto de ", Desconto, "% é de R$", valor_final)
