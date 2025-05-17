palavras = ("inter", "futebol", "viajar", "namorada", "familia")
vogais = "AEIOUaeiou"
for palavra in palavras:
    print(f"\nA palavra {palavra} tem as vogais:", end=" ")
    for i in range(0, len(palavra)):
        if palavra[i] in vogais:
            print(f"{palavra[i]}", end= " ")