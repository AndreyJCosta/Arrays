#Exercicio01
#Perguntar ao usuario quantos alunos tem na salae criar um
#array unidimensional (Vetor) com o nome qde todos os Alunos da sala.

quant=int(input("Digite a quantidade de alunos: "))
nomes=[" "]*quant
for x in range (quant):
    nomes[x]=input(f" Digite o {x+1}º Aluno: ")
for a in range (quant):
    print(f'{nomes[a]} ')



