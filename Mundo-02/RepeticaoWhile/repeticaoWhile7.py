#Sequencia de Fibonacci
n = int(input("Digite quantos elementos da sequencia de Fibonacci deseja ver: "))
termo = 0
termo1 = 1
while n != 0:
    seq = termo + termo1
    print(termo, end=" ")
    termo = termo1
    termo1 = seq
    n -= 1
