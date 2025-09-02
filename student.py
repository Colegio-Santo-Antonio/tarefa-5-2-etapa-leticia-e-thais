def validar_cartao(cartao):

    cartao = [int(digito) for digito in cartao]


    impares = sum(cartao[-1::-2])


    pares = []
    for digito in cartao[-2::-2]:
        dobro = digito * 2
        if dobro >= 10:
            dobro = (dobro - 10) + 1
        pares.append(dobro)

    soma = impares + sum(pares)
    if soma % 10 == 0:
        return "Cartão válido"
    else:
        return "Cartão inválido"

cartao = input().strip()

print(validar_cartao(cartao))# Leia uma linha com o número do cartão
numero = input()
