#Exercício 13
#Faça um algoritmo que leia 30 valores do tipo inteiro e armazene-os em um vetor.
#A seguir, o algoritmo deverá informar (1) todos os números pares que existem no vetor;
#(2) o menor e o maior valor existente no vetor;
#(3) quantos dos valores do vetor são maiores que a média desses valores:


valor=[" "]*5
valorMaior=0
valorMenor=0
soma=0
pares=[" "]*5

for x in range(5):
    valor[x]=int(input(f"Digite o {x + 1}º valor: "))
    if x == 0:
        valorMenor = valor[x]
    soma+=valor[x]

    if valor[x] > valorMaior:
        valorMaior=valor[x]

    if valor[x] < valorMenor:
        valorMenor=valor[x]

media=soma/5
cont=0

for a in range (5):
    if valor[a] > media:
        cont+=1

for b in range (5):
    if valor[b] % 2 ==0:
        pares[b]=valor[b]

print()
print(f"Os numeros pares são: ")
for c in range (5):
    print(pares[c], end=" ")
print()
print(f" O menor de todo é o --> {valorMenor}.\n\o/\n"
      f"O maior de todos é o --> {valorMaior}.\n\o/\n"
      f"No total existem '{cont}' numeros que são maiores que a media que é --> {media}.")

print()
print("Até que fim eu conseguir!!!!!")





