n  = int(input("Digite um número inteiro: "))
contN = 0
soma = 0
while n != 999:
    contN += 1
    soma += n
    n = int(input("Digite um número inteiro: "))
print("Foram digitados {} números e a soma entre eles é {}".format(contN, soma))