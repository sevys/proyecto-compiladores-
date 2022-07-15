import cv2
import pandas as pd
from tkinter import *
import re
from pila import Pila
import numpy as np
import threading
from prueba import dibujar_salida




matrizPredictiva = pd.DataFrame([[1,0,0,0,0,0,0,0,0,0,0],
                                [2,0,0,0,0,0,0,0,0,0,0],
                                [0,3,0,0,0,0,0,0,0,0,0],
                                [0,0,4,0,0,0,0,0,0,0,0],
                                [0,0,0,5,0,0,0,0,0,0,0],
                                [0,0,0,0,6,0,0,0,0,0,0],
                                [0,0,0,7,0,0,0,0,0,0,0],
                                [0,0,0,0,8,0,0,0,0,0,0],
                                [0,0,0,0,9,0,0,0,0,0,0],
                                [0,0,0,0,10,0,0,0,0,0,0],
                                [0,0,0,0,11,0,0,0,0,0,0],
                                [0,0,0,0,12,0,0,0,0,0,0],
                                [0,0,0,0,13,0,0,0,0,0,0],
                                [0,0,0,0,0,14,0,0,0,0,0],
                                [0,0,0,0,0,0,15,0,0,0,0],
                                [0,0,0,0,16,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,17,0,0,0],
                                [0,0,0,0,0,0,0,0,18,0,0],
                                [0,0,0,0,0,0,0,0,0,19,0],
                                [0,0,0,0,0,0,0,0,0,0,20]],
                                index= ['DF','SA','DFI','P','SEC','RESTOSEC','INI','ENTRY','VARIABLE','RV','PROCESO','RESTOPROCESO','X','NUMERO','OPERADOR','IMPRESION','FINAL','DFF','SC','IGUAL'],
                                columns= ['<','Diagrama',':','inicio','a..z | A..Z','0..9','+|-|/|*','final','DiagramaFlujo','>','=']
                                )

pila =['DF','SA','DFI','P','SEC','DFF','SC']



def expresion(tipo):

    delimitadores = re.compile("(^([<]|[>]|[:]|[=]))")
    palabrasReservadas = re.compile("(^(DiagramaFlujo|inicio|proceso|impresion|final))")
    numeros = re.compile("(^([0-9]+))")
    operadores = re.compile("(^([-]|[+]|[*]|[/]))")
    letras = re.compile("(^([A-Z-a-z]+))")

    delimitador = []
    reservadas = []
    numero = []
    operador = []
    palabras = []
    errores = []

    for element in tipo:
        listBox.delete(0, 5)
        resultadoDelimitador = re.fullmatch(delimitadores, element)
        resultadoPalabraReservada = re.fullmatch(palabrasReservadas, element)
        resultadoNumero = re.fullmatch(numeros, element)
        resultadoOperador = re.fullmatch(operadores, element)
        resultadoLetra = re.fullmatch(letras, element)

        if(resultadoDelimitador != None):
            print('si es verdad')
            delimitador.append(element)

        elif(resultadoPalabraReservada != None):
            print('si es verdad')
            reservadas.append(element)

        elif(resultadoNumero != None):
            print('si es verdad')
            numero.append(element)

        elif(resultadoOperador != None):
            print('si es verdad')
            operador.append(element)

        elif(resultadoLetra != None):
            print('si es verdad')
            palabras.append(element)

        else:
            print('no es correcto')
            errores.append(element)

    listBox.insert(END, ('token delimitador ', delimitador))

    listBox.insert(END, ('token palabras reservadas', reservadas))

    listBox.insert(END, ('token numeros ', numero))

    listBox.insert(END, ('token operadores ', operador))

    listBox.insert(END, ('token letras ', palabras))

    listBox.insert(END, ('errores ', errores))


