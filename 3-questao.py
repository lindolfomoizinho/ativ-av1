print("Informe os horários no formato 24h.")
hora_inicio = int(input("Hora de partida: "))
minuto_inicio = int(input("Minuto de partida: "))
hora_chegada = int(input("Hora de chegada: "))
minuto_chegada = int(input("Minuto de chegada: "))
    
segundos_parados = int(input("Segundos parados para descanso: "))
litros_gastos = float(input("Litros de combustível gastos: "))
preco_combustivel = float(input("Preço do litro de combustível (em R$): "))
distancia = float(input("Distância percorrida (em Km): "))

inicio_em_segundos = hora_inicio * 3600 + minuto_inicio * 60
chegada_em_segundos = hora_chegada * 3600 + minuto_chegada * 60
    
   
if chegada_em_segundos < inicio_em_segundos:
    chegada_em_segundos += 24 * 3600
    
tempo_total_viagem = chegada_em_segundos - inicio_em_segundos
    
    
tempo_movimento = tempo_total_viagem - segundos_parados
    

velocidade_media_global = (distancia / (tempo_total_viagem / 3600)) if tempo_total_viagem > 0 else 0
velocidade_media_movimento = (distancia / (tempo_movimento / 3600)) if tempo_movimento > 0 else 0
    
    
custo_combustivel = litros_gastos * preco_combustivel
    
    
km_por_litro = distancia / litros_gastos if litros_gastos > 0 else 0
litros_por_hora = (litros_gastos / (tempo_movimento / 3600)) if tempo_movimento > 0 else 0
custo_por_km = custo_combustivel / distancia if distancia > 0 else 0
    
   
print("\n--- Dados do computador de bordo ---")
print(f"a) Tempo total de viagem: {tempo_total_viagem} segundos")
print(f"b) Velocidade média global: {velocidade_media_global:.2f} Km/h")
print(f"   Velocidade média em movimento: {velocidade_media_movimento:.2f} Km/h")
print(f"c) Custo da viagem com combustível: R$ {custo_combustivel:.2f}")
print(f"d) Desempenho do carro:")
print(f"   - Km por litro: {km_por_litro:.2f} Km/l")
print(f"   - Litros por hora: {litros_por_hora:.2f} l/h")
print(f"   - Custo por Km: R$ {custo_por_km:.2f}/Km")