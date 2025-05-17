razao = int(input("Digite a razao da PA: "))
termo = int(input("Digite o primeiro termo da PA: "))
termo10 = termo + (10 - 1) * razao
indice = 10
while indice + 1 != 1:
    indice -= 1
    print(termo)
    termo = razao + termo
indice = int(input("Mais quantos termos deseja buscar? "))
while indice + 1 != 1:
    indice -= 1
    print(termo)
    termo = razao + termo
print("Finalizado")