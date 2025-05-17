from modulos1.utilidadeCeV.dado import leiaInt

def menu(nome):
    while True:
        print(f"{"="*30}\n{"Menu Principal":^30}\n{"="*30}")
        print(f"1 - Ver pessoas cadastradas\n2 - Cadastrar nova pessoa\n3 - Sair do sistema")
        opcao = leiaInt("\nSua opção: ")
        if opcao == 1:
            pessoasCadastradas(nome)

        if opcao == 2:
            nomePessoa = str(input("Nome: "))
            idade = leiaInt("Idade: ")
            cadastrarPessoa(nome, nomePessoa, idade)

        if opcao == 3:
            print(f"Fechando Sistema...")
            break

    return nome


def pessoasCadastradas(nome):
    try:
        a = open(nome, "rt")
    except:
        print("Erro ao ler arquivo")
    else:
        print(f"{"="*30}\n{"Pessoas Cadastradas":^30}\n{"="*30}")
        for linha in a:
            dado = linha.split(";")
            dado[1] = dado[1].replace("\n","")
            print(f"{dado[0]}\t{dado[1]:>15} anos")
    finally:
        a.close()


def cadastrarPessoa(nome, nomePessoa = "<desconhecido>", idade=None):
    try:
        a = open(nome, "at")
    except:
        print("Houve um erro na abertura do arquivo")
    else:
        try:
            a.write(f"{nomePessoa};{idade}\n")
        except:
            print("Houve um erro na hora de escrever os dados")
        else:
            print(f"Novo registro de {nomePessoa} adicionado.")
            a.close()

def arquivoExiste(nome):
    try:
        a = open(nome, "rt")
        a.close()
    except FileNotFoundError:
        print("Arquivo não encontrado")
        return False
    else:
        print("Arquivo encontrado")
        return True


def criarArquivo(nome):
    try:
        a = open(nome, "wt+")
        a.close()
    except:
        print("Houve um erro na criação do arquivo")
    else:
        print(f"Arquivo {nome} criado")