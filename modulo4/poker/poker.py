from limpiar import limpiar01


numeroCartas = 0
numeroCartasCont = 0
clasificacion=[]

for i in range(len(limpiar01.var01)):
    lalo=str(limpiar01.var01[i][1])
    for j in range(len(lalo)):
        numeroCartas = lalo.count(lalo[j])
        numeroCartasCont = numeroCartasCont + numeroCartas
        #print(numeroCartas)
        #print(numeroCartasCont)
        if(numeroCartas == 1  and clasificacion.count("DIFERENTE") < 5):
            clasificacion.append("DIFERENTE")
            numeroCartas = 0
        elif(numeroCartas == 2 and clasificacion.count("PAR") < 2 ):    
            clasificacion.append("PAR")
            numeroCartas = 0
        elif(numeroCartas == 3 and clasificacion.count("TERCIA") < 1 ): 
            clasificacion.append("TERCIA")
            numeroCartas = 0
        elif(numeroCartas == 4 and clasificacion.count("POKER") < 1 ): 
            clasificacion.append("POKER")
            numeroCartas = 0
        elif(numeroCartas == 5 and clasificacion.count("QUINTANILLA") < 1 ): 
            clasificacion.append("QUINTANILLA")
            numeroCartas = 0
        if(numeroCartasCont > 4 or j == len(lalo)):
        #if( j == len(lalo)-1):
            limpiar01.var01[i].append(clasificacion)
            numeroCartas = 0
            numeroCartasCont = 0
            clasificacion=[]
            break
        #print("######") 
        #print(clasificacion)
        #numeroCartas = 0
        #numeroCartasCont = 0
        #clasificacion=[]
        
    #clasificacion=[]
    #print(clasificacion[i])
    #break

for i in range(len(limpiar01.var01)):
    print('{}{}'.format(limpiar01.var01[i][0],limpiar01.var01[i][2]))
        