def obtener_entrada():
    tipo = entrada.get().split(' ')
    expresion(tipo)

    letras = re.compile("(^([A-Z-a-z]+))")
    numeros = re.compile("(^([0-9]+))")
    operadores = re.compile("(^([-]|[+]|[*]|[/]))")


    pila = Pila()
    print('Vamos obtener entrada')
    lista_cadena_entrada = []
    entradaText = entrada.get()
    lista_cadena_entrada =  entradaText.split()

    pila.apilar('SC')
    pila.apilar('DFF')
    pila.apilar('SEC')
    pila.apilar('P')
    pila.apilar('DFI')
    pila.apilar('SA')
    pila.apilar('DF')
    print('Valores de inicio de la pila: ')
    pila.ver_pila()

    # print(lista_cadena_entrada)
    valorPila = pila.desapilar()


    if valorPila == 'DF':
        valor0Matriz = str(matrizPredictiva.at['DF','<'])
        posicion0= str(lista_cadena_entrada[0])
        pila.apilar(posicion0)
        pila.ver_pila()
        valorPila= pila.desapilar()
        if valor0Matriz == '1' and valorPila == '<':
            print('pasa')
            pila.ver_pila()
            valor1Matriz = str(matrizPredictiva.at['SA','<'])
            posicion0= str(lista_cadena_entrada[0])
            pila.desapilar()
            pila.apilar(posicion0)
            pila.ver_pila()
            valorPila = pila.desapilar()

            if valor1Matriz == '2' and valorPila == '<':
                print('pasa')
                pila.ver_pila()
                posicion1 = str(lista_cadena_entrada[1])
                valor2Matriz = str(matrizPredictiva.at['DFI','Diagrama'])
                pila.desapilar()
                pila.apilar(posicion1)
                pila.ver_pila()
                valorPila= pila.desapilar()
                if valor2Matriz == '3' and valorPila == 'Diagrama':
                    print('pasa')
                    pila.ver_pila()
                    pila.desapilar()
                    posicion3 = str(lista_cadena_entrada[2])
                    valor3Matriz = str(matrizPredictiva.at['P',':'])
                    pila.apilar(posicion3)
                    pila.ver_pila()
                    valorPila = pila.desapilar()
                    pila.ver_pila()
                    if valor3Matriz == '4' and valorPila == ':':
                        print('pasa \n')
                        print("pila SEC \n")
                        pilaSec = Pila()
                        pilaSec.apilar('RESTOSEC')
                        pilaSec.apilar('ENTRY')
                        pilaSec.apilar('INI')
                        pilaSec.ver_pila()

                        pilaSec.desapilar()
                        posicion4 = str(lista_cadena_entrada[3])
                        valo4Matriz = str(matrizPredictiva.at['INI','inicio'])
                        pilaSec.apilar(posicion4)
                        pilaSec.ver_pila()
                        valorPila= pilaSec.desapilar()
                        if valo4Matriz == '7' and valorPila =='inicio':

                            pilaSec.ver_pila()
                            pilaSec.desapilar()
                            posicion5 = str(lista_cadena_entrada[4])
                            valo5Matriz = str(matrizPredictiva.at['ENTRY','a..z | A..Z'])
                            pilaSec.apilar(posicion5)
                            pilaSec.ver_pila()
                            valorPila= pilaSec.desapilar()
                            resultadoPila = re.fullmatch(letras,valorPila)
                            pilaSec.ver_pila()
                            if valo5Matriz == '8' and resultadoPila !=None:

                                print("\npila RESTOSEC")
                                pilaRestoSec = Pila()
                                pilaRestoSec.apilar('FINAL')
                                pilaRestoSec.apilar('IMPRESION')
                                pilaRestoSec.apilar('PROCESO')
                                pilaRestoSec.ver_pila()


                                print("\npila PROCESO")
                                pilaProceso = Pila()
                                pilaProceso.apilar('RESTOPROCESO')
                                pilaProceso.apilar('=')
                                pilaProceso.apilar('VARIABLE')
                                pilaProceso.ver_pila()

                                pilaProceso.desapilar()
                                posicion6 = str(lista_cadena_entrada[5])
                                pilaProceso.apilar(posicion6)
                                pilaProceso.ver_pila()
                                valorPila= pilaProceso.desapilar()
                                resultadoPila = re.fullmatch(letras,valorPila)
                                valo6Matriz = str(matrizPredictiva.at['VARIABLE','a..z | A..Z'])

                                if valo6Matriz == '9' and resultadoPila != None:
                                    print('Entra variable proceso')
                                    pilaProceso.ver_pila()
                                    pilaProceso.desapilar()
                                    pilaProceso.ver_pila()
                                    posicion7 = str(lista_cadena_entrada[6])
                                    valo7Matriz = str(matrizPredictiva.at['IGUAL','='])
                                    pilaProceso.apilar(posicion7)
                                    pilaProceso.ver_pila()
                                    valorPila = pilaProceso.desapilar()
                                    if valo7Matriz == '20' and valorPila == '=':
                                        print('pasa el igual')
                                        pilaProceso.ver_pila()

                                        #Resto proceso
                                        print("\npila RESTOPROCESO ")
                                        pilaRestoProceso = Pila()
                                        pilaRestoProceso.apilar('X')
                                        pilaRestoProceso.apilar('OPERADOR')
                                        pilaRestoProceso.apilar('VARIABLE')
                                        pilaRestoProceso.ver_pila()
                                        pilaRestoProceso.desapilar()

                                        posicion8 = str(lista_cadena_entrada[7])
                                        valo8Matriz = str(matrizPredictiva.at['VARIABLE','a..z | A..Z'])

                                        pilaRestoProceso.apilar(posicion8)
                                        pilaRestoProceso.ver_pila()
                                        valorPila= pilaRestoProceso.desapilar()
                                        resultadoPila = re.fullmatch(letras,valorPila)
                                        resultadoPilaNumero = re.fullmatch(numeros,valorPila)

                                        if valo8Matriz == '9' and resultadoPila != None:
                                            print("pasa")
                                            pilaRestoProceso.ver_pila()
                                            pilaRestoProceso.desapilar()
                                            posicion9 = str(lista_cadena_entrada[8])
                                            valo9Matriz = str(matrizPredictiva.at['OPERADOR','+|-|/|*'])
                                            pilaRestoProceso.apilar(posicion9)
                                            pilaRestoProceso.ver_pila()
                                            valorPila = pilaRestoProceso.desapilar()

                                            resultadoPilaOperadores = re.fullmatch(operadores,valorPila)
                                            if valo9Matriz == '15' and resultadoPilaOperadores != None:
                                                pilaRestoProceso.ver_pila()
                                                pilaX = Pila()
                                                pilaX.apilar('VARIABLE')
                                                pilaX.ver_pila()
                                                pilaX.desapilar()
                                                posicion10 = str(lista_cadena_entrada[9])
                                                pilaX.apilar(posicion10)
                                                valo10Matriz = str(matrizPredictiva.at['VARIABLE','a..z | A..Z'])
                                                valorPila = pilaX.desapilar()
                                                resultadoPila = re.fullmatch(letras,valorPila)

                                                if valo10Matriz == '9' and resultadoPila != None:
                                                    print('pasa')
                                                    pilaX.ver_pila()
                                                    print('\nvolvemos a la pila restoSec porque todo el proceso ya cumplio')
                                                    pilaRestoSec.desapilar()
                                                    pilaRestoSec.ver_pila()
                                                    pilaRestoSec.desapilar()
                                                    posicion11 = str(lista_cadena_entrada[10])
                                                    valo11Matriz = str(matrizPredictiva.at['IMPRESION','a..z | A..Z'])
                                                    pilaRestoSec.apilar(posicion11)
                                                    pilaRestoSec.ver_pila()
                                                    valorPila = pilaRestoSec.desapilar()
                                                    resultadoPila = re.fullmatch(letras,valorPila)

                                                    if valo11Matriz == '16' and resultadoPila != None:
                                                        pilaRestoSec.ver_pila()
                                                        pilaRestoSec.desapilar()
                                                        posicion11 = str(lista_cadena_entrada[11])
                                                        valo11Matriz = str(matrizPredictiva.at['FINAL','final'])
                                                        pilaRestoSec.apilar(posicion11)
                                                        pilaRestoSec.ver_pila()
                                                        valorPila = pilaRestoSec.desapilar()
                                                        if valo11Matriz == '17' and valorPila == 'final':
                                                            print('espera la primera pila y eliminamos todo lo que se hizo en SEC')
                                                            pila.ver_pila()
                                                            pila.desapilar()
                                                            pila.desapilar()
                                                            posicion12 = str(lista_cadena_entrada[12])
                                                            valo12Matriz = str(matrizPredictiva.at['DFF','DiagramaFlujo'])
                                                            pila.apilar(posicion12)
                                                            pila.ver_pila()
                                                            valorPila = pila.desapilar()
                                                            if valo12Matriz == '18' and valorPila == 'DiagramaFlujo':
                                                                print('final')
                                                                pila.ver_pila()
                                                                pila.desapilar()
                                                                posicion13 = str(lista_cadena_entrada[13])
                                                                valo13Matriz = str(matrizPredictiva.at['SC','>'])
                                                                print(valo13Matriz)
                                                                pila.apilar(posicion13)
                                                                pila.ver_pila()
                                                                valorPila = pila.desapilar()

                                                                if valo13Matriz == '19' and valorPila == '>':
                                                                    print('la pila esta vacia ',pila.esta_vacia())

                                                                    listBoxtwo.insert(END, ('Lo que ingreso es correcto'))
                                                                    print('La cadena es correcta')

                                                                #en esta parte es donde pongo el metodo para bibujar las salida
                                                                    threading.Thread(target=dibujar_salida(lista_cadena_entrada)).start()
                                                                    
                                                                else:
                                                                    listBoxtwo.insert(END, ('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla'))
                                                                    print('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla')
                                                            else:
                                                                listBoxtwo.insert(END, ('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla'))
                                                                print('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla')
                                                        else:
                                                            listBoxtwo.insert(END, ('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla'))
                                                            print('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla')
                                                    else:
                                                        listBoxtwo.insert(END, ('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla'))
                                                        print('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla')
                                                else:
                                                    pilaX = Pila()
                                                    pilaX.apilar('NUMERO')
                                                    pilaX.ver_pila()
                                                    pilaX.desapilar()
                                                    posicion10 = str(lista_cadena_entrada[9])
                                                    valo10Matriz = str(matrizPredictiva.at['NUMERO','0..9'])
                                                    pilaX.apilar(posicion10)
                                                    pilaX.ver_pila()
                                                    valorPila = pilaX.desapilar()
                                                    resultadoPila = re.fullmatch(numeros,valorPila)
                                                    if valo10Matriz == '14' and resultadoPila !=None:

                                                        print('\nvolvemos a la pila restoSec porque todo el proceso ya cumplio')
                                                        pilaRestoSec.desapilar()
                                                        pilaRestoSec.ver_pila()
                                                        pilaRestoSec.desapilar()
                                                        posicion11 = str(lista_cadena_entrada[10])
                                                        valo11Matriz = str(matrizPredictiva.at['IMPRESION','a..z | A..Z'])
                                                        pilaRestoSec.apilar(posicion11)
                                                        pilaRestoSec.ver_pila()
                                                        valorPila = pilaRestoSec.desapilar()
                                                        resultadoPila = re.fullmatch(letras,valorPila)

                                                        if valo11Matriz == '16' and resultadoPila != None:
                                                            pilaRestoSec.ver_pila()
                                                            pilaRestoSec.desapilar()
                                                            posicion11 = str(lista_cadena_entrada[11])
                                                            valo11Matriz = str(matrizPredictiva.at['FINAL','final'])
                                                            pilaRestoSec.apilar(posicion11)
                                                            pilaRestoSec.ver_pila()
                                                            valorPila = pilaRestoSec.desapilar()
                                                            if valo11Matriz == '17' and valorPila == 'final':
                                                                print('espera la primera pila y eliminamos todo lo que se hizo en SEC')
                                                                pila.ver_pila()
                                                                pila.desapilar()
                                                                pila.desapilar()
                                                                posicion12 = str(lista_cadena_entrada[12])
                                                                valo12Matriz = str(matrizPredictiva.at['DFF','DiagramaFlujo'])
                                                                pila.apilar(posicion12)
                                                                pila.ver_pila()
                                                                valorPila = pila.desapilar()
                                                                if valo12Matriz == '18' and valorPila == 'DiagramaFlujo':
                                                                    print('final')
                                                                    pila.ver_pila()
                                                                    pila.desapilar()
                                                                    posicion13 = str(lista_cadena_entrada[13])
                                                                    valo13Matriz = str(matrizPredictiva.at['SC','>'])
                                                                    print(valo13Matriz)
                                                                    pila.apilar(posicion13)
                                                                    pila.ver_pila()
                                                                    valorPila = pila.desapilar()

                                                                    if valo13Matriz == '19' and valorPila == '>':
                                                                        print('la pila esta vacia ',pila.esta_vacia())
                                                                        print('La cadena es correcta')
                                                                        listBoxtwo.insert(END, ('La cadena es correcta'))
                                                                        #aqui tambien tengo que poner el metodo que dibuja
                                                                        threading.Thread(target=dibujar_salida(lista_cadena_entrada)).start()
                                                                            
                                                                    else:
                                                                        listBoxtwo.insert(END, ('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla'))
                                                                        print('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla')
                                                                else:
                                                                    listBoxtwo.insert(END, ('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla'))
                                                                    print('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla')
                                                            else:
                                                                listBoxtwo.insert(END, ('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla'))
                                                                print('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla')
                                                        else:
                                                            listBoxtwo.insert(END, ('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla'))
                                                            print('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla')
                                                    else:
                                                        listBoxtwo.insert(END, ('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla'))
                                                        print('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla')

                                            else:
                                                listBoxtwo.insert(END, ('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla'))
                                                print('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla')

                                        else:

                                            if resultadoPilaNumero != None:
                                                print("entra numero")
                                                pilaRestoProcesotwo = Pila()
                                                pilaRestoProcesotwo.apilar('ENTRY')
                                                pilaRestoProcesotwo.apilar('OPERADOR')
                                                pilaRestoProcesotwo.apilar('NUMERO')
                                                pilaRestoProcesotwo.ver_pila()

                                                pilaRestoProcesotwo.desapilar()
                                                posicion8 = str(lista_cadena_entrada[7])
                                                pilaRestoProcesotwo.apilar(posicion8)
                                                pilaRestoProcesotwo.ver_pila()
                                                valorPila = pilaRestoProcesotwo.desapilar()
                                                resultadoPilaNumero = re.fullmatch(numeros,valorPila)
                                                valo8Matriz = str(matrizPredictiva.at['NUMERO','0..9'])


                                                if valo8Matriz == '14' and resultadoPilaNumero != None:
                                                    pilaRestoProcesotwo.ver_pila()
                                                    pilaRestoProcesotwo.desapilar()
                                                    posicion9 = str(lista_cadena_entrada[8])
                                                    pilaRestoProcesotwo.apilar(posicion9)
                                                    pilaRestoProcesotwo.ver_pila()
                                                    valo9Matriz = str(matrizPredictiva.at['OPERADOR','+|-|/|*'])
                                                    valorPila = pilaRestoProcesotwo.desapilar()
                                                    resultadoPilaOperadores = re.fullmatch(operadores,valorPila)
                                                    pilaRestoProcesotwo.ver_pila()

                                                    if valo9Matriz == '15' and resultadoPilaOperadores != None:

                                                        pilaRestoProcesotwo.desapilar()
                                                        posicion10 = str(lista_cadena_entrada[9])
                                                        pilaRestoProcesotwo.apilar(posicion10)
                                                        pilaRestoProcesotwo.ver_pila()
                                                        valorPila = pilaRestoProcesotwo.desapilar()
                                                        valo10Matriz = str(matrizPredictiva.at['ENTRY','a..z | A..Z'])
                                                        resultadoPila = re.fullmatch(letras,valorPila)

                                                        if valo10Matriz == '8' and resultadoPila != None:
                                                            print('\nvolvemos a la pila restoSec porque todo el proceso ya cumplio')
                                                            pilaRestoSec.desapilar()
                                                            pilaRestoSec.ver_pila()
                                                            pilaRestoSec.desapilar()
                                                            posicion11 = str(lista_cadena_entrada[10])
                                                            valo11Matriz = str(matrizPredictiva.at['IMPRESION','a..z | A..Z'])
                                                            pilaRestoSec.apilar(posicion11)
                                                            pilaRestoSec.ver_pila()
                                                            valorPila = pilaRestoSec.desapilar()
                                                            resultadoPila = re.fullmatch(letras,valorPila)

                                                            if valo11Matriz == '16' and resultadoPila != None:
                                                                pilaRestoSec.ver_pila()
                                                                pilaRestoSec.desapilar()
                                                                posicion11 = str(lista_cadena_entrada[11])
                                                                valo11Matriz = str(matrizPredictiva.at['FINAL','final'])
                                                                pilaRestoSec.apilar(posicion11)
                                                                pilaRestoSec.ver_pila()
                                                                valorPila = pilaRestoSec.desapilar()
                                                                if valo11Matriz == '17' and valorPila == 'final':
                                                                    print('espera la primera pila y eliminamos todo lo que se hizo en SEC')
                                                                    pila.ver_pila()
                                                                    pila.desapilar()
                                                                    pila.desapilar()
                                                                    posicion12 = str(lista_cadena_entrada[12])
                                                                    valo12Matriz = str(matrizPredictiva.at['DFF','DiagramaFlujo'])
                                                                    pila.apilar(posicion12)
                                                                    pila.ver_pila()
                                                                    valorPila = pila.desapilar()
                                                                    if valo12Matriz == '18' and valorPila == 'DiagramaFlujo':
                                                                        print('final')
                                                                        pila.ver_pila()
                                                                        pila.desapilar()
                                                                        posicion13 = str(lista_cadena_entrada[13])
                                                                        valo13Matriz = str(matrizPredictiva.at['SC','>'])
                                                                        print(valo13Matriz)
                                                                        pila.apilar(posicion13)
                                                                        pila.ver_pila()
                                                                        valorPila = pila.desapilar()

                                                                        if valo13Matriz == '19' and valorPila == '>':
                                                                            print('la pila esta vacia ',pila.esta_vacia())
                                                                            print('La cadena es correcta')
                                                                            listBoxtwo.insert(END, ('La cadena es correcta'))

                                                                            #aqui tambien tengo que poner el metodo que dibuja
                                                                            threading.Thread(target = dibujar_salida(lista_cadena_entrada)).start()

                                                                        else:
                                                                            listBoxtwo.insert(END, ('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla'))
                                                                            print('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla')
                                                                    else:
                                                                        listBoxtwo.insert(END, ('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla'))
                                                                        print('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla')
                                                                else:
                                                                    listBoxtwo.insert(END, ('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla'))
                                                                    print('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla')

                                                            else:
                                                                listBoxtwo.insert(END, ('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla'))
                                                                print('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla')



                                                        else:
                                                            print('\nvolvemos a la pila restoSec porque todo el proceso ya cumplio')
                                                            pilaRestoSec.desapilar()
                                                            pilaRestoSec.ver_pila()
                                                            pilaRestoSec.desapilar()
                                                            posicion11 = str(lista_cadena_entrada[10])
                                                            valo11Matriz = str(matrizPredictiva.at['IMPRESION','a..z | A..Z'])
                                                            pilaRestoSec.apilar(posicion11)
                                                            pilaRestoSec.ver_pila()
                                                            valorPila = pilaRestoSec.desapilar()
                                                            resultadoPila = re.fullmatch(letras,valorPila)

                                                            if valo11Matriz == '16' and resultadoPila != None:
                                                                pilaRestoSec.ver_pila()
                                                                pilaRestoSec.desapilar()
                                                                posicion11 = str(lista_cadena_entrada[11])
                                                                valo11Matriz = str(matrizPredictiva.at['FINAL','final'])
                                                                pilaRestoSec.apilar(posicion11)
                                                                pilaRestoSec.ver_pila()
                                                                valorPila = pilaRestoSec.desapilar()
                                                                if valo11Matriz == '17' and valorPila == 'final':
                                                                    print('espera la primera pila')
                                                                    print('espera la primera pila y eliminamos todo lo que se hizo en SEC')
                                                                    pila.ver_pila()
                                                                    pila.desapilar()
                                                                    pila.desapilar()
                                                                    posicion12 = str(lista_cadena_entrada[12])
                                                                    valo12Matriz = str(matrizPredictiva.at['DFF','DiagramaFlujo'])
                                                                    pila.apilar(posicion12)
                                                                    pila.ver_pila()
                                                                    valorPila = pila.desapilar()
                                                                    if valo12Matriz == '18' and valorPila == 'DiagramaFlujo':
                                                                        print('final')
                                                                        pila.ver_pila()
                                                                        pila.desapilar()
                                                                        posicion13 = str(lista_cadena_entrada[13])
                                                                        valo13Matriz = str(matrizPredictiva.at['SC','>'])
                                                                        print(valo13Matriz)
                                                                        pila.apilar(posicion13)
                                                                        pila.ver_pila()
                                                                        valorPila = pila.desapilar()

                                                                        if valo13Matriz == '19' and valorPila == '>':
                                                                            print('la pila esta vacia ',pila.esta_vacia())
                                                                            print('La cadena es correcta')
                                                                            listBoxtwo.insert(END, ('La cadena es correcta'))

                                                                            #aqui tambien tengo que poner el metodo que dibuja
                                                                            threading.Thread(target=dibujar_salida(lista_cadena_entrada)).start()

                                                                        else:
                                                                            listBoxtwo.insert(END, ('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla'))
                                                                            print('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla')
                                                                else:
                                                                    listBoxtwo.insert(END, ('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla'))
                                                                    print('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla')
                                                            else:
                                                                listBoxtwo.insert(END, ('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla'))
                                                                print('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla')

                                                    else:
                                                        listBoxtwo.insert(END, ('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla'))
                                                        print('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla')

                                                else:
                                                    listBoxtwo.insert(END, ('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla'))
                                                    print('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla')

                                            else:
                                                listBoxtwo.insert(END, ('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla'))
                                                print('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla')
                                    else:

                                        if resultadoPila != None:
                                            print('')
                                            pilaRestoSec.ver_pila()
                                            pilaRestoSec.desapilar()
                                            posicion11 = str(lista_cadena_entrada[6])
                                            valo11Matriz = str(matrizPredictiva.at['FINAL','final'])
                                            pilaRestoSec.apilar(posicion11)
                                            pilaRestoSec.ver_pila()
                                            valorPila = pilaRestoSec.desapilar()
                                            if valo11Matriz == '17' and valorPila == 'final':
                                                print('espera la primera pila y eliminamos todo lo que se hizo en SEC')
                                                pila.ver_pila()
                                                pila.desapilar()
                                                pila.desapilar()
                                                posicion12 = str(lista_cadena_entrada[7])
                                                valo12Matriz = str(matrizPredictiva.at['DFF','DiagramaFlujo'])
                                                pila.apilar(posicion12)
                                                pila.ver_pila()
                                                valorPila = pila.desapilar()
                                                if valo12Matriz == '18' and valorPila == 'DiagramaFlujo':
                                                    print('final')
                                                    pila.ver_pila()
                                                    pila.desapilar()
                                                    posicion13 = str(lista_cadena_entrada[8])
                                                    valo13Matriz = str(matrizPredictiva.at['SC','>'])
                                                    print(valo13Matriz)
                                                    pila.apilar(posicion13)
                                                    pila.ver_pila()
                                                    valorPila = pila.desapilar()

                                                    if valo13Matriz == '19' and valorPila == '>':
                                                        print('la pila esta vacia ',pila.esta_vacia())
                                                        print('La cadena es correcta')
                                                        listBoxtwo.insert(END, ('La cadena es correcta'))

                                                        #aqui tambien tengo que poner el metodo que dibuja
                                                        threading.Thread(target=dibujar_salida(lista_cadena_entrada)).start()

                                                    else:
                                                        listBoxtwo.insert(END, ('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla'))
                                                        print('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla')
                                                else:
                                                    listBoxtwo.insert(END, ('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla'))
                                                    print('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla')
                                            else:
                                                listBoxtwo.insert(END, ('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla'))
                                                print('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla')

                                        else :
                                            listBoxtwo.insert(END, ('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla'))
                                            print('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla')


                                else:
                                    pilaProceso.apilar(valorPila)
                                    pilaProceso.ver_pila()
                                    listBoxtwo.insert(END, ('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla'))
                                    print('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla')

                            else:
                                pilaSec.apilar(valorPila)
                                pilaSec.ver_pila()
                                listBoxtwo.insert(END, ('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla'))
                                print('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla')


                        else:
                            pila.apilar(valorPila)
                            listBoxtwo.insert(END, ('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla'))
                            print('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla')
                    else:
                        listBoxtwo.insert(END, ('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla'))
                        print('El valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla')
                        pila.apilar(valorPila)
                else:
                    listBoxtwo.insert(END, ('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla'))
                    pila.apilar(valorPila)
                    print('El valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla')
            else:
                print('no pasa')
                pila.apilar(posicion0)
                pila.ver_pila()


        else:
            listBoxtwo.insert(END, ('el valor del tope de la pila: ', valorPila, ' no corresponde con lo que produce en la tabla'))
            print('el tope de la pila: ',valorPila,' no corresponde con lo que produce en la tabla')






