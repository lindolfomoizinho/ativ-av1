valor = int(input("Digite um número: "))

if 0 <= valor <= 9999:
    unidade = valor % 10
    valor //= 10

    dezena = valor % 10
    valor //= 10

    centena = valor % 10
    valor //= 10

    milhar = valor

    print(f"A soma dos algarismos é: {unidade + dezena + centena + milhar}")
else:
    print("Digite um valor entre 0 e 9999")