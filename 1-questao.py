def soma_algarismos (numero):
    unidade = numero % 10
    numero //= 10
    
    dezena = numero % 10 
    numero //= 10
    
    centena = numero % 10
    numero //= 10

    milhar = numero

    print(f"A soma dos algarismos é: {unidade + dezena + centena + milhar}")

valor = int(input("Digite um número: "))

if valor >= 0 or valor <=9999:
    print(soma_algarismos(valor))
else:
    print("Digite um valor entre 0 e 9999")