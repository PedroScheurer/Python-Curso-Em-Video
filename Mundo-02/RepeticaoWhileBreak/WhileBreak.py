soma = n = c = 0
while True:
    n = int(input("Digite um número [999 para parar]: "))
    if n == 999:
        break
    soma += n
    c += 1
print(f"A soma entre os {c} valores é {soma}")