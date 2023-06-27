"""
10. Faça um programa que pede para a usuária digitar uma base e um expoente.

O seu programa deverá responder o resultado da operação de potência entre os números digitados sem utilizar o operador ** do Python.

lebrando que: b^e = bxbxbxbxb ( e vezes)
"""

#Resposta:

b = int(input("Digite uma base: b =  "))
e = int(input("Digite uma base: e =  "))
print("")

p = 1 #potencia

for i in range(e):
  p = p * b
  i += 1

print(b,"^",e,"=",p)
  

print("")
print("Programa terminado")
