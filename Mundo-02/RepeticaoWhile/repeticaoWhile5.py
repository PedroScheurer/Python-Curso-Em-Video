razao = int(input("Digite a razao da PA: "))
termo = int(input("Digite o primeiro termo da PA: "))
termo10 = termo + (10 - 1) * razao
teste = 10
while teste + 1 != 1:
    teste -= 1
    print(termo)
    termo = razao + termo

