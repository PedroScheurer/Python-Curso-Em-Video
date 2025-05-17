#MEU MODO
'''frase = str(input("Digite uma frase: ")).strip().replace(" ", "")
fraseAoContrario = frase[-1::-1]
if fraseAoContrario == frase:
    is_polindromo = True
    print(is_polindromo)
else:
    is_polindromo = False
    print(is_polindromo)'''

#MODO DO GUANABARA
frase = str(input("Digite uma frase: ")).upper().strip()
palavras = frase.split()
junto = "".join(palavras)
inverso = ""
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    is_palindromo = True
else:
    is_palindromo = False
print(inverso)
print(is_palindromo)