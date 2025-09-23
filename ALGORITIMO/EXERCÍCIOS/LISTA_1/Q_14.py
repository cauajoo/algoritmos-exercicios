print("Calculadora de excesso de peso para pescadores:")

pso = float(input("\nDigite o peso total dos peixes pescados (em kg): "))
exesso = pso - 50
multa = exesso * 4

if pso > 50:
    print(f"\nO peso total dos peixes pescados foi de {pso:.2f} kg")
    print(f"\nO peso excedeu em {exesso:.2f} kg")
    print(f"A multa a ser paga é de R$ {multa:.2f}")

else:
    print(f"\nO peso {pso} está dentro do limite permitido. Não há multa a ser paga.")
