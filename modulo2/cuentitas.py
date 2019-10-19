
#%%
import random
import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, date, timedelta
from mpl_toolkits.mplot3d import Axes3D   
from pandas import ExcelWriter
from pandas import ExcelFile
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
#%%
datos='C:/Users/lalo/Desktop/lalo/Nueva carpeta/diplomado/datos - copia.xlsx'
df=pd.read_excel(datos, sheet_name='KL') 

#listCuentaI=[]
labelTipoConsumo=["GPRS","OROAM","TGG","GPRSO","MOBILE","MMS","GPRSCM"]
tbVarTipEsc=["Variable","Tipo Variable","Esc medición"]
variables=df.columns.tolist()
tbVariables=[
    [variables[1], "CUALITATIVA", "NOMINAL"],
    [variables[2],"CUANTITATIVA-CONTINUA","RAZON"],
    [variables[3],"CUANTITATIVA-DISCRETA","RAZON"]
]
labelEstadistico1=["Estadístico","Consumo Sg", "Edad años"]
labelEstadistico=["Mínimo", "q1","q2","Media","q3","Máximo","Desv. estandár"]
tbP2B=[]

#%%
def descripcionDatosCuentitas():
    print('{:^10}{:>18}{:>19}{:>14}'.format(tbVarTipEsc[0],tbVariables[0][0],tbVariables[1][0],tbVariables[2][0]))
    print('{}'.format("----------------------------------------------------------------------------"))
    print('{:^10}{:>14}{:>25}{:>25}'.format(tbVarTipEsc[1],tbVariables[0][1],tbVariables[1][1],tbVariables[2][1]))
    print('{}'.format("----------------------------------------------------------------------------"))
    print('{:^10}{:>11}{:>13}{:>25}'.format(tbVarTipEsc[2],tbVariables[0][2],tbVariables[1][2],tbVariables[2][2]))



#%%
def descripcionDatosCuentitas2():
    cuantiles=[
        df["duracionConsumo"].quantile([0.25,0.5,0.75]).tolist(),
        df["edad"].quantile([0.25,0.5,0.75]).tolist()
    ]
    tbP2B = [
        [str(df["duracionConsumo"].min()),str(cuantiles[0][0]),str(cuantiles[0][1]),str(df["duracionConsumo"].mean()),str(cuantiles[0][2]),str(df["duracionConsumo"].max()),str(df["duracionConsumo"].std())],
        [ str(df["edad"].min()),str(cuantiles[1][0]),str(cuantiles[1][1]),str(df["edad"].mean()),str(cuantiles[1][2]),str(df["edad"].max()),str(df["edad"].std())]
    ]
    print("------------------------------------------------------------------------------")
    print('{:30}{:30}{:30}'.format(labelEstadistico1[0],labelEstadistico1[1],labelEstadistico1[2]))
    print("------------------------------------------------------------------------------")
    for i in range(len(labelEstadistico)):
        print('{:30}{:30}{:30}'.format(labelEstadistico[i],tbP2B[0][i],tbP2B[1][i]))
        print("------------------------------------------------------------------------------")

    
#%%
def graficasP1Cualitativa():
    colTipoConsumo=df["tipoConsumo"].tolist()
    colTipoConsumo1=[]
    colTipoConsumo1.append(colTipoConsumo.count('GPRS'))
    colTipoConsumo1.append(colTipoConsumo.count('OROAM'))
    colTipoConsumo1.append(colTipoConsumo.count('TGG'))
    colTipoConsumo1.append(colTipoConsumo.count('GPRSO'))
    colTipoConsumo1.append(colTipoConsumo.count('MOBILE'))
    colTipoConsumo1.append(colTipoConsumo.count('MMS'))
    colTipoConsumo1.append(colTipoConsumo.count('GPRSCM'))
    gfBarr=plt.figure()
    plt.axes((0.1, 0.3, 0.8, 0.6))
    plt.bar(range(len(colTipoConsumo1)),colTipoConsumo1)
    plt.ylim(0,133)
    plt.title("Tipos de Consumos /n")
    plt.xticks(np.arange(len(labelTipoConsumo)), labelTipoConsumo, rotation = 45)
    plt.show()


