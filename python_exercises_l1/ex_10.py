'''Vamos falar de coisa boa: aumento salarial!

Faça um programa que pergunta o salário da funcionária, o aumento a ser aplicado (em %) e responde o seu novo salário.'''

# Resposta:

Salario_Atual = float(input("Qual o valor do seu salario atual?  "))
Aumento = float(input("Quantos % vai aumentar?  "))
Salario_Final  = (Salario_Atual*(100+Aumento))/100
print("O valor do seu salario com um aumento de ", Aumento, "% é de R$", Salario_Final)
