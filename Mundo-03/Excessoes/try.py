def leiaInt(msg = 0):
    msg = input("Digite um número inteiro: ")
    while True:
        try:
            int(msg)
            break
        except (ValueError, TypeError):
            msg = input("Erro: por favor, digite um número inteiro válido: ")
    return msg


def leiaFloat(msg = 0):
    msg = input("Digite um número real: ")
    while True:
        try:
            float(msg)
            break
        except (ValueError, TypeError):
            msg = input("Erro: por favor, digite um número real válido: ")
    return msg

inteiro = leiaInt()
real = leiaFloat()
print(f"O valor inteiro digitado foi {inteiro} e o real foi {real}.")
