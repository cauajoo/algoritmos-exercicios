# # num1 = int(input("Digite o primeiro número: "))
# # num2 = int(input("Digite o segundo número: "))
# # operacao = input("Digite a operação: ")

# # if operacao == "+" or operacao == "soma" or operacao == "adicao":
# #     resultado = num1 + num2
# #     print(f"O resultado da soma é: {resultado}")
# # elif operacao == "-" or operacao == "subtracao" or operacao == "subtrair":
# #     resultado = num1 - num2
# #     print(f"O resultado da subtração é: {resultado}")
# # elif operacao == "*" or operacao == "multiplicacao" or operacao == "multiplicar":
# #     resultado = num1 * num2
# #     print(f"O resultado da multiplicação é: {resultado}")
# # elif operacao == "/" or operacao == "divisao" or operacao == "dividir":
# #     resultado = num1 / num2
# #     print(f"O resultado da divisão é: {resultado}")
# # else:
# #     print("Operação inválida.")

# usrio = input("Digite o usuário: ")
# snha = input("Digite a senha: ")



# if usrio == "admin" and snha == "123456":
#     print("Usuario logado com sucesso!")
# else:
#     print("Senha ou usuário inválido. Tente novamente!")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    if num1 == 0 or num1 > 0:
        print(f"O número {num1} é positivo ou neutro.")
    else:
        print(f"O número {num1} é negativo.")
else:   
    if num2 == 0 or num2 > 0:
        print(f"O número {num2} é positivo ou neutro.")
    else:
        print(f"O número {num2} é negativo.")

