'''Faça um programa que pergunta a temperatura em graus Fahrenheit e responde a temperatura correspondente em graus Celsius.

Atenção: apenas trocar "celsius" e "fahrenheit" na equação utilizada no exercício anterior não é a solução. Você deve realizar a inversão completa da fórmula (ou utilizar o mesmo truque para consultar essa fórmula no Google).'''

# Resposta:

Temperatura = float(input("Qual é a temperatura em grados fahrenheit?  "))
celsius  = (Temperatura - 32)*5/9
print("A temperatura em celsius é ", celsius)
