real = float(input("Quanto dinheiro você tem na carteira? R$: "))
cotacao_dolar = 3.27
dolar = real / cotacao_dolar
#print(f"Com {real:.2f} rais, posso comprar {dolar:.2f} dolares")
print("Com {:.2f} reais, posso comprar {:.2f} dolares".format(real, dolar))