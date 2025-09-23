# # Cálculo do IMC

# # peso = 70
# # altura = 1.75

# # imc = peso / (altura ** 2)
# # print(f'\nSeu IMC é: {imc:.2f}')

# # # Cálculo de desconto em um produto

# # v_prodt = 100
# # desc = 0.1

# # print(f'\nValor do produto: R${v_prodt}')
# # v_desc = (v_prodt * desc)
# # print(f'Valor do desconto: R${v_desc}')

# # v_final = v_prodt - v_desc
# # print(f'Valor final do produto: R${v_final}')

# # # Cálculo de média de notas:

# # nta1 = 7.0
# # nta2 = 8.0
# # nta3 = 6.0

# # med = (nta1 + nta2 + nta3) / 3

# # print(f'\nSua média é: {med}')

# # Interação com o usuário:

# # nome = input('\nDigite seu nome: ')
# # nasc = int(input('Digite seu ano de nascimento: '))
# # idd = 2025 - nasc

# # print('\nSeu nome é', nome+', e sua idade é', idd)

# # Cálculo de idade no futuro:

# # nome = input('\nDigite seu nome: ')
# # idd = int(input('Digite sua idade: '))
# # anos_fut = int(input('Digite quantos anos no futuro você quer saber sua idade: '))
# # idd_fut = idd + anos_fut

# # print(f'\nSeu nome é {nome}, e sua idade daqui a {anos_fut} anos será {idd_fut}')

# n1 = int(input("Digite um número: "))
# n2 = int(input("Digite outro número: "))

# sm = n1 + n2
# sb = n1 - n2
# mt = n1 * n2
# dv = n1 / n2

# print(f'\nA soma entre {n1} e {n2} é {sm}')
# print(f'A subtração entre {n1} e {n2} é {sb}')
# print(f'A multiplicação entre {n1} e {n2} é {mt}')
# print(f'A divisão entre {n1} e {n2} é {dv}')

nta1 = int(input("Digite a primeira nota: "))
nta2 = int(input("Digite a segunda nota: "))
nta3 = int(input("Digite a terceira nota: "))

med = (nta1 + nta2 + nta3) / 3

print(f'\nA média entre {nta1}, {nta2} e {nta3} é: {med}')

