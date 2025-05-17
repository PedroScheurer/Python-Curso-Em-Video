def fatorial(n, show=False):
    """
        -> Calcula o Fatorial de um número
        :parametro n: O número a ser calculado.
        :parametro show: (opcional) Mostrar ou não a conta.
        :return: O valor do Fatorial de um número
    """
    aux = n
    if show == True:
        for i in range(1, n + 1):
            n *= i
            print(f"{i}", end=" ")
            if i < aux:
                print(f"x", end=" ")
        print("= ", end="")
        return n
    elif show == False:
        for i in range(1, n + 1):
            n *= i
        return n


print(fatorial(5, True))
help(fatorial)