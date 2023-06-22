'''Um estacionamento cobra um valor mínimo de 10 reais, correspondente a 1h de uso. Cada hora adicional gera mais 5 reais de cobrança. Ex: um carro estacionado por 5 horas irá pagar 10 reais pela primeira hora + 5 reais pela segunda + 5 pela terceira + 5 pela quarta + 5 pela quinta, totalizando 30 reais.
Faça um programa que pergunte para a usuária quanto tempo seu carro ficou estacionado e responde o valor em reais a ser pago.
OBS: o estacionamento não considera minutos, tampouco horas fracionárias. Portanto, o seu programa não precisa se preocupar com isso. Se a pessoa ficou 5 horas e 2 minutos, ela passou de 5 horas, portanto ela deve digitar a hora inteira mais próxima: 6 horas.'''

# Resposta:

Horas = float(input("Quantas horas você ficou estadionado(a)?  "))
Valor_Pagar  = 5*Horas+5
print("O valor em Reais a ser pago é de R$ ", Valor_Pagar)
