dist = float(input("Digite a distancia da viagem em KMs: "))
if dist <= 200:
    valPassagem = dist * 0.5
else:
    valPassagem = dist * 0.45

print("O valor da passagem fica R${:.0f},00 com uma distancia de {:.0f}KMs".format(valPassagem, dist))