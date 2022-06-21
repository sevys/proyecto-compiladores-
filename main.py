from msilib.schema import ListBox
from tkinter import *
import re


def obetener_entrada():
    tipo = entrada.get().split(' ')

    expresion(tipo)


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



ventana = Tk()
ventana.geometry('500x600')
ventana.config(bg='#E5E6E8')
ventana.title('Gramatica')

entrada = StringVar()

titulo = Label(ventana, text='GRAMATICA', fg='#72A7E9')
titulo.place(x=150, y=10)
titulo.config(font="Inter 27 italic bold", bg='#E5E6E8')

labelEntrada = Label(ventana, text='ENTRADA')
labelEntrada.place(x=30,y=105)
labelEntrada.config(font='Inter 10',bg='#E5E6E8')

labelSalida = Label(ventana, text='SALIDA')
labelSalida.place(x=30, y=300)
labelSalida.config(font='Inter 10',bg='#E5E6E8')

cajaEntrada = Entry(ventana, font='arial 13', justify='center', textvariable=entrada, bg='#D3DAE2', bd=0)
cajaEntrada.place(x=30, y=130, width=435, height=36)

listBox = Listbox(ventana)
listBox.place(relx=0.18, rely=0.35, relwidth=0.7, relheight=0.3)

barra = Scrollbar(ventana, command=listBox.yview)
barra.place(relx=0.90, rely=0.35, relheight=0.3)

boton = Button(ventana, text='ACEPTAR', command=obetener_entrada)
boton.place(x=150, y=500, width=205, height=38)
boton.config(font='Inter 15', bg='#F8E000', fg='black', bd=0)

ventana.mainloop()