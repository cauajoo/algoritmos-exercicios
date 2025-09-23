# Faça um Programa que peça a área em m² que uma pessoa deseja pintar.

print("Tinta custa R$80.00 a lata de 18 litros, e rende 3m² por litro.")

areaQd = int(input("Digite a área em m² que deseja pintar: "))
ltrs = areaQd / 3
ltas = ltrs / 18

if ltrs <= 18:
    print(f"Você precisará de 1 lata de tinta, por R$80.00. Utilizando {ltrs:.2f} litros de tinta.")
elif ltrs % 18 == 0:
    vlrLtas = ltas * 80
    print(f"Você precisará de {int(ltas)} latas de tinta, por R${vlrLtas:.2f}. Utilizando {ltrs:.2f} litros de tinta")
else:
    ltas = int(ltas) + 1
    vlrLtas = ltas * 80
    print(f"Você precisará de {int(ltas)} latas de tinta, por R${vlrLtas:.2f}. Utilizando {ltrs:.2f} litros de tinta") 