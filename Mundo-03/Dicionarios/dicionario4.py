from datetime import date
cadastro = dict()
nome = str(input("Nome: "))
anoNasc = int(input("Ano de nascimento: "))
dataAtual = date.today()
idade = dataAtual.year - anoNasc
carteira = int(input("Carteira de trabalho (0 se não tiver): "))
#add a lista
cadastro["nome"] = nome
cadastro["anoNasc"] = anoNasc
cadastro["idade"] = idade
cadastro["carteira"] = carteira

if cadastro["carteira"] != 0:
    anoContratado = int(input("Ano de contratação: "))
    salario = float(input("Salario: "))
    cadastro["anoContratado"] = anoContratado
    cadastro["salario"] = salario
    anoAposentado = cadastro[("anoContratado")] + 35
    cadastro["idadeAposentado"] = anoAposentado - anoNasc
print(cadastro)
for k, v in cadastro.items():
    print(f"O(a) {k} é {v}")