#%%
def graficasP1Tiempo():
    y = df["duracionConsumo"].tolist()
    plt.title('Tiempo llamadas')
    plt.hist(y, bins=6, alpha=1, edgecolor = 'black',  linewidth=1)
    plt.grid(True)
    plt.xlabel('Tiempo en sg')
    plt.ylabel('Persoanas')
    plt.show()
    plt.clf()


#%%
def GrafP1Edad():
    y = df["edad"].tolist()
    plt.title('Edades de usuarios')
    plt.hist(y, bins=6, alpha=1, edgecolor = 'black',  linewidth=1)
    plt.grid(True)
    plt.xlabel('Edades')
    plt.ylabel('Personas')
    plt.show()
    plt.clf()


###############################################################################
######################CUENTITAS PAGINA 2#######################################
###############################################################################

#%%
def estimacionPuntualA():
    tipoConsumo=df["tipoConsumo"].tolist()
    diccionario = {'LLAMADAS' : [] ,
    'MENSAJES' : [] ,
    'DATOS' : [] 
    }
    diccionario["LLAMADAS"].append(tipoConsumo.count("OROAM"))
    diccionario["LLAMADAS"].append(tipoConsumo.count("MOBILE"))
    diccionario["MENSAJES"].append(tipoConsumo.count("TGG"))
    diccionario["MENSAJES"].append(tipoConsumo.count("MMS"))
    diccionario["DATOS"].append(tipoConsumo.count("GPRSCM"))
    diccionario["DATOS"].append(tipoConsumo.count("GPRS"))
    diccionario["DATOS"].append(tipoConsumo.count("GPRSO"))
    print("De la variable cualitativa la dividimos para hacer la Estimación puntual las variables son: ")
    for i in range(len(labelTipoConsumo)):
        print(labelTipoConsumo[i] + " ", end="")
        print("")
    print("\t--------------------------------------------------")
    print('{}{:^15}{:^15}{:^15}'.format("\t","TIPO DE CONSUMO","TOTAL NACIONAL", "TOTAL INTERNACIONAL"))
    print("\t--------------------------------------------------")
    print('{}{:^15}{:^15}{:^15}'.format("\t","LLAMADAS",diccionario["LLAMADAS"][0],diccionario["LLAMADAS"][1]))
    print("\t--------------------------------------------------")
    print('{}{:^15}{:^15}{:^15}'.format("\t","MENSAJES",diccionario["MENSAJES"][0],diccionario["MENSAJES"][1]))
    print("\t--------------------------------------------------")
    print('{}{:^15}{:^15}{:^15}{}{}'.format("\t","DATOS",diccionario["DATOS"][0],diccionario["DATOS"][1]," MAS ",diccionario["DATOS"][2]))
    print("\t--------------------------------------------------")
    print("""
    Puse mas 8 xq GPRSCM y GPRSCO son datos internacionales es lo mismo \nPero tienen etiquetas diferentes  por que uno va a un servidor y el otro va a otro servidor pero es lo mismo 
    """)


#%%
def estimacionPuantualB():
    estPunB=[]
    estPunB=[
        ["CONSUMO EN SG",df["duracionConsumo"].mean(),df["duracionConsumo"].var()],
        ["EDAD",df["edad"].mean(),df["edad"].var()]
    ]

    print("""
        +--------------------------------------------------------+
        |                                                        |
        |        Estime para las dos variables cuantitativas     |
        |                                                        |
        +--------------------------------------------------------+
    """)
    print('{:^10}{:^25}{:^31}'.format("VARIABLE","MEDIA MUESTRAL","VARIANZA MUESTRAL"))
    print("-------------------------------------------------------------------------------------------")
    print('{:^10}{:^20}{:^32}'.format(estPunB[0][0],estPunB[0][1],estPunB[0][2]))
    print("--------------------------------------------------------------------------------------")
    print('{:^4}{:^37}{:^1}'.format(estPunB[1][0],estPunB[1][1],estPunB[1][2]))
    print("----------------------------------------------------------------------------------------")
    
    print("""
        +--------------------------------------------------------+
        |                                                        |
        |        Ccoeficiente de correlación muestral           |
        |                                                        |
        +--------------------------------------------------------+
    """)

    print(df.corr(method="pearson"))
    print("""
        Se mostrara la grafica lineal a continuación
    """)
    os.system("pause")    
    os.system("cls")
    plt.plot(df["duracionConsumo"], df["edad"], "ro")
    plt.ylabel("EDAD")
    plt.xlabel("DURACIÓN CONSUMO")
    plt.show()
