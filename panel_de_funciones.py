def diccionario_de_funciones(fuente_unico):
    """[Autor: Daniela Bolivar]
       [Ayuda: Crea un diccionario con las funciones del programa,
       a la vez crea un subdiccionario con las características vaciías de cada función]
    """

    diccionario_funciones={}
    for linea in fuente_unico:
        diccionario_funciones[linea[0]]={'Funcion.Módulo':'', 'Parámetros': 0, 'Líneas':0, 'Invocaciones':0, 'Returns':0, 'If': 0 , 'For': 0, 'While':0, 'Break':0, 'Exit':0, 'Coment':0, 'Ayuda':'','Autor':''}
    
    return diccionario_funciones


def funcion_codigo(lista):
    """[Autor: Daniela Bolivar]
       [Ayuda: Dada una línea, analiza el código perteneciente a la función que se encuentra en ella.
       Es decir, la cantidad de 'returns', 'if', 'for','while', 'breaks', 'exit']
    """
    
    c_returns=0 
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
        
        elif 'return 'in lista[i]:
            c_returns+=1
        
    return [c_returns, c_if, c_for, c_while, c_break, c_exit]


def invocacion_a_funcion(funcion,lista):
    """[Autor: Daniela Bolivar]
       [Ayuda: Dada una función 'x' del programa, se analiza si ésta invoca a otra función 'y']
    """

    invocacion_por_funcion=0
    
    k=0

    for i in range(3,len(lista)):
        
            if funcion in lista[i]:
            #Cuento la cantidad de veces que la función 'x' es invocada por la función 'y'      
             k+=1
    
    #si la función 'x' fue invocada, genero una lista 
    # donde la primer componente es el nombre de la función 'y' y la segunda componente las veces que las veces que fue invocada la función 'x' 
    if k!=0: 

        invocacion_por_funcion=k

    return invocacion_por_funcion


def cantidad_parametros_codigo(lista):
    """[Autor: Daniela Bolivar]
       [Ayuda: Esta función se utilizará para contar los parámetros de una función por eso es que se analiza
       a partir de la componente 1 de la lista]
    """
    n=0
    T=True
    k=1
    while T and k< len(lista):
        if ')' in lista[k]:
            T=False
            
        n+=1
        if '()' in lista[k]:
            T=False
            n=0
        k+=1
    #Se le suma 1 a la resta porque la tercera componente es el módulo
    k=len(lista)-(k+1)
    return n,k            

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
        lista=linea.rstrip('\n').split(',') 

        #Analizo si hay funciones invocadas por la función de la línea
        for funcion in diccionario_funciones: 

            if funcion != lista[0]: # Descarto que esté analizando la línea donde se define la función

                invocacion_a_funcion(funcion,lista)

                diccionario_funciones[funcion]['Invocaciones']+=invocacion_a_funcion(funcion,lista)
                

        
        funcion_codigo(lista) #Analizo el resto del código de la línea

        #Completo el diccionario
        diccionario_funciones[lista[0]]['Funcion.Módulo']=str(lista[0])+'.'+str(lista[2])
        diccionario_funciones[lista[0]]['Parámetros']=cantidad_parametros_codigo(lista)[0]
        diccionario_funciones[lista[0]]['Líneas']=cantidad_parametros_codigo(lista)[1]
        diccionario_funciones[lista[0]]['Returns']=funcion_codigo(lista)[0]
        diccionario_funciones[lista[0]]['If']=funcion_codigo(lista)[1]
        diccionario_funciones[lista[0]]['For']=funcion_codigo(lista)[2]
        diccionario_funciones[lista[0]]['While']=funcion_codigo(lista)[3]
        diccionario_funciones[lista[0]]['Break']=funcion_codigo(lista)[4]
        diccionario_funciones[lista[0]]['Exit']=funcion_codigo(lista)[5]

    return diccionario_funciones


def funcion_comentarios(linea):
    """[Autor: Daniela Bolivar]
       [Ayuda: Dada una línea, analiza los comentarios pertenecientes a la función que se encuentra en ella.
       Es decir la cantidad de líneas de comentarios, si existe la descripcción de la función y el autor de esta]
    """

    lista=linea.strip().split(',')

    comentarios=len(lista)-3

    if lista[1]==' ':
        autor='Anónimo'
    else:     
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

        lista=funcion_comentarios(linea)

        diccionario_funciones[lista[0]]['Coment']=funcion_comentarios(linea)[0]
        diccionario_funciones[lista[0]]['Ayuda']=funcion_comentarios(linea)[1]
        diccionario_funciones[lista[0]]['Autor']=funcion_comentarios(linea)[2]

    return diccionario_funciones


def longitud_columna(palabra,clave,diccionario):
    """[Autor: Daniela Bolivar]
       [Ayuda: Danda una palabra, comparo su longitud con la correspondiente a los elementos que se obtienen
       del diccionario en la clave  ingresados.
       La función devuelve el máximo número que se obtiene de estas comparaciones más dos]
    """
    n=len(palabra)

    for funciones in diccionario: #Recorro el diccionario ingresado con la clave ingresada

        if n<len(diccionario[funciones][clave]):
            n=len(diccionario[funciones][clave])

    return n+2

def longitud_caracteres(lista):
    """[Autor: Daniela Bolivar]
       [Ayuda: Danda una lista, obtengo la longitud de cada elemento de esta y le sumo dos, estos resultados son
       guardados en otra lista que es devuelta por la función]
    """
    longitud=[]

    for i in range(0,len(lista)):
        longitud.append(len(lista[i])+1)
    
    return longitud




