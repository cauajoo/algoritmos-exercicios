nta1 = float(input("Digite sua primeira nota: "))
nta2 = float(input("Digite sua segunda nota: "))

med = (nta1 + nta2)/2

if med == 10:
    print(f"Sua média é {med:.2f}. Aprovado com Dinstinção!")
elif med >= 7:
    print(f"Sua média é {med:.2f}. Aprovado!")
else: 
    print(f"Sua média é {med:.2f}. Reprovado!")