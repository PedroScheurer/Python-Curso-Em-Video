produto = float(input("Digite o valor do produto: "))
print("Formas de pagamento:\n[1] À Vista no dinheiro ou cheque (10% de desconto)\n[2] À Vista no cartão (5% de desconto)\n[3] 2x no cartão\n[4] 3x no cartão ou mais (20% de juros)")
opcao = int(input("\nSelecione uma opção: "))

if opcao == 1:
    preco = produto - produto * 10/100
    print("Preco final R${}".format(preco))
elif opcao == 2:
    preco = produto - produto * 5/100
    print("Preço final R${}".format(preco))
elif opcao == 3:
    preco = produto
    parcela = preco / 2
    print("Preço final R${} em 2x de R${:.2f}".format(preco, parcela))
elif opcao == 4:
    preco = produto + produto * 20/100
    qntdParcelas = int(input("Digite a quantidade de parcelas: "))
    parcela = preco / qntdParcelas
    print("Preço final R${} em {}x de R${:.2f}".format(preco, qntdParcelas, parcela))
else:
    print("Opção inválida")