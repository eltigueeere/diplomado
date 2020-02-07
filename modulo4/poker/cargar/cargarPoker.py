import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

datos='C:/Users/lalo/Downloads/poker/datos/lalo.xlsx'

df=pd.read_excel(datos, sheet_name='Hoja1') 

variables=df.values.tolist ()