def panel_de_funciones(archivo, fuente_unico, comentarios):
    
    """[Autor: Daniela Bolivar]
       [Ayuda: Dados los archivos fuente_unico.csv y comentarios.csv se escribe sobre un "archivo" csv 
        la información de cada una de las funciones]
    """
    #Creo el diccionario que analiza ambos archivos csv a la vez
    diccionario_funciones=analisis_comentarios_funciones(analisis_codigo_funciones(fuente_unico),comentarios)

    #Los Campos 'FUNCION' y 'Autor' son los únicos campos del diccionario en los cuales la no se puede  
    #predecir la longitud de caracteres que necesitará la columna, por eso se aplica la función 'longitud_columna()'
    
    n=longitud_columna('FUNCION','Funcion.Modulo',diccionario_funciones)

    m=longitud_columna('Autor','Autor',diccionario_funciones)

    #En los demás campos del diccionario, se obtendrán números, por eso bastará con que la longitud de la
    #columna se restrinja a la longitud del título

    columnas=['Parámetros', 'Líneas', 'Invocaciones', 'Returns', 'If/Elif', 'For', 'While', 'Break', 'Exit', 'Coment', 'Ayuda']

    longitud=longitud_caracteres(columnas)


    #En el archivo csv escribo el título de las columnas y a la vez los imprimo por pantalla los dejo centrados
    print('FUNCION',' '*(n-len('FUNCION')),'|Líneas ', '|Invocaciones ', '|Returns ', '|If/Elif ', '|For ', '|While ', '|Break ', '|Exit ', '|Coment ', '|Ayuda ', '|Autor ',' '*(n-len('FUNCION')),'|')
    
    archivo.write('{},{},{},{},{},{},{},{},{},{},{},{},{}\n'.format('FUNCION', 'Parámetros', 'Líneas', 'Invocaciones', 'Returns', 'If/Elif', 'For', 'While', 'Break', 'Exit', 'Coment', 'Ayuda', 'Autor'))

    #Escribo el archivo csv, donde cada línea corresponde al análisis de una función y a la vez los imprimo el análisis por pantalla
    for funcion in diccionario_funciones:

        print(diccionario_funciones[funcion]['Funcion.Modulo'], ' '*(n-len(diccionario_funciones[funcion]['Funcion.Modulo'])),'|', diccionario_funciones[funcion]['Parámetros'],' '*(longitud[0]-len(str(diccionario_funciones[funcion]['Parámetros']))),'|', diccionario_funciones[funcion]['Líneas'],' '*(longitud[1]-len(str(diccionario_funciones[funcion]['Líneas']))),'|', diccionario_funciones[funcion]['Invocaciones'],' '*(longitud[2]-len(str(diccionario_funciones[funcion]['Invocaciones']))),'|', diccionario_funciones[funcion]['Returns'],' '*(longitud[3]-len(str(diccionario_funciones[funcion]['Returns']))),'|', diccionario_funciones[funcion]['If'],' '*(longitud[4]-len(str(diccionario_funciones[funcion]['If']))),'|', diccionario_funciones[funcion]['For'],' '*(longitud[5]-len(str(diccionario_funciones[funcion]['For']))),'|', diccionario_funciones[funcion]['While'],' '*(longitud[6]-len(str(diccionario_funciones[funcion]['While']))),'|', diccionario_funciones[funcion]['Break'],' '*(longitud[7]-len(str(diccionario_funciones[funcion]['Break']))),'|', diccionario_funciones[funcion]['Exit'],' '*(longitud[8]-len(str(diccionario_funciones[funcion]['Exit']))),'|', diccionario_funciones[funcion]['Coment'],' '*(longitud[9]-len(str(diccionario_funciones[funcion]['Coment']))),'|', diccionario_funciones[funcion]['Ayuda'],' '*(longitud[10]-len(diccionario_funciones[funcion]['Ayuda'])),'|', diccionario_funciones[funcion]['Autor'], ' '*(m-len(diccionario_funciones[funcion]['Autor'])),'|')

        archivo.write('{},{},{},{},{},{},{},{},{},{},{},{},{}\n'.format( diccionario_funciones[funcion]['Funcion.Modulo'] , diccionario_funciones[funcion]['Parámetros'], diccionario_funciones[funcion]['Líneas'], diccionario_funciones[funcion]['Invocaciones'][0], diccionario_funciones[funcion]['Returns'], diccionario_funciones[funcion]['If'], diccionario_funciones[funcion]['For'], diccionario_funciones[funcion]['While'], diccionario_funciones[funcion]['Break'], diccionario_funciones[funcion]['Exit'], diccionario_funciones[funcion]['Coment'] , diccionario_funciones[funcion]['Ayuda'], diccionario_funciones[funcion]['Autor'] ))

    return 


def generacion_archivo():
    """[Autor: Daniela Bolivar]
       [Ayuda: Esta función abre los archivos correspondientes, crea el archivo pedido e imprime la información]
    """
    fuente_unico= open('fuente_unico.csv','r' )

    comentarios= open('comentaios.csv','r' )

    panel_general= open('panel_general.csv','w')

    panel_de_funciones(panel_general, fuente_unico, comentarios)


    fuente_unico.close()

    comentarios.close()

    panel_general.close()

    return


generacion_archivo()
