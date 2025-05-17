#def soma(a, b):
#    print(f"A = {a}\nB = {b}")
#    s = a + b
#    print(f"A soma entre eles é {s}")


#soma(10,100.0212)

#def contador(*num):
#    tam = len(num)
#    print(f"Recebi os valores {num} e são ao todo {tam} números")


#contador(4, 12, 54, 5, 6, 3)
#valores = [5,4,7,2,4,6]
#def dobra(lst):
#    pos = 0
#    while pos < len(lst):
#        lst[pos] *= 2
#        pos +=1

#dobra(valores)

#def soma(* numeros):
#    s = 0
#    for i in numeros:
#        s += i
#    print(f"A soma dos números {numeros} é {s}")
#soma(3,4,1,2,3,4)


#parametros opcionais
#def soma(a=0,b=0,c=0):

#Escopo de variaveis

#def teste(b):
#   global a
#   a=8
#   b+=4


#a = 5
#print(a)
#    retorno = 5
#teste(a)
#print(a)
#     retorno = 8

#def somar(a=0, b=0, c=0):
#    s = a + b + c
#    print(f"A soma vale {s}")


#somar(3, 4, 2)
#somar(2, 3)


#def somar(a0,b=0,c=0)
#   s = a + b + c
#   return s


#r1 = somar(3,5,1)
#r2 = somar(10, 20)
#r3 = (4,4)

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial(7)

print(f"Obtive os resultados {f1,f2,f3}")