cedula100 = cedula50 = cedula20 = cedula10 = cedula5 = cedula2 = cedula1 = 0
valor = int(input("Digite um valor: R$ "))
while True:
	while valor >= 100:
		cedula100 += 1
		valor -= 100
	while valor >= 50:
		cedula50 += 1
		valor -= 50
	while valor >= 20:
		cedula20 += 1
		valor -= 20
	while valor >= 10:
		cedula10 += 1
		valor -= 10
	while valor >= 5:
		cedula5 += 1
		valor -= 5
	while valor >= 2:
		cedula2 += 1
		valor -= 2
	while valor >= 1:
		cedula1 += 1
		valor -= 1
	if valor == 0:
		break
print(f"Cédulas de R$100 = {cedula100}\nCédulas de R$50 = {cedula50}\nCédulas de R$20 = {cedula20}\nCédulas de R$10 = {cedula10}\nCédulas de R$5 = {cedula5}\nCédulas de R$2 = {cedula2}\nMoedas de R$1 = {cedula1}")