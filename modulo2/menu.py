
from modulo2 import modulo2 as m2

import os
import sys

def menu():
    while True:
        print("""
                            Bienvenido:
            1.- Antecedentes
            2.- Descripci´on de los datos
            3.- Estimación puntual
            4.- Intervalo de Confianza para una población 

            S EXIT
        """)
    
        op=input("Opción: ")
        if(op=="1"):
            os.system("cls")
            m2.antecedentes()
            os.system("cls")
        elif(op=="2"):
            os.system("cls")
            m2.descripcionDatos()
            os.system("cls")
        elif(op=="3"):
            os.system("cls")
            m2.estimacionPuntual()
            os.system("cls")
        elif(op=="4"):
            os.system("cls")
            m2.confianza2()
            os.system("cls")
        elif(op=="S" or op=="s"):
            os.system("cls")
            print("Bye")
            print("")
            print("")
            sys.exit()
        else:
            print("No es opción!")