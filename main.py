
def retorna_menor_custo(entrada):

    lake=[3,110,80,90,80]
    bridge=[4,160,110,60,50]
    ridge=[5,220,100,150,40]

    entrada=entrada
    

    entrada_formatada=entrada.split()
    entrada_formatada[0]=str(entrada_formatada)
    tipo_do_cliente=entrada_formatada[0]
    data=[""]*(len(entrada_formatada)-1)


    cont=0
    for p in range(len(entrada_formatada)-1):
        nome_dia_bruto=entrada_formatada[cont+1]
        nome_dia_formatado=nome_dia_bruto[10:]
        nome_dia_formatado=nome_dia_formatado.replace(",","")
        nome_dia_formatado=nome_dia_formatado.replace(")","")
        data[cont]=nome_dia_formatado

        cont=cont+1
        


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

    return(nome_hotel_mais_barato)
    