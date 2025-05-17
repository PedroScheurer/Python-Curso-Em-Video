lanche = ("Hambuerguer", "Suco", "Pizza", "Pudim", "Batata frita")
#TRÊS TÉCNICAS PARA ACESSAR ELEMENTO:
#for cont in range(0, len(lanche)):
#    print(lanche[cont])
#Possível definir inicio, final e de quantos em quantos

#Pega todos elementos e não precisa da posição
#for comida in lanche:
#    print(f"Eu vou comer {comida}")
#print("Comi muito, slk")

#Parecido com a primeira, PRECISA DE DUAS VARIAVEIS
#for pos, comida in enumerate(lanche):
#    print(f"Eu vou comer {comida} que fica na posição {pos}")

print(sorted(lanche))