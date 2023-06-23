'''Modifique o programa das médias do exercício anterior da seguinte maneira:

Caso a aluna tenha ficado de exame, pergunte a nota do exame.
Uma nova média deve ser calculada entre a média original e a nota do exame:
media_exame = (media + exame)/2
O programa deve exibir essa nova média junto do novo status:
Aprovada por exame caso a media_exame seja pelo menos 50.
Reprovada caso a media_exame seja inferior a 50.'''

#Resposta:

#Pergunta ao usuario:
Nota1 = float(input("Qual a sua primeira nota? "))
Nota2 = float(input("Qual a sua segunda nota? "))

media  = (Nota1 + Nota2)/2

#Formula para ver media e situação da aluna:
if 0 <= media <30:
  print("Sua média é ", media, " - Reprovada")
if 30 <= media <70:
  print("Sua média é ", media, " - Exame")

  exame = float(input("Qual a nota do seu exame? "))
  final = (media + exame)/2
  if final < 50:
    print("Nota: ", final, "Reprovada") 
  if final >= 50:
      print ("Nota: ", final, "Aprovada")
if 70 <= media <=100:
  print("Sua média é ", media, " - Aprovada")
