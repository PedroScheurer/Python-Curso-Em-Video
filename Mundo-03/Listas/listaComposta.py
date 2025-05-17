teste = []
teste.append("Gustavo")
teste.append(40)
galera = []
galera.append(teste[:])
teste[0] = "Maria"
teste[1] = 22
galera.append(teste[:])
print(galera)

galera = [["Joao", 19], ["Ana", 33], ["Joaquim", 13], ["Maria", 45]]
print(galera[2][1])

for pessoa in galera:
    print(f"{pessoa[0]} tem {pessoa[1]} anos de idade")

pessoal = []
dado = []
for c in range(0, 3):
    dado.append(str(input("nome: ")))
    dado.append(int(input("idade: ")))
    pessoal.append(dado[:])
    dado.clear()
for p in pessoal:
    if p[1] >= 21:
        print(p)