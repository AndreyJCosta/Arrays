#Exercicio 02
#altere o exercício anterior e mostre na tela,
# ao final, o nome de cada aluno e sua
#respectiva posição no array.

quant=int(input("Digite a quantidade de alunos: "))
nomes=[" "]*quant
for x in range (quant):
    nomes[x]=input(f" Digite o {x+1}º Aluno: ")
for a in range (quant):
    print(f'{nomes[a]} e esta na posiçaõ {a} ')
