from time import sleep
def maior(*valores):
    print(f"{"=" * 30}")
    if len(valores) != 0:
        print("Analisando os valores passados...")
        for i in valores:
            print(f"{i}", end=" ")
        print(f"Foram informados {len(valores)} ao todo.")
        print(f"O maior valor informado foi {max(valores)}")
    else:
        print("Analisando os valores passados...")
        print(f"Nenhum valor digitado")


maior(3,4,5,1,2,3,5,6,8,123)
sleep(1)
maior(4,7,0)
sleep(1)
maior(1,2)
maior()