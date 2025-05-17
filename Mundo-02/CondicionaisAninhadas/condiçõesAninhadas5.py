nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2
print("Sua média é: {}".format(media))
if media < 5:
    print("Reprovado(a)")
elif 5 <= media < 7:
    print("Recuperação")
elif media >= 7:
    print("Aprovado(a)")