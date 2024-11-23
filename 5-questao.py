minutos = int(input("Digite o número de minutos que o veículo permaneceu no estacionamento: "))

horas = (minutos + 59) // 60

valor = 0

if horas <= 2:
    valor = horas * 8
elif horas <= 4:
    valor = 2 * 8 + (horas - 2) * 5
elif horas <= 12:
    valor = 2 * 8 + 2 * 5 + (horas - 4) * 3
else:
    valor = 30

print(f"Valor a ser pago: R$ {valor:.2f}")
