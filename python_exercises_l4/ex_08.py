"""
8. A constante π (leia "pi"), que representa a relação entre o comprimento de uma circunferência e o seu diâmetro, possui valor aproximado de 3.14159265.

Acredita-se que ele possui infinitas casas após o ponto decimal, sem repetição. Isso nos impede de determinar seu valor exato, mas há várias técnicas diferentes para calcular aproximações arbitrariamente boas.

Muitas dessas técnicas envolvem calcular a soma de sequências convergentes, isto é, sequências onde conforme somamos mais termos seguindo alguma regra, mais ela se aproxima de um valor específico.

Uma dessas técnicas é a Fórmula de Leibniz:

1- 1/3 + 1/5 - 1/7 + 1/9 - ... = pi/4
que também é:
π = 4 ( 1 - 1/3 + 1/5 - 1/7 + 1/9 - ... )

Note que existe uma regra fácil de deduzir para quais seriam os próximos denominadores e sinais. Quanto mais termos forem acrescentados, mais a soma se aproxima de π/4. Portanto, ao calcularmos essa soma com milhares ou milhões de termos e dividirmos o resultado por 4, devemos ter uma boa aproximação de π.

Faça um programa que pergunta para a usuária com quantos termos ela gostaria de fazer a conta. Seu programa deverá calcular π utilizando a fórmula de Leibniz com a quantidade de termos especificada pela usuária.

Desafio: quando seu programa estiver pronto, experimente alguns valores e veja quantos termos são necessários para determinar o valor de π com uma precisão que você considere satisfatória.
"""

#Resposta:

terminos = int(input("Com quantos termos você gostaria de fazer a conta: n =  "))
print("")

x = 1
π = 0

for i in range(terminos + 1):
  if i% 2 == 0:
    π += 4/x
  else:
    π -= 4/x
  x += 2
print("π = ",π)

print("")
print("Programa terminado")
print("")
print("")
print("Considero uma aproximação satisfatoria com aproximadamente 9500 terminos, para chegar pelo menos nas 3 primeiras casas decimais exatas do π, com a quarta casa decimal aproximada para 6.")
