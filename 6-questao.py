from datetime import datetime
from dateutil.relativedelta import relativedelta

sexo = input("Digite o sexo da pessoa (masculino/feminino): ").strip().lower()

data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")

data_contribuicao = input("Digite a data de início da contribuição (DD/MM/AAAA): ")
inicio_contribuicao = datetime.strptime(data_contribuicao, "%d/%m/%Y")


hoje = datetime.now()

idade_atual = relativedelta(hoje, nascimento).years

tempo_contribuicao = relativedelta(hoje, inicio_contribuicao).years

data_aposentadoria_idade = None
data_aposentadoria_tempo = None

if sexo == "masculino":
    data_aposentadoria_idade = nascimento + relativedelta(years=65)
elif sexo == "feminino":
    data_aposentadoria_idade = nascimento + relativedelta(years=62)

if sexo == "masculino":
    data_aposentadoria_tempo = inicio_contribuicao + relativedelta(years=35)
elif sexo == "feminino":
    data_aposentadoria_tempo = inicio_contribuicao + relativedelta(years=30)

if data_aposentadoria_idade and tempo_contribuicao >= 15:
    if data_aposentadoria_idade > data_aposentadoria_tempo:
        data_final = data_aposentadoria_tempo
    else:
        data_final = data_aposentadoria_idade
else:
    data_final = data_aposentadoria_tempo

if data_final > hoje:
    print("A data de aposentadoria será:", data_final.strftime("%d/%m/%Y"))
else:
    print("A pessoa já pode se aposentar!")
