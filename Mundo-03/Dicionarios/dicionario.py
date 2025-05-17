filme = {"Nome": "Star Wars",
        "Ano": 1977,
         "Diretor": "George Lucas"
}
filme["Gênero"]= "ação"
del filme["Ano"]
print(filme)
print(filme.values())
print(filme.keys())
print(filme.items())
for chave, valor in filme.items():
    print(f"O {chave} é {valor}")
filme["nome"] = "Star Wars IV"
for k, v in filme.items():
    print(f"O {k} é {v}")

#estado1 = {"uf" : "RJ",
#          "nome" : "Rio De Janeiro"
#        }
#estado2 = {"uf" : "RS",
#           "nome" : "Rio Grande Do Sul"
#        }
#brasil = []
#brasil.append(estado1)
#brasil.append(estado2)

#print(brasil[0]["uf"])

estado = dict()
brasil = list()
for i in range(0,3):
    estado["nome"] = str(input("Nome: "))
    estado["uf"] = str(input("UF: "))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f"O campo {k} tem valor {v}")