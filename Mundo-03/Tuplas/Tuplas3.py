from random import randint
maior = menor = 0
tupla = (randint(1,100), randint(1,100),randint(1,100),
         randint(1,100),randint(1,100),)
print(tupla)
for c in tupla:
    if tupla.index(c) == 0:
        maior = c
        menor = c
    if maior < c:
        maior = c
    if menor > c:
        menor = c
print(f"O maior número é {maior} e o menor é {menor}")