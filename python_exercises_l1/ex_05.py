#Faça um programa que pergunte para a motorista a distância que ela dirigiu e o tempo que seu trajeto levou, e responda sua velocidade média.

#Resposta:

print("Colocar como resposta apenas o número da distancia e do tempo solicitado")
Distancia = float(input("Qual a distancia em kilometros que você dirigiu?  "))
Tempo = float(input("Quanto tempo em horas você demorou? "))
Velocidade_Media  = Distancia/Tempo
print("Sua velocidade média foi de ", Velocidade_Media, "km/h")
