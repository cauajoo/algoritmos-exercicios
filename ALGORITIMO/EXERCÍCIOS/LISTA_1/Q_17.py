print("Tinta custa R$80.00 a lata de 18 litros e R$25.00 a lata de 3.6 litros, e rende 6m² por litro.")

areaQd = int(input("Digite a área em m² que deseja pintar: "))
ltrs = areaQd / 6

if ltrs < 18:
    ltas = ltrs / 3.6
    vlrLtas = ltas * 25
    if ltrs % 3.6 == 0:
        print(f"Você precisará de {int(ltas)} latas de tinta, por R${vlrLtas:.2f}. Utilizando {ltrs:.2f} litros de tinta.")
    else:
        ltas = int(ltas) + 1
        vlrLtas = ltas * 25
        print(f"Você precisará de {int(ltas)} latas de tinta, por R${vlrLtas:.2f}. Utilizando {ltrs:.2f} litros de tinta.")
else:
    ltas = ltrs / 18
    
    
    # if ltrs % 18 == 0:
    #     vlrLtas = ltas * 80
    #     print(f"Você precisará de {int(ltas)} latas de tinta, por R${vlrLtas:.2f}. Utilizando {ltrs:.2f} litros de tinta")
    # else:
    #     ltas = int(ltas)
    #     ltas1 = ltrs - (ltas * 18)
    #     ltas1 = (ltas1 * 6) / 3.6

    #     if ltas1 % 3.6 == 0:
    #         ltas = ltas + ltas1
    #         vlrLtas = (ltas * 80) + (ltas1 * 25)
    #         print(f"Você precisará de {int(ltas)} latas de tinta, por R${vlrLtas:.2f}. Utilizando {ltrs:.2f} litros de tinta")
    #     else:
    #         ltas1 = int(ltas1) + 1
    #         vlrLtas = (ltas * 80) + (ltas1 * 25)
    #         ltas = ltas + ltas1
    #         print(f"Você precisará de {int(ltas)} latas de tinta, por R${vlrLtas:.2f}. Utilizando {ltrs:.2f} litros de tinta")