dia_inicial = int(input("Dia inicial: "))
mes_inicial = int(input("Mês inicial (1 a 12): "))
dia_final = int(input("Dia final: "))
mes_final = int(input("Mês final (1 a 12): "))

if mes_inicial < 1 or mes_inicial > 12 or mes_final < 1 or mes_final > 12:
    print("Os meses devem estar no intervalo de 1 a 12.")
else:
    if mes_inicial == 1 or mes_inicial == 3 or mes_inicial == 5 or mes_inicial == 7 or mes_inicial == 8 or mes_inicial == 10 or mes_inicial == 12:
        dias_mes_inicial = 31
    elif mes_inicial == 4 or mes_inicial == 6 or mes_inicial == 9 or mes_inicial == 11:
        dias_mes_inicial = 30
    elif mes_inicial == 2:
        dias_mes_inicial = 28
    else:
        dias_mes_inicial = 0

    if mes_final == 1 or mes_final == 3 or mes_final == 5 or mes_final == 7 or mes_final == 8 or mes_final == 10 or mes_final == 12:
        dias_mes_final = 31
    elif mes_final == 4 or mes_final == 6 or mes_final == 9 or mes_final == 11:
        dias_mes_final = 30
    elif mes_final == 2:
        dias_mes_final = 28
    else:
        dias_mes_final = 0

    if dia_inicial < 1 or dia_inicial > dias_mes_inicial or dia_final < 1 or dia_final > dias_mes_final:
        print("Dias inválidos para o mês informado.")
    elif mes_inicial > mes_final or (mes_inicial == mes_final and dia_inicial > dia_final):
        print("A data inicial deve ser menor ou igual à data final.")
    else:
        dias_decorridos = 0

        if mes_inicial == mes_final:
            dias_decorridos = dia_final - dia_inicial
        else:
            dias_decorridos += dias_mes_inicial - dia_inicial

            mes_corrente = mes_inicial + 1
            while mes_corrente < mes_final:
                if mes_corrente == 1 or mes_corrente == 3 or mes_corrente == 5 or mes_corrente == 7 or mes_corrente == 8 or mes_corrente == 10 or mes_corrente == 12:
                    dias_decorridos += 31
                elif mes_corrente == 4 or mes_corrente == 6 or mes_corrente == 9 or mes_corrente == 11:
                    dias_decorridos += 30
                elif mes_corrente == 2:
                    dias_decorridos += 28
                mes_corrente += 1

            dias_decorridos += dia_final

        print(f"Quantidade de dias decorridos entre as datas: {dias_decorridos} dia(s).")