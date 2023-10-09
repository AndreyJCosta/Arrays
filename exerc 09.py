#Exercício 09
#Altere o sistema anterior e faça um sistema de login, pedindo a senha do usuário e
#mostrando seu nome e a mensagem, login efetuado com sucesso.


print("|||||---> LOGIN <---|||||")
print(" Faça seu cadastro de usuário!")
print()
nomes=[" "]
senhas=[" "]
for x in range(1):
    nomes[x] = input("Cadastre seu nome: ")
    senhas[x] = input("Cadastre sua senha: ")
print()
print("Agora efetue seu login: ")
senha = input("Digite a sua senha: ")
print()
while senha != senhas[x]:
    senha = input(" SENHA INVÁLIDA. Tente novamente: ")

else:
    print(f" Bem Vindo {nomes[x]}, login efetuado com sucesso! ")