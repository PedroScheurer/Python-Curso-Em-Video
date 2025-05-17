from operator import index

tabela = ("Internacional", "São Paulo", "Flamengo", "Cuiába",
          "Criciúma", "Grêmio", "Atlético MG", "Avaí",
          "Fluminense", "Athletico PR", "Santos", "Corinthians",
          "Botafogo", "Vasco", "Fortaleza", "Juventude", "Ceará",
          "Palmeiras", "Bahia", "Cruzeiro")
print(tabela[:5])
print(tabela[-4:])
print(sorted(tabela))
for c in tabela:
    if c == "Cruzeiro":
        print(f"O {c} fica na posição {tabela.index(c) + 1}")
for pos, c in enumerate(tabela):
    if c == "Corinthians":
        print(f"O {c} fica na posição {pos}")
print(f"O Inter fica na posição {tabela.index("Internacional") + 1}")
