
from modulo2 import cuentitas as cu
from modulo2 import cuentitas2 as cu2

import os

def antecedentes():
    print("""
    +--------------------------------------------------------------------------------------------------------+
    |                                           Antecedentes.                                                |
    |                                                                                                        |
    |                                                                                                        |
    | Los datos que hemos podido recopilar hace referencia a números de cuenta de usuarios de una línea      |
    | telefónica y los consumos que pueden tener como lo son:                                                |
    |    Voz                                                                                                 |
    |    Datos                                                                                               |
    |    Mensajes                                                                                            |
    |                                                                                                        |
    | Buscaremos obtener la mayor información de relevancia posible con forme resolvemos los puntos          |
    | del proyecto para poder llegar a la conclusión si es que estos datos pueden llegar a tener algún       |
    | valor o si es que no los tiene o nos faltó recopilar más información.                                  |
    |                                                                                                        |
    |                                                                                                        | 
    +--------------------------------------------------------------------------------------------------------+
                                    
    """)
    os.system("pause")
    

def descripcionDatos():
    print("""
    +--------------------------------------------------------------------------------------------------------+
    |                                           Fuente Datos.                                                |
    |                                                                                                        |
    |                                                                                                        |
    | La fuente de los datos salió de las Bases de Datos de pruebas QA de una conocidas empresa te telefonía.|
    |                                                                                                        |
    |                                                                                                        | 
    +--------------------------------------------------------------------------------------------------------+
    """)

    print("""
    +--------------------------------------------------------------------------------------------------------+
    |                                          A) Análisis Datos                                             |
    |                                                                                                        |
    |                                                                                                        |
    | Realizar el análisis descriptivo (exploratorio) de las variables cualitativa y cuantitativa.           |
    |                                                                                                        |
    |                                                                                                        | 
    +--------------------------------------------------------------------------------------------------------+
    """)
    cu.descripcionDatosCuentitas()
    print("\n\n")
    os.system("pause")
    os.system("cls")

    print("""
    +--------------------------------------------------------------------------------------------------------+
    |                                         B) Análisis Variables.                                         |
    |                                                                                                        |
    |                                                                                                        |
    | Para registrar los resultados de las variables cuantitativas llene la siguiente  tabla:                |
    |                                                                                                        |
    |                                                                                                        | 
    +--------------------------------------------------------------------------------------------------------+
    """)
    cu.descripcionDatosCuentitas2()
    while True:
        print("""
        +--------------------------------------------------------------------------------------------------------+
        |                                           Graficas de variables.                                       |
        |                                                                                                        |
        |             1.-Variable Cualitativa                                                                    |
        |             2.-Variable cuantitativa 1                                                                 | 
        |             3.-Variable cuantitativa 2                                                                 | 
        |             4.-Concluciones Generales                                                                  |
        |             S Menu anterior                                                                            |
        |                                                                                                        |
        +--------------------------------------------------------------------------------------------------------+
        """)

        opGrafic=input("Opcion: ")

        if(opGrafic=="1"):
            cu.graficasP1Cualitativa()
        elif(opGrafic=="2"):
            cu.graficasP1Tiempo()
        elif(opGrafic=="3"):
            cu.GrafP1Edad()
        elif(opGrafic=="4"):
            print("""
            +--------------------------------------------------------------------------------------------------------+
            |                       C) Comente sobre los resultados del inciso anterior                              |
            |                                                                                                        |
            |                                                                                                        |
            |                                                                                                        |
            |                                                                                                        |
            |                                                                                                        |
            |                                                                                                        |
            |                                                                                                        |
            +--------------------------------------------------------------------------------------------------------+
            """)
        elif(opGrafic=="s" or opGrafic=="S"):
            break
        else:
            print("No es opción")



#########################################################################################################################
#############         #################################  #####  #########################################################
############  #####  #################################  #####  ##########################################################
###########  #####  #################################  #####  ###########################################################
##########  #####  #################################  #####  ############################################################
#########         #################################  #####  #############################################################
########  ########################################  #####  ##############################################################
#######  ########################################  #####  ###############################################################
######  ########################################  #####  ################################################################
#########################################################################################################################

def estimacionPuntual():
    cu.estimacionPuntualA()
    os.system("pause")
    os.system("cls")
            
    cu.estimacionPuantualB()
    print()
    print()
    os.system("pause")
    os.system("cls")


def confianza2():
    print("""
            +--------------------------------------------------------------------------------------------------------+
            |                                  2 INTERVALO DE CONFIANZA PARA UNA POBLACIÓN                           |
            +--------------------------------------------------------------------------------------------------------+
    """) 
    print()
    cu2.printConfianza()        
    os.system("pause")
