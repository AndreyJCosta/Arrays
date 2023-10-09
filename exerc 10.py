#Exercício 10
#Faça um código para ler um valor N qualquer (que será o tamanho dos vetores). Após, ler dois
#vetores A e B (de tamanho N cada um) e depois armazenar em um terceiro vetor Soma a soma dos
#elementos do vetor A com os do vetor B (respeitando as mesmas posições) e escrever o vetor Soma.


listaN = int(input("Digite um valor qualquer para ser o tamanho da lista: "))
A=[" "]*listaN
B=[" "]*listaN
for x in range(listaN):
    A[x]=int(input(f"Digite o {x + 1}ª valor para lista A: "))
print()
for c in range(listaN):
    B[c]=int(input(f"Digite o {c + 1}º valor para lista B: "))
soma=[" "]*listaN
for d in range(listaN):
    soma[d]=A[d]+B[d]
print()
print(f"A soma dos vetores da lista A e da Lista B é: {soma}")