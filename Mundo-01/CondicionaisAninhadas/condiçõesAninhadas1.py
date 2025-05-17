valCasa = float(input("Valor da casa: "))
sal = float(input("Salário: "))
anos = int(input("ANOS para pagamento: "))

prestMensal = valCasa / (anos * 12)
trintadoSal = sal * 30 / 100
if  prestMensal > trintadoSal:
    print("Negado, valor da prestação (R${}) maior que 30% do salário {}.".format(prestMensal, trintadoSal))
else:
    print("Aprovado, valor da prestação (R${}) menor que 30% do salário {}.".format(prestMensal, trintadoSal))