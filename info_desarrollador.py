
def diccionario_autores_funciones(comentarios):
    """[Autor: Daniela Bolivar]
       [Ayuda: Crea un diccionario con los autores de cada función,
       a la vez crea un subdiccionario con las características vacías de cada función creada]
    """

    diccionario_autores={}
    for linea in comentarios:
        if linea[1] not in diccionario_autores:
            
            diccionario_autores[linea[1]]={'Función':['linea[0]'], 'Líneas':[0],'Cantidad Funciones':0, 'Líneas Totales':0, 'Porcentaje':0}

        else:
            diccionario_autores[linea[1]]['Función'].append('linea[0]')

    
    return diccionario_autores


def encuentro_funcion_autor(lista, diccionario):
    
    autor=''
    for nombre in diccionario:
        if 'lista[0]' in diccionario[nombre]['Función']:
            autor=nombre
    
    return autor


def analisis_cantidad_lineas(fuente_unico, comentarios):
    """[Autor: Daniela Bolivar]
       [Ayuda: dado el archivo funte_unico.csv se analizará el código de cada una de las funciones en el archivo.
       El resultado del análisis quedará cargado en un diccionario]
    """
    #Genero el diccionario
    diccionario_autores= diccionario_autores_funciones(comentarios) 

    n=0
    
    #Recorro línea por línea el csv
    for linea in fuente_unico:
        #transfomo la línea a analizar en una lista
        lista=linea.rstrip('\n').split(',') 

        #Completo el diccionario
        autor = encuentro_funcion_autor(lista, diccionario_autores)

        diccionario_autores[autor]['Líneas'].append(len(lista)-3)

        diccionario_autores[autor]['Líneas Totales']+= len(lista)-3

        n+=len(lista)-3
    
    for autor in diccionario_autores:
        diccionario_autores[autor]['Porcentaje']= round(diccionario_autores[autor]['Líneas Totales']*100/n,2)
        diccionario_autores[autor]['Cantidad Funciones']= len(diccionario_autores[autor]['Función'])

    diccionario_porcentajes=sorted(diccionario_autores.items, key=lambda x: x[autor]['Porcentaje'], reverse=True)


    return diccionario_porcentajes


def longitud_de_funciones(diccionario):
    """[Autor: Daniela Bolivar]
       [Ayuda: Danda una palabra, comparo su longitud con la correspondiente a los elementos que se obtienen
       del diccionario en la clave  ingresados.
       La función devuelve el máximo número que se obtiene de estas comparaciones más dos]
    """
    n=len('10 Funciones - Lineas ')

    for nombre in diccionario:

        for i in range(0, len(diccionario[nombre]['Función'])):

            if n<len(diccionario[nombre]['Función'][i]):
                n=len(diccionario[nombre]['Función'][i])

    return n


def creacion_informe(fuente_unico, comentarios):

    diccionario_autores=analisis_cantidad_lineas(fuente_unico, comentarios)

    n=longitud_de_funciones(diccionario_autores)

    m=n+11


    for autor in diccionario_autores:
        

        print('\n','Autor: '+ autor,'\n')

        print('{:8}{:21}{:^6}'.format(' ', 'Funcion', 'Líneas'))

        print('{:8}{:{fill}{align}{width}}'.format(' ','', fill='-', align='^',width=m))

        for i in range(0,len(diccionario_autores[autor]['Función'])):


            print('{0:8}{1:21}{2:5d}'.format(' ', diccionario_autores[autor]['Función'][i], diccionario_autores[autor]['Líneas'][i]))
    
        print('{:8}{:<2}{:19}{:4d}{:2}{:.2%}'.format(' ', diccionario_autores[autor]['Cantidad Funciones'], ' Funciones - Lineas ', diccionario_autores[autor]['Líneas Totales'],' ', diccionario_autores[autor]['Porcentaje']), '\n') 

    return
################### Bloque Principal ###################


comentarios = open("comentarios.csv")
fuente_unico = open("fuente_unico.csv")
participacion = open("participacion.txt","w")
procesar_archivos(desarrolladores, participacion)
comentarios.close()
participacion.close()
