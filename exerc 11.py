#Exercício 11
#Faça um código para ler um vetor de 30 números. Após isto, ler mais um número
#qualquer, calcular e escrever quantas vezes esse número aparece no vetor.


num=[" "]*30
for x in range(30):
    num[x]=int(input(f"Digite o {x + 1}ª número:  "))
cont= 0
print()
numEscolha=int(input("Escolha um número para saber quantas vezes ele apareceu no vetor: "))
print()
for a in num:
    if a == numEscolha:
        cont+=1
print()
print(f" O Nº {numEscolha} apareceu {cont}x no vetor.")