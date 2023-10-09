#Exercício 03
#altere o exercício anterior para permitir
#achar o nome de um aluno na lista

cont=0
quant=int(input("Digite a quantidade de Alunos: "))
nomes=[" "]*quant
for x in range (quant):
    nomes[x]=input(f" Digite o nome do {x+1}º Aluno: ")
for a in range (quant):
    print(f" {nomes[a]} esta na posiçaõ {a}.")
print()
print("==="*20)
print()
pesquisa=input("Digite o nome do Aluno para ver se ele esta na sala: ")
for b in range (quant):
    if nomes[b] == pesquisa:
        print(f" {pesquisa} esta na lista na posiçaõ {a}. ")
        cont=cont+1
if cont == 0:
    print(f" O nome {pesquisa} não está na lista!")