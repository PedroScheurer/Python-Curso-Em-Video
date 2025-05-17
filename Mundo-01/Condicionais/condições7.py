sal = float(input("Diga seu salário: "))

if sal <= 1250:
    novoSal = sal + sal * 15/100
else:
    novoSal = sal + sal * 10/100

print("Seu novo salário será de {}".format(novoSal))