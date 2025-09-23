num = int(input("Digite um número menor que 1000:"))

if num > 1000:
    cnta1 = num // 100
    num -= cnta1 * 100
    if num > 1:
        if num >= 10:
            cnta2 = num // 10
            num -= cnta2 * 10



