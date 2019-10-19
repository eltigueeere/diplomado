
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
from scipy.stats import sem, t
from scipy import mean
#%%
datos='C:/Users/lalo/Desktop/lalo/Nueva carpeta/diplomado/datos - copia.xlsx'
df=pd.read_excel(datos, sheet_name='KL') 

##%
def intervaloDeConfianza1(confianza, data):
    confianzaMedia=""
    n = len(data)
    m = mean(data)
    std_err = sem(data)
    h = std_err * t.ppf((1 + confianza) / 2, n - 1)
    inicioConfMed = m - h
    finConfMed = m+h
    confianzaMedia=str(inicioConfMed) + " a " + str(finConfMed) 
    return confianzaMedia

##%
def intervaloDeConfianza2(confianza, data):
    confianzaMedia=""
    n = len(data)
    m = np.var(data)
    std_err = sem(data)
    h = std_err * t.ppf((1 + confianza) / 2, n - 1)
    inicioConfMed = m - h
    finConfMed = m+h
    confianzaMedia=str(inicioConfMed) + " a " + str(finConfMed) 
    return confianzaMedia

def printConfianza():
    confianza1=0.90
    confianza2=0.95
    data1=df["duracionConsumo"]
    data2=df["edad"]
    confianzaMediaT=[]
    confianzaVarT=[]
    confianzaMediaT.append(intervaloDeConfianza1(confianza1, data1))
    confianzaMediaT.append(intervaloDeConfianza1(confianza1, data2))

    confianzaVarT.append(intervaloDeConfianza2(confianza2, data1))
    confianzaVarT.append(intervaloDeConfianza2(confianza2, data2))
    print('{:^20}{:^40}{:^55}'.format("NOMBRE VARIABLE","INTERVALO DE CONFIANZA DEL 90% PARA LA MEDIA","INTERVALO DE CONFIANZA DEL 90% PARA LA VARIAAANZA"))
    print('{:^10}{:^50}{:^55}'.format("TIEMPO CONSUMO",confianzaMediaT[0],confianzaVarT[0]))
    print('{:^10}{:^50}{:^55}'.format("EDAD   USUARIO",confianzaMediaT[1],confianzaVarT[1]))

#%%
def confianza3incisoA():
    print("""
             DIVIDIENDO LA VARIABLE CUALITATIVA EN DOS GRUPOS NOS QUEDA 
                GRUPO 1:
                    USO DE LA LINEA CELULAR DENTRO DEL PAÍS "NACIONAL"
                CON LAS CATEGORIAS :
                    MOBILE, MMS Y GPRS

                
                GRUPO 2:
                    USO DE LA LINEA CELULAR FUERA DEL PAÍS "INTERNACIONAL"                           
                CON LAS CATEGORIAS :
                    OROAM,TGG,GPRSO Y GPRSCM
    """)

def confianza3incisoB():