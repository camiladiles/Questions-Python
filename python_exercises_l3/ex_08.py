'''Iremos novamente fazer o programa da média do exercício anterior, mas com uma diferença: agora não iremos perguntar a quantidade de notas. A usuária deverá digitar uma nota negativa quando desejar parar de digitar mais notas.

Atenção: o número negativo não deve ser considerado uma nota (portanto, não deve interferir na média).'''

#Resposta:

nota = 0
numero = 0
soma_notas = 0 #para guardar a soma das notas
contador = 1

while nota >= 0:
  nota = float(input("Digite sua nota: "))
  if nota >= 0:
    soma_notas += nota
    numero = numero + 1
    contador += 1
    
media = (soma_notas) / (numero)

print(" ")
print("A sua media é ", media)
