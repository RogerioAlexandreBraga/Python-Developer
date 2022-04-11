largura_parede = float(input("Digite a largura da parede: "))
altura_parede = float(input("Digite a altura da parede: "))
area = largura_parede * altura_parede
litro_tinta = 2
total_de_tinta = area / litro_tinta
print(
    "A dimensão é {:.2f} x {:.2f} m², e a área da parede é {:.2f} m² quadrados, e utilizará {:.2f} litros de tinta para pintá-la".format(
        largura_parede, altura_parede, area, total_de_tinta))
