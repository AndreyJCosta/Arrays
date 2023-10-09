#Exercício 06
#Faça um código para ler 5 números e armazenar em um vetor. Após a leitura
#total dos 5 números, o código deve escrever esses 5 números lidos na ordem inversa.


num=[" "] * 5
for x in range(5):
    num[x]=int(input(f"Digite seu {x + 1 }º Número: "))
print()
print("A ordem é:")
for a in range(4, -1,-1):
    print( num[a], end=" ")