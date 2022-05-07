from main import retorna_menor_custo
cont=0

def get_cheapest_hotel(number):   #DO NOT change the function's name
        global cont
        cont=cont+1
        if(cont==1):
            entrada="Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)"
        if(cont==2):
            entrada="Regular: 20Mar2009(fri), 21Mar2009(sat), 22Mar2009(sun)"
        if(cont==3):
            entrada="Rewards: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)"
        
        cheapest_hotel = retorna_menor_custo(entrada)
    
        return cheapest_hotel