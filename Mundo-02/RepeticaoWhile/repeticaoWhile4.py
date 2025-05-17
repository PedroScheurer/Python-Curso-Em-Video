num = int(input("Digite o número que deseja fatorar: "))
numF = num
auxW = num
auxF = num
#Formato em While
while num != 1:
   num -= 1
   auxW = auxW * num
print(auxW)
#Formato em For
for auxF in range (numF, 1,-1):
    numF = (auxF - 1) * numF
print(numF)