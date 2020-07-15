def diccionario_de_funciones(fuente_unico):
    """[Autor: Daniela Bolivar]
       [Ayuda: Crea un diccionario con las funciones del programa,
       a la vez crea un subdiccionario con las características vaciías de cada función]
    """

    diccionario_funciones={}
    for linea in fuente_unico:
        diccionario_funciones[linea[0]]={'Módulo':'', 'Parámetros': 0, 'Líneas':0, 'Invocaciones':[0], 'Returns':0, 'If': 0 , 'For': 0, 'While':0, 'Break':0, 'Exit':0, 'Coment':0, 'Ayuda':'','Autor':''}
    
    return diccionario_funciones


def funcion_codigo(lista):
    """[Autor: Daniela Bolivar]
       [Ayuda: Dada una línea, analiza el código perteneciente a la función que se encuentra en ella.
       Es decir, la cantidad de 'returns', 'if', 'for','while', 'breaks', 'exit']
    """
    # Como estamos trabajando con funciones, por definición sólo puede haber un return
    c_returns=1 
    c_if=0
    c_for=0
    c_while=0
    c_break=0
    c_exit=0

    for i in range (3, len(lista)):
        if 'if ' in lista[i] or 'elif ' in lista[i]:
            c_if+=1

        elif 'for ' in lista[i]:
            c_for+=1

        elif 'while ' in lista[i]:
            c_while+=1

        elif 'break' in lista[i]:
            c_break+=1

        elif 'exit' in lista[i]:
            c_exit+=1
        

    return [c_returns, c_if, c_for, c_while, c_break, c_exit]


def invocacion_a_funcion(funcion,lista):
    """[Autor: Daniela Bolivar]
       [Ayuda: Dada una función 'x' del programa, se analiza si ésta invoca a otra función 'y']
    """

    invocacion_por_funcion=[]
    
    k=0

    for i in range(3,len(lista)):
        
            if funcion in lista[i]:
            #Cuento la cantidad de veces que la función 'x' es invocada por la función 'y'      
            k+=1
    
    #si la función 'x' fue invocada, genero una lista 
    # donde la primer componente es el nombre de la función 'y' y la segunda componente las veces que las veces que fue invocada la función 'x' 
    if k!=0: 

        invocacion_por_funcion=[lista[0],k]

    return invocacion_por_funcion
            

def analisis_codigo_funciones(fuente_unico):
    """[Autor: Daniela Bolivar]
       [Ayuda: dado el archivo funte_unico.csv se analizará el código de cada una de las funciones en el archivo.
       El resultado del análisis quedará cargado en un diccionario]
    """
    #Genero el diccionario
    diccionario_funciones= diccionario_de_funciones(fuente_unico) 

    
    #Recorro línea por línea el csv
    for linea in fuente_unico:
        #transfomo la línea a analizar en una lista
        lista=linea.strip().split(',') 

        #Analizo si hay funciones invocadas por la función de la línea
        for funcion in diccionario_funciones: 

            if funcion != lista[0]: # Descarto qu esté analizando la línea donde se define la función

                invocacion_a_funcion(funcion,lista)

                diccionario_funciones[funcion]['Invocaciones'][0]+=invocacion_a_funcion(funcion,lista)[1]
                diccionario_funciones[funcion]['Invocaciones'].append(invocacion_a_funcion(funcion,lista))

        
        funcion_codigo(lista) #Analizo el resto del código de la línea

        #Completo el diccionario
        diccionario_funciones[lista[0]]['Módulo']=lista[2]
        diccionario_funciones[lita[0]]['Parámetros']=len(lista[1])
        diccionario_funciones[lita[0]]['Líneas']=len(lista)-3
        diccionario_funciones[lita[0]]['Returns']=funcion_codigo(lista)[0]
        diccionario_funciones[lita[0]]['If']=funcion_codigo(lista)[1]
        diccionario_funciones[lita[0]]['For']=funcion_codigo(lista)[2]
        diccionario_funciones[lita[0]]['While']=funcion_codigo(lista)[3]
        diccionario_funciones[lita[0]]['Break']=funcion_codigo(lista)[4]
        diccionario_funciones[lita[0]]['Exit']=funcion_codigo(lista)[5]

    return diccionario_funciones


def funcion_comentarios(linea):
    """[Autor: Daniela Bolivar]
       [Ayuda: Dada una línea, analiza los comentarios pertenecientes a la función que se encuentra en ella.
       Es decir la cantidad de líneas de comentarios, si existe la descripcción de la función y el autor de esta]
    """

    lista=linea.strip().split(',')

    comentarios=len(lista)-3
        
    autor= lista[1]

    ayuda= 'Si'
    if lista[2]=='':
        ayuda='No'

    return [comentarios, ayuda, autor]


def analisis_comentarios_funciones(diccionario_funciones,comentarios):
    """[Autor: Daniela Bolivar]
       [Ayuda: Dado el archivo comentarios.csv se analizarán los comentarios de cada una de las funciones del archivo.
       El análisis será cargado a un diccionario que se le entrega a la función.]
    """

    for linea in comentarios: #Recorro línea por línea comentarios.csv

        funcion_comentarios(linea)

        diccionario_funciones[lista[0]]['Coment']=funcion_comentarios(linea)[0]
        diccionario_funciones[lita[0]]['Ayuda']=funcion_comentarios(linea)[1]
        diccionario_funciones[lita[0]]['Autor']=funcion_comentarios(linea)[2]

    return diccionario_funciones


def panel_de_funciones(fuente_unico, comentarios):
    """[Autor: Daniela Bolivar]
       [Ayuda: dados los archivos fuente_unico.csv y comentarios.csv se crea un archivo csv 
       que contiene la información de cada una de las funciones]
    """
    columnas=[FUNCION, Parámetros, Líneas, Invocaciones, Returns, If/Elif, For, While, Break, Exit, Coment, Ayuda, Autor]

     writer=csv.DictWriter(panel_general, fieldnames=columnas) #Creo un diccionario 

     writer.writeheader() #Escribo el nombre de las columnas

     #Creo el diccionario que analiza ambos archivos csv a la vez
     diccionario_funciones=analisis_comentarios_funciones(analisis_codigo_funciones(fuente_unico),comentarios)


     #Escrivo un csv donde cada línea corresponde al análisis de una función
     for funcion in diccionario_funciones:
        
         writer.writerow({'FUNCION': funcion . diccionario_funciones[funcion]['Modulo'] , 'Parámetros': diccionario_funciones[funcion]['Parámetros'], 'Líneas': diccionario_funciones[funcion]['Líneas'], 'Invocaciones': diccionario_funciones[funcion]['Invocaciones'][0], 'Returns':diccionario_funciones[funcion]['Returns'], 'If/Elif':diccionario_funciones[funcion]['If'], 'For':diccionario_funciones[funcion]['For'], 'While':diccionario_funciones[funcion]['While'], 'Break':diccionario_funciones[funcion]['Break'], 'Exit':diccionario_funciones[funcion]['Exit'], 'Coment':diccionario_funciones[funcion]['Coment'] , 'Ayuda':diccionario_funciones[funcion]['Ayuda'], 'Autor':diccionario_funciones[funcion]['Autor']  } )


    return 






#Main
import csv
fuente_unico= open('fuente_unico.csv','r' )

comentarios= open('comentaios.csv','r' )

panel_general= open('panel_general.csv','w', newline='' )


fuente_unico.close()

comentarios.close()

panel_general.close()

