# Salário Líquido:

vlrHrs = float(input("Digite o valor da hora trabalhada: "))
hrsTbl = float(input("Digite o número de horas trabalhadas no mês: "))

salBruto = vlrHrs * hrsTbl
ir = salBruto * 0.11
inss = salBruto * 0.08
sind = salBruto * 0.05
salLiq = salBruto - ir - inss - sind

print(f"Salário Bruto: R$ {salBruto:.2f}")
print(f"IR (11%): R$ {ir:.2f}")
print(f"INSS (8%): R$ {inss:.2f}")
print(f"Sindicato (5%): R$ {sind:.2f}")
print(f"Salário Líquido: R$ {salLiq:.2f}")

