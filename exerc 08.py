#Exercício 08
#Faça um código para ler 5 nomes de usuários e suas respectivas senhas, e
#armazenar cada lista em um array diferente, após completar a digitação,
#imprimir , nome, senha e posição dos dados no array.


nomes=[" "]*5
senhas=[" "]*5
for x in range(0, 5):
    nomes[x] = input(f"Digite o nome do {x+1}º usuario: ")
    senhas[x] = input(f"Digite sua senha: ")
    print()
print("\o/"*20)
print()
for a in range(0,5):
    print(f"Nome: {nomes[a]}\nSenha: {senhas[a]}\nSeu índice: {a}")
    print()