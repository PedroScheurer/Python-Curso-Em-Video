extenso = ("zero", "um", "dois", "três", "quatro", "cinco",
           "seis", "sete", "oito", "nove", "dez")
n = int(input("Digite um número entre 0 e 10: "))
while True:
    if n < 0 or n > 10:
        n = int(input("Inválido, tente novamente: "))
    else:
        print(extenso[n])
        break
