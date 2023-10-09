# Exercício 05
#Ler um vetor A de 10 números. logo em seguida, ler mais um número e guardar em uma variável X.
#Armazenar em um vetor M o resultado de cada elemento de A multiplicado pelo
#valor X. Logo após, imprimir o vetor M.


A = [" "] * 10
for b in range(10):
    A[b] = int(input(f"Digite o {b + 1}º Número: "))
print()
X = int(input("Digite o valor para multiplicar cada elemento da lista: "))
M = [" "] * 10
for c in range(10):
    M[c]=A[c]*X
print()
print("///" *20)
print()
print(f"Os valores ta lista foi {A}\n\o/\nO multiplicador foi {X}\n\o/\nLista multiplicada: {M}")