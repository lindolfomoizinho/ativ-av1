# Fiz usando apenas if e else mas tem uma resolução com dicionarios e laços de repetição no final :/

def calcular_saque(valor):
    cedulas_100 = cedulas_50 = cedulas_20 = cedulas_10 = cedulas_5 = cedulas_2 = 0
    moedas_1 = moedas_050 = moedas_025 = moedas_010 = moedas_005 = moedas_001 = 0

    # Cálculo das cédulas
    if valor >= 100:
        cedulas_100 = int(valor // 100)
        valor -= cedulas_100 * 100
    
    if valor >= 50:
        cedulas_50 = int(valor // 50)
        valor -= cedulas_50 * 50

    if valor >= 20:
        cedulas_20 = int(valor // 20)
        valor -= cedulas_20 * 20

    if valor >= 10:
        cedulas_10 = int(valor // 10)
        valor -= cedulas_10 * 10

    if valor >= 5:
        cedulas_5 = int(valor // 5)
        valor -= cedulas_5 * 5

    if valor >= 2:
        cedulas_2 = int(valor // 2)
        valor -= cedulas_2 * 2

    # Cálculo das moedas
    if valor >= 1:
        moedas_1 = int(valor // 1)
        valor -= moedas_1 * 1

    if valor >= 0.50:
        moedas_050 = int(valor // 0.50)
        valor -= moedas_050 * 0.50

    if valor >= 0.25:
        moedas_025 = int(valor // 0.25)
        valor -= moedas_025 * 0.25

    if valor >= 0.10:
        moedas_010 = int(valor // 0.10)
        valor -= moedas_010 * 0.10

    if valor >= 0.05:
        moedas_005 = int(valor // 0.05)
        valor -= moedas_005 * 0.05

    if valor >= 0.01:
        moedas_001 = int(valor // 0.01)
        valor -= moedas_001 * 0.01

    return cedulas_100, cedulas_50, cedulas_20, cedulas_10, cedulas_5, cedulas_2, moedas_1, moedas_050, moedas_025, moedas_010, moedas_005, moedas_001

valor_saque = float(input("Digite o valor do saque: "))

cedulas_100, cedulas_50, cedulas_20, cedulas_10, cedulas_5, cedulas_2, moedas_1, moedas_050, moedas_025, moedas_010, moedas_005, moedas_001 = calcular_saque(valor_saque)

print("\nCédulas necessárias:")
if cedulas_100 > 0:
    print(f"R$100.00: {cedulas_100} cédulas")
if cedulas_50 > 0:
    print(f"R$50.00: {cedulas_50} cédulas")
if cedulas_20 > 0:
    print(f"R$20.00: {cedulas_20} cédulas")
if cedulas_10 > 0:
    print(f"R$10.00: {cedulas_10} cédulas")
if cedulas_5 > 0:
    print(f"R$5.00: {cedulas_5} cédulas")
if cedulas_2 > 0:
    print(f"R$2.00: {cedulas_2} cédulas")

print("\nMoedas necessárias:")
if moedas_1 > 0:
    print(f"R$1.00: {moedas_1} moeda")
if moedas_050 > 0:
    print(f"R$0.50: {moedas_050} moedas")
if moedas_025 > 0:
    print(f"R$0.25: {moedas_025} moedas")
if moedas_010 > 0:
    print(f"R$0.10: {moedas_010} moedas")
if moedas_005 > 0:
    print(f"R$0.05: {moedas_005} moedas")
if moedas_001 > 0:
    print(f"R$0.01: {moedas_001} moedas")
'''
def calcular_saque(valor):
    cedulas = [100, 50, 20, 10, 5, 2]
    moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

    resultado_cedulas = {}
    
    for cedula in cedulas:
        quantidade = int(valor // cedula)  
        
        if quantidade > 0:
            resultado_cedulas[cedula] = quantidade
            valor -= quantidade * cedula
    
    resultado_moedas = {}
    for moeda in moedas:
        quantidade = int(round(valor // moeda))  
        if quantidade > 0:
            resultado_moedas[moeda] = quantidade
            valor -= quantidade * moeda  

    return resultado_cedulas, resultado_moedas

valor_saque = float(input("Digite o valor do saque: "))

cedulas, moedas = calcular_saque(valor_saque)

print("\nCédulas necessárias:")
for cedula, quantidade in cedulas.items():
    print(f"R${cedula:.2f}: {quantidade} cédulas")

print("\nMoedas necessárias:")
for moeda, quantidade in moedas.items():
    print(f"R${moeda:.2f}: {quantidade} moedas")
'''

