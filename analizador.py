def diccionario_de_invocaciones(fuente_unico):
    """[Autor: Daniela Bolivar]
       [Ayuda: Crea un diccionario con las funciones del programa y a cada función le asigna un número por orden de aparición en el archivo.
       A la vez crea un subdiccionario con las características vaciías de cada función]
    """
    n=1 #Variable que se utiliza para asignar un número a la funcion
    diccionario_de_invocaciones={}
    for linea in fuente_unico:
        diccionario_de_invocaciones[linea[0]]={'Columna':n,'Invoca':[], 'Llamada':[] , 'Total Invocaciones':0}
        n+=1
    
    return diccionario_de_invocaciones

def invocacion_a_funcion(funcion,lista):
    """[Autor: Daniela Bolivar]
       [Ayuda: Dada una función 'x' del programa se analiza si ésta invoca a otra función 'y']
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
       [Ayuda: Dado el archivo funte_unico.csv se analizará el código de cada una de las funciones en el archivo.
       El resultado del análisis quedará cargado en un diccionario]
    """
    #Genero el diccionario
    diccionario= diccionario_de_invocaciones(fuente_unico)

    n=0 #Servirá como contador de funciones
    #Recorro línea por línea el csv
    for linea in fuente_unico:
        #transfomo la línea a analizar en una lista
        lista=linea.rstrip('\n').split(',') 

        n+=1

        #Analizo si hay funciones invocadas por la función de la línea
        #Para que los comentarios tengan más clariadad llamaré: 
        # Función_L a la función definida en la línea
        # Función_D a la función que se está llamando en el diccionario
        for funcion in diccionario: 

            invocacion_a_funcion(funcion,lista) #Se analiza si la Función_D es invocada por la Función_L

            if invocacion_a_funcion(funcion,lista)!=[]:

                diccionario[funcion]['Total Invocaciones']+=invocacion_a_funcion(funcion,lista)[1]
                #Suma el número de veces en que la Función_D es invocada por la Función_L

                diccionario[lista[0]]['Invocada'].append(invocacion_a_funcion(funcion,lista))
                #Escribe el nombre de la Función_D y el número de veces que es invocada por la Función_L

                diccionario[invocacion_a_funcion(funcion,lista)[0]]['Llamada'].append(lista[0])
                #Escribe el nombre de la Función_L que invoca a la Función_D


    return [n,diccionario]


def encabezado(n):
    """[Autor: Daniela Bolivar]
       [Ayuda: Dado un número n se generará una lista donde la primera componente sea 'FUNCIONES' y el resto
       los números del 1 al n]
    """
    encabezado=['FUNCIONES']

    for i in range(n):
        encabezado.append(str(i+1))

    return encabezado


def generacion_fila(n, funcion, diccionario):
    """[Autor: Daniela Bolivar]
       [Ayuda: Dada una función del dccionario se genrará una lista donde
       la primer compnente será el número de la función y su nombre
       el resto de las componentes serán vacías numéros o 'X' según corresponda]
    """
    fila=[]

    for i in range(0,n+1): #Genero un a fila de n+1 componentes todas vacías
        fila.append(' ')

    fila[0]=diccionario[funcion]['Columna'] + ' - '+ funcion #Cambio la primer componente por el número y nombre de la función

    for j in range(0,len(diccionario[funcion]['Invoca']),2):
        
        k=diccionario[diccionario[funcion]['Invoca'][j]]['Columna']
        #Obtengo el número del la función que es invocada por la fila

        fila[k]=str(diccionario[funcion]['Invoca'][j+1])
        #En la componente k+1 de la fila escribo el número de invocaciones

    for l in range(len(diccionario[funcion]['Llamada'])):
        
        nombre=diccionario[funcion]['Llamada'][l]
        #Del diccionario obtengo el nombre de la funcion que invoca a la función columna
        m=diccionario[nombre]['Columna']
        #Luego obtengo su número

        fila[m]= 'X'
        #En la componente m+1 de la fila escribo 'X'

    return fila


def total_invocaciones( diccionario):
    """[Autor: Daniela Bolivar]
       [Ayuda: Se generará una lista donde la primera componente sea 'Total Invocaciones' y el resto los números
       correspondientes a las invocaciones de las funciones.
       Si la función no tiene invocaciones se escribirá un ' ']
    """

    total=['Total Invocaciones']

    for funcion in diccionario:

        if diccionario[funcion]['Total Invocaciones'] !=0:

            total.append(str(diccionario[funcion]['Total Invocaciones']))

        else:
            total.append(' ')

    return total


def longitud_primera_columna(diccionario):
    """[Autor: Daniela Bolivar]
       [Ayuda: Dada la frase 'Total de Invocaciones' comparo su longitud con la correspondiente a el número de la
        función más los nombres de las funciones del archivo.
       La función devuelve el máximo número que se obtiene de estas comparaciones]
    """
    n=len('Total Invocaciones')

    for funcion in diccionario:

        if n<len(diccionario[funcion]['Columna'] + ' - '+ funcion):
            n=len(diccionario[funcion]['Columna'] + ' - '+ funcion)

    return n



def creacion_tabla(fuente_unico):
    """[Autor: Daniela Bolivar]
       [Ayuda: Dado un archivo creo una lista de listas con la información analizada por las anteriores funciones]
    """

    diccionario_funciones=analisis_codigo_funciones(fuente_unico)

    k=longitud_primera_columna(diccionario_funciones[1])

    tabla=encabezado(diccionario_funciones[0])
    tabla[0]=tabla[0]+ ' '*(k+3-len(tabla[0]))

    for funcion in diccionario_funciones[1]:
        lista=generacion_fila(diccionario_funciones[0], funcion, diccionario_funciones[1])
        lista[0]=lista[0]+ ' '*(k+3-len(lista[0]))
        tabla.append(lista)

    totales=total_invocaciones(diccionario_funciones[1])
    totales[0]=totales[0]+ ' '*(k+3-len(totales[0]))
    tabla.append(totales)

            
    return tabla


def imprimir(archivo,fuente_unico):
    """[Autor: Daniela Bolivar]
       [Ayuda: Dado un archivo se escribre sobre este una tabla. La cual también se imprime por pantalla]
    """
    tabla= creacion_tabla(fuente_unico)

    for lista in tabla:
        fila=' | '.join(lista)

        print(fila, '|')
        archivo.write(fila, '|')

        print('-'*(len(fila)+2))
        archivo.write(fila, '|')
    
    return



def generar_analizador():
    """[Autor: Daniela Bolivar]
       [Ayuda: Esta función abre los archivos correspondientes, crea el archivo pedido e imprime la información]
    """

    fuente_unico= open('fuente_unico.csv','r' )

    analizador=open('analizador.txt', 'w')

    imprimir(analizador,fuente_unico)

    fuente_unico.close()

    analizador.close()


    return

generar_analizador()
