def nombre_autores(nombre):
    """[Autor: Daniela Bolivar]
       [Ayuda: Dado un sting lo corta, para obtener el nombre.]
    """
    x=nombre.find(':')+2
    autor=nombre[x:-1]

    return autor

def diccionario_autores_funciones(comentarios):
    """[Autor: Daniela Bolivar]
       [Ayuda: Crea un diccionario con los autores de cada función. A la vez crea un subdiccionario 
       con las funciones creadas por el autor, y características vacías de cada función.
       A las funciones que no tengan un autor cargado, se le asignará el autor 'Anónimo' ]
    """

    diccionario_autores={}

    for linea in comentarios:

        lista=linea.rstrip('\n').split(',')

        if lista[1]=='':
            autor='Anónimo'

        else:     
            autor= nombre_autores(lista[1])

        if autor not in diccionario_autores:
            
            diccionario_autores[autor]={'Función':[lista[0]], 'Líneas':[],'Cantidad Funciones':0, 'Líneas Totales':0, 'Porcentaje':0}

        else:
            diccionario_autores[autor]['Función'].append(lista[0])

    
    return diccionario_autores




def encuentro_funcion_autor(funcion, diccionario):
    """[Autor: Daniela Bolivar]
       [Ayuda: Dada una lista y el diccionario creado en 'diccionario_autores_funciones(comentarios)' se busca
       a qué autor pertenece la lista ingresada]
    """
    
    autor=''
    for nombre in diccionario:
        if funcion in diccionario[nombre]['Función']:
            autor=nombre
    
    return autor  

