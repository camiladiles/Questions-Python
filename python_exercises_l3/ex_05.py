'''Faça um programa que pede para a usuária digitar um número inteiro positivo. Seu programa deverá responder a soma de do número com todos os seus antecessores positivos.

Ex: se o número digitado for 5, a conta a ser realizada será 5 + 4 + 3 + 2 + 1, e o resultado na tela será "15".'''

#Resposta con y sem WHILE:

#Resposta sem WHILE
numero = int(input("Digite um número inteiro positivo: "))
print("")

soma = numero * (numero + 1) // 2 

print("A soma dos", numero, "primeiros inteiros positivos é", soma)

#Resposta com WHILE
numero = int(input("Digite um número inteiro positivo: "))
print("")

resultado_suma = 0
contador = 1

while contador <= numero:
    resultado_suma += contador
    contador = contador + 1

print("A soma dos", numero, "primeiros inteiros positivos é", resultado_suma)

'''[INFORMAÇÃO IMPORTANTE] Lembrando que:
resultado *= count é o mesmo que: resultado = resultado * count
Ou seja, o novo valor de 'resultado' vai ser o valor antigo multiplicado por 'count'.
Já: count += 1 significa: count = count + 1
Ou seja, estamos incrementando o valor de 'count' em uma unidade, a cada iteração do laço WHILE.
'''
