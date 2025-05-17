def notas(*notas,sit=False):
    """
    -> Função para analisar notas e situações de vários alunos
    :param notas: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    soma=0
    for i in notas:
        total = len(notas)
        maior = max(notas)
        menor = min(notas)
        soma += i
    
    media = soma / total
    if media >= 7:
        situacao = "Boa"
    else:
        situacao = "Ruim"
    dict = {"Total":total,"Maior":maior,"Menor":menor,
            "Media":media}

    if sit:
        dict["Situação"] = situacao

    return dict

print(notas(8,5,6,10, 10, 4,7,sit=True))
help(notas)
print(notas(3,4,2,sit=True))