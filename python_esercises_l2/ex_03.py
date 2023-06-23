#Faça um programa que pergunta o nome da usuária e o horário do dia (apenas horas, sem os minutos). O programa deverá responder:

#Bom dia, [nome]! caso o horário esteja entre 4 e 11.
#Boa tarde, [nome]! caso o horário esteja entre 12 e 17.
'''Boa noite, [nome]! caso o horário esteja entre 18 e 23 ou 0 e 3.
Horário inválido caso o horário seja superior a 23 ou inferior a 0.'''

#Resposta:
#Pergunta ao usuario:

nome = input("Qual o seu nome? ")
hora = int(input("Que horas são?"))

#Formula para ver dizer bom dia/tarde/noite
if 4<= hora<12:
  print("Bom dia, ", nome, "!")
if 12<= hora<18:
  print("Bom tarde, ", nome, "!")
if 18<= hora<23:
  print("Bom noite, ", nome, "!")
if hora>23 or hora<0:
  print ("Horario Invalido")
