nta1 = float(input("Digite sua primeira nota: "))
nta2 = float(input("Digite sua segunda nota: "))

med = (nta1 + nta2)/2

if med > 9 and med <= 10:
    print(f"Nota A, Média {med}")
elif med > 7.5 and med <= 9:
    print(f"Nota B, Média {med}")
elif med > 6 and med <= 7.5: 
    print(f"Nota C, Média {med}")
elif med > 4 and med <= 6: 
    print(f"Nota D, Média {med}")
elif med >= 0 and med <= 4: 
    print(f"Nota E, Média {med}")
else: 
    print(f"Digite as notas novamente!")