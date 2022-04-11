preco_produto_1 = float(input("Digite o valor do produto 1: R$: "))
percentual = float(input("Digite o percentual do desconto: "))
desconto = preco_produto_1*percentual/100
novo_preco = preco_produto_1 - desconto
print("O valor do produto com o desconto é: {:.2f}".format(novo_preco))
