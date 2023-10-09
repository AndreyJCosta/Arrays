#Exercício 12
#Escreva um algoritmo que solicite ao usuário a entrada de 5 nomes, e que exiba
#a lista desses nomes na tela. Após exibir essa lista, o programa deve
#mostrar também os nomes na ordem inversa em que o usuário os digitou, um por linha.


nomes=[" "]*5
for x in range(5):
    nomes[x]=input(f"Digite o {x +1 }ª nome: ")
print(nomes)
print(f" Na ordem inversa:")
for a in range(4, -1, -1):
    print(nomes[a])