ventana = Tk()
ventana.geometry('500x900')
ventana.config(bg='#E5E6E8')
ventana.title('Gramatica')

entrada = StringVar()

titulo = Label(ventana, text='GRAMATICA', fg='#72A7E9')
titulo.place(x=150, y=10)
titulo.config(font="Inter 27 italic bold", bg='#E5E6E8')

labelEntrada = Label(ventana, text='ENTRADA')
labelEntrada.place(x=30,y=105)
labelEntrada.config(font='Inter 10',bg='#E5E6E8')

labelSalida = Label(ventana, text='TOKEN')
labelSalida.place(x=30, y=300)
labelSalida.config(font='Inter 9',bg='#E5E6E8')

labelSalidaTwo = Label(ventana, text='ANALIZADOR SINTACTICO')
labelSalidaTwo.place(x=160, y=830)
labelSalidaTwo.config(font='Inter 9',bg='#E5E6E8')

cajaEntrada = Entry(ventana, font='arial 13', justify='center', textvariable=entrada, bg='#D3DAE2', bd=0)
cajaEntrada.place(x=30, y=100, width=435, height=36)

listBox = Listbox(ventana)
listBox.place(relx=0.18, rely=0.20, relwidth=0.7, relheight=0.3)

listBoxtwo = Listbox(ventana)
listBoxtwo.place(relx=0.18, rely=0.60, relwidth=0.7, relheight=0.3)

barra = Scrollbar(ventana, command=listBox.yview)
barra.place(relx=0.90, rely=0.35, relheight=0.3)

boton = Button(ventana, text='ACEPTAR', command=obtener_entrada)
boton.place(x=150, y=455, width=205, height=38)
boton.config(font='Inter 15', bg='#F8E000', fg='black', bd=0)

ventana.mainloop()