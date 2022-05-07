
#TESTE, MODIFICANDO A ENTRADA DE ACORDO COM ESSA CONFIGURAÇÃO: <tipo_do_cliente>: <data1>, <data2>, <data3>


#RESPECTIVAMENTE: CLASSIFICAÇÃO,TAXA REGULAR, RAXA REWARD REWARD*2
lake=[3,110,80,90,80]
bridge=[4,160,110,60,50]
ridge=[5,220,100,150,40]


#RECEBE A ENTRADA

entrada="Rewards: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)"



#SEPARA TIPO_DO_CLIENTE DE DATAS EM ESPAÇOS NO VETOR
entrada_formatada=entrada.split()
entrada_formatada[0]=str(entrada_formatada)

#RECEBE STRING COM TIPO_DO_CLIENTE
tipo_do_cliente=entrada_formatada[0]

#CRIANDO LISTA DO TAMANHO DA ENTRADA, PARA CASO RECEBA MAIS DATAS
data=[""]*(len(entrada_formatada)-1)


#FORMATAÇÃO DE CADA BLOCO DE DATA PARA UM ESPAÇO NO VETOR DATA[], CONTANDO APARTIR DE 1 POIS O 0 É O VALOR DO TIPO_DO_CLIENTE
cont=0
for p in range(len(entrada_formatada)-1):
    nome_dia_bruto=entrada_formatada[cont+1]
    nome_dia_formatado=nome_dia_bruto[10:]
    nome_dia_formatado=nome_dia_formatado.replace(",","")
    nome_dia_formatado=nome_dia_formatado.replace(")","")
    data[cont]=nome_dia_formatado

    cont=cont+1
    

#VE QUAL DIA, DE ACORDO COM O QUE TA ENTRE PARENTESES (), EX. (MON), E SEPARA DO FIM DE SEMANA

valorTotalLake=0
valorTotalBridge=0
valorTotalRidge=0

for i in range(len(entrada_formatada)-1):
    if (data[i]=="mon" or data[i]=="tues" or data[i]=="wed" or data[i]=="thur" or data[i]=="fri"):
        if(tipo_do_cliente[2:9]=="Regular"):
            valorTotalLake=valorTotalLake+lake[1]
            valorTotalBridge=valorTotalBridge+bridge[1]
            valorTotalRidge=valorTotalRidge+ridge[1]

        if(tipo_do_cliente[2:9]=="Rewards"):
            valorTotalLake=valorTotalLake+lake[2]
            valorTotalBridge=valorTotalBridge+bridge[2]
            valorTotalRidge=valorTotalRidge+ridge[2]
    else:
        if(tipo_do_cliente[2:9]=="Regular"):
            valorTotalLake=valorTotalLake+lake[3]
            valorTotalBridge=valorTotalBridge+bridge[3]
            valorTotalRidge=valorTotalRidge+ridge[3]

        if(tipo_do_cliente[2:9]=="Rewards"):
            valorTotalLake=valorTotalLake+lake[4]
            valorTotalBridge=valorTotalBridge+bridge[4]
            valorTotalRidge=valorTotalRidge+ridge[4]

#SE TODOS VALORES FOREM DIFERENTES, PEGA O MENOR E DENOMINA O NOME A VARIAVEL NOME_HOTEL_MAIS_BARATO

if(valorTotalLake != valorTotalBridge and valorTotalLake != valorTotalRidge and valorTotalRidge != valorTotalBridge):
    if(valorTotalLake < valorTotalBridge and valorTotalLake < valorTotalRidge):
        menorValor=valorTotalLake
        nome_hotel_mais_barato="Lakewood"

    if(valorTotalRidge < valorTotalLake and valorTotalRidge < valorTotalBridge):
        menorValor=valorTotalRidge
        nome_hotel_mais_barato="Ridgewood"

    if(valorTotalBridge < valorTotalLake and valorTotalBridge < valorTotalRidge):
        menorValor=valorTotalBridge
        nome_hotel_mais_barato="Bridgewood"

        #SE FOREM IGUAIS, PEGA AS NOTAS E VE QUAL MAIOR  
else:

    if(valorTotalLake == valorTotalBridge):
        if(lake[0]>bridge[0]):
            menorValor=valorTotalLake
            nome_hotel_mais_barato="Lakewood"
        else:
            menorValor=valorTotalBridge
            nome_hotel_mais_barato="Bridgewood"

    if(valorTotalLake == valorTotalRidge):
        if(lake[0]>ridge[0]):
            menorValor=valorTotalLake
            nome_hotel_mais_barato="Lakewood"
        else:
            menorValor=valorTotalRidge
            nome_hotel_mais_barato="Ridgewood"

    if(valorTotalRidge == valorTotalBridge):
        if(ridge[0]>bridge[0]):
            menorValor=valorTotalRidge
            nome_hotel_mais_barato="Ridgewood"
        else:
            menorValor=valorTotalBridge
            nome_hotel_mais_barato="Bridgewood"

print("\n\n\n----------------------------------------------------------------------")
print(f"O Hotel mais Barato de acordo com as Datas, É: {nome_hotel_mais_barato}")
print("----------------------------------------------------------------------\n\n")