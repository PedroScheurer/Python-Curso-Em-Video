aluno = {"Nome" : str(input("Nome do aluno: ")),
         "Média": float(input("Média do aluno: "))}
if aluno["Média"] >= 7:
    aluno["Situação"] = "Aprovado"
else:
    aluno["Situção"] = "Reprovado"
for k, v in aluno.items():
    print(f"{k} é igual a {v}")