def numero_parametros_codigo(lista):
    """[Autor: Daniela Bolivar]
       [Ayuda: Esta función se utilizará para contar los parámetros de una función]
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
        
    return n   

def numero_lineas_codigo(n,lista):
    """[Autor: Daniela Bolivar]
       [Ayuda: Esta función se utilizará para contar las líneas de código de una función]
    """
    inico_p= False
    c_abierto=0
    c_cerrado=0
    k=0
    
    for i in lista[n+2:]:
        c_abierto+=i.count('(')
          
        c_cerrado+=i.count(')') 

        if c_abierto>c_cerrado :
            inico_p= True

        if c_abierto==c_cerrado:
            inico_p= False
            

        if inico_p :
            
            k+=1
                    
    
    if n==0:
        k= len(lista[2:])-(k+1)
        
    else:
        k=len(lista[n+2:])-k
        

    return k 


def analisis_cantidad_lineas(fuente_unico, comentarios):
    """[Autor: Daniela Bolivar]
       [Ayuda: dado el archivo funte_unico.csv se analizará el código de cada una de las funciones en el archivo.
       El resultado del análisis quedará cargado en un diccionario]
    """
    #Genero el diccionario a partir del arcivo comentarios.csv
    comentarios= open('comentarios.csv','r' )
    diccionario_autores= diccionario_autores_funciones(comentarios) 


    n=0 #Esta variable servirá para contar las líneas totales del código
    
    #Recorro línea por línea el archivo fuente_unico
    fuente_unico= open('fuente_unico.csv','r' )

    for linea in fuente_unico:
        #transfomo la línea a analizar en una lista
        lista=linea.rstrip('\n').split(',') 

        #Completo el diccionario
        autor = encuentro_funcion_autor(lista[0], diccionario_autores)

        diccionario_autores[autor]['Líneas'].append(numero_lineas_codigo(numero_parametros_codigo(lista),lista))

        diccionario_autores[autor]['Líneas Totales']+= numero_lineas_codigo(numero_parametros_codigo(lista),lista)

        n+=numero_lineas_codigo(numero_parametros_codigo(lista),lista)
    
    for autor in diccionario_autores:
        diccionario_autores[autor]['Porcentaje']= diccionario_autores[autor]['Líneas Totales']/n
        diccionario_autores[autor]['Cantidad Funciones']= len(diccionario_autores[autor]['Función'])


    return diccionario_autores

def lista_autores(diccionario):
    """[Autor: Daniela Bolivar]
       [Ayuda: Dado un diccionario se obtendrá una lista ordenada de mayor a menor según el procentaje]
    """
    autores_ordenados=[]
    lista=sorted(diccionario.items(), key=lambda x: x[1]['Porcentaje'], reverse=True)

    for autor in lista:
        autores_ordenados.append(autor[0])
    
    return autores_ordenados


def longitud_de_funciones(diccionario):
    """[Autor: Daniela Bolivar]
       [Ayuda: Dada la frase '10 Funciones - Lineas ', comparo su longitud con la correspondiente a los nombres de
       las funciones del archivo.
       La función devuelve el máximo número que se obtiene de estas comparaciones]
    """
    #Escribo 10 porque con esto tengo en cuenta de que el número de funciones del autor se puede encontrar en las dos cifras
    n=len('10 Funciones - Lineas ') 

    for nombre in diccionario:

        for i in range(0, len(diccionario[nombre]['Función'])):

            if n<len(diccionario[nombre]['Función'][i]):
                n=len(diccionario[nombre]['Función'][i])

    return n


def creacion_informe(archivo,fuente_unico, comentarios):
    """[Autor: Daniela Bolivar]
       [Ayuda: Dados los archivos fuente_unico.csv y comentarios.csv se escribe sobre un "archivo" e imprime por
       pantalla la información requerida]
    """
    fuente_unico= open('fuente_unico.csv','r' )
     
    comentarios= open('comentarios.csv','r' )
    diccionario_autores=analisis_cantidad_lineas(fuente_unico, comentarios)


    autores_ordenados=lista_autores(diccionario_autores)

    n=longitud_de_funciones(diccionario_autores)+2

    m=n+16

    f_total=0

    l_total=0

    print(' '*4,'Informe de Desarrollo por Autor')

    archivo.write(' '*4 +'Informe de Desarrollo por Autor'+'\n')

    for autor in autores_ordenados:
        

        print('\n','Autor: '+ autor,'\n')
        archivo.write('\n'+'\n'+'Autor: '+ autor +'\n'+'\n')

        print(' '*7,'Funcion',' '*(n-len('Funcion')),'Líneas' )
        archivo.write(' '*7 + 'Funcion'+ ' '*(n-len('Funcion')) +'Líneas' )

        print(' '*7,'-'*m )
        archivo.write('\n'+' '*7 + '-'*m +'\n')

        for i in range(0,len(diccionario_autores[autor]['Función'])):

            print(' '*7,diccionario_autores[autor]['Función'][i],' '*(n-len(diccionario_autores[autor]['Función'][i])),' '*(4-len(str(diccionario_autores[autor]['Líneas'][i]))),diccionario_autores[autor]['Líneas'][i])
            archivo.write(' '*7 + str(diccionario_autores[autor]['Función'][i]) +' '*(n-len(diccionario_autores[autor]['Función'][i]))+ ' '*(4-len(str(diccionario_autores[autor]['Líneas'][i]))) + str(diccionario_autores[autor]['Líneas'][i])+'\n')
    
        print(' '*7,diccionario_autores[autor]['Cantidad Funciones'],' Funciones - Lineas',' '*(n-(len(' Funciones - Lineas')+len(str(diccionario_autores[autor]['Cantidad Funciones'])))),' '*(3-len(str(diccionario_autores[autor]['Líneas Totales']))),diccionario_autores[autor]['Líneas Totales'], ' ', '{:.2%}'.format(diccionario_autores[autor]['Porcentaje']), '\n')
        archivo.write(' '*7 + str(diccionario_autores[autor]['Cantidad Funciones']) + ' Funciones - Lineas'+ ' '*(n-(len(' Funciones - Lineas') + len(str(diccionario_autores[autor]['Cantidad Funciones'])))) + ' '*(4-len(str(diccionario_autores[autor]['Líneas Totales']))) + str(diccionario_autores[autor]['Líneas Totales']) + '     ' + '{:.2%}'.format(diccionario_autores[autor]['Porcentaje']) + '\n')

        f_total+=diccionario_autores[autor]['Cantidad Funciones']
        l_total+=diccionario_autores[autor]['Líneas Totales']
    
    print('\n'+'Total: ', str(f_total) , 'Funciones - Lineas' , ' '*(n-(len('Funciones -Lineas')+len(str(diccionario_autores[autor]['Cantidad Funciones'])))) , l_total)
    archivo.write('\n'+'Total: '+ str(f_total) + ' Funciones - Lineas' + ' '*(n-(len('Funciones - Lineas')+len(str(diccionario_autores[autor]['Cantidad Funciones'])))) + str(l_total))

    return


def generacion_participacion():
    """[Autor: Daniela Bolivar]
       [Ayuda: Esta función abre los archivos correspondientes, crea el archivo pedido e imprime la información]
    """
    fuente_unico= open('fuente_unico.csv','r' )
     
    comentarios= open('comentarios.csv','r' )

    participacion= open('participacion.txt','w')

    creacion_informe(participacion, fuente_unico, comentarios)


    fuente_unico.close()

    comentarios.close()

    participacion.close()

    return


        






