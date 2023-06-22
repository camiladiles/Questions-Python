'''Faça um programa que pergunta a temperatura em graus Celsius e responde a temperatura correspondente em graus Fahrenheit.

Dica: se você digitar converta celsius para fahrenheit no Google, ele irá exibir a fórmula que você utilizará em seu programa e uma calculadora que pode auxiliar você na hora de testar seu programa.'''

# Resposta:

Temperatura = float(input("Qual é a temperatura em grados celsius?  "))
fahrenheit  = ((9/5)*Temperatura) + 32
print("A temperatura em fahrenheit é ", fahrenheit)
