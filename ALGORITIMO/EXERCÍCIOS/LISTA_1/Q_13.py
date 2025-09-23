alt = float(input("Digite sua altura em metros: "))
gen = input("Digite seu gênero (H/M): ")

if gen == 'H' or gen == 'h':
    psoIdl = (72.7 * alt) - 58
else:
    psoIdl = (62.1 * alt) - 44.7

print(f"Seu peso ideal é: {psoIdl:.2f} kg")