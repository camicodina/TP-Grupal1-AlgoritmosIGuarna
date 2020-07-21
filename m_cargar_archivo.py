
def solicitar_archivo():
    #ruta_archivo_fuente = input('solicitar la ruta del archivo:')
    archivo_fuente = open(r'.\programa_prueba\programas.txt','r')

    return archivo_fuente

def leer_linea_txt(archivo):
    linea = archivo.readline()
    #Devuelve 1 string si la linea no tiene nada vacios
    return linea if linea else ('') 
    
def calculo_nombre_modulo(ruta_modulo):
    division_ruta = ruta_modulo.split('\\')
    tamano_division_ruta = len(division_ruta)-1
    nombre_modulo = division_ruta[tamano_division_ruta].rstrip('.py')

    return nombre_modulo

def validacion_funcion_inicial(linea_modulo):
    validacion_inicio = False
    if linea_modulo.startswith('def '):
        validacion_inicio = True 
    
    return validacion_inicio

def validacion_funcion_final(validacion_final,linea_modulo,archivo_modulo):

    validacion1 =  linea_modulo.startswith('    return')
    if linea_modulo.startswith('def '):
        validacion2 = False
    elif linea_modulo[0:4] != '    ' :
        validacion2 = True
    else:
        validacion2 = False
    if validacion1 or validacion2:
        validacion_final = False
    return validacion_final

def calculo_nombre_funcion(linea_modulo):
    nombre_funcion = ''
    parametros = ''
    if linea_modulo.startswith('def '):
        linea_sin_def = linea_modulo.replace('def ','')
        linea_sin_def_dospuntos = linea_sin_def.replace(':\n','')
        i = 0

        while linea_sin_def_dospuntos[i] != '(':
            nombre_funcion += linea_sin_def_dospuntos[i]
            i+=1    

        parametros = linea_sin_def_dospuntos.lstrip(nombre_funcion)

    return nombre_funcion,parametros


def carga_diccionario(linea_modulo,funciones,nombre_modulo,comentario_m):
        
    nombre_funcion,parametros = calculo_nombre_funcion(linea_modulo)
    if nombre_funcion != '':
        if not nombre_funcion in funciones:
            autor = ''
            ayuda = ''
            comentario_simple = ''
            lineas_funcion = ''
            funciones[nombre_funcion] = [parametros,nombre_modulo,autor,ayuda,comentario_simple,lineas_funcion]

    return nombre_funcion
        

def calculo_comentarios(linea_modulo,funciones,comentario_m,nombre_d):
    c_multiple = '"""' 
    comentario_simple = ''
    autor = ''
    ayuda = ''

    if c_multiple in linea_modulo:
        comentario_m +=1

    if not comentario_m %2 == 0 :
        if linea_modulo.startswith('    """[Autor:'):
            posicion = linea_modulo.find('[')
            while linea_modulo[posicion] != ']' :
                autor += linea_modulo[posicion]
                posicion +=1
            autor = autor + ']'
            funciones[nombre_d][2] = autor

        if linea_modulo.startswith('       [Ayuda:'):
            nueva_linea = linea_modulo.replace('\n','').lstrip(' ')
            ayuda += nueva_linea + ' '
            funciones[nombre_d][3] += ayuda
        elif linea_modulo.endswith(']\n') and not linea_modulo.startswith('    """[Autor:'):
            nueva_linea = linea_modulo.replace('\n','').rstrip(' ').lstrip(' ')
            ayuda += nueva_linea + ' '
            funciones[nombre_d][3] = ayuda
            
    if '#' in linea_modulo:
        posicion = linea_modulo.find('#')
        while posicion < len(linea_modulo):
            comentario_simple += linea_modulo[posicion]
            posicion +=1
        comentario_simple = comentario_simple.replace('\n','') + '$'
        funciones[nombre_d][4] += comentario_simple

    if comentario_m %2 == 0:
        if '#' in linea_modulo:
            posicion = linea_modulo.find('#')
            nueva_linea = linea_modulo[0:posicion].rstrip('\n').lstrip(' ') + '$'
        elif '"""' in linea_modulo:
            nueva_linea = ''
        else:
            nueva_linea = linea_modulo.rstrip('\n').lstrip(' ') + '$'

        funciones[nombre_d][5] += nueva_linea

    return comentario_m             

def funciones_por_modulo(archivo_fuente):
    #retorna una lista ordenado alfabeticamente por funciones
    ruta_modulo = leer_linea_txt(archivo_fuente).rstrip('\n')
    archivo_ruta_funciones = open('archivo_rutas_funciones.txt','w')
    while ruta_modulo != '':
    
        nombre_modulo = calculo_nombre_modulo(ruta_modulo)
        
        archivo_modulo = open(ruta_modulo,'r')

        
        linea_modulo = leer_linea_txt(archivo_modulo)
        funciones = {}

        while linea_modulo != '': 
            validacion_inicio = validacion_funcion_inicial(linea_modulo)
            validacion_final = True
            comentario_m = 0
            while linea_modulo != '' and validacion_inicio and validacion_final:

                nombre = carga_diccionario(linea_modulo,funciones,nombre_modulo,comentario_m)
                if nombre != '':
                    nombre_d = nombre
                
                comentario_m = calculo_comentarios(linea_modulo,funciones,comentario_m,nombre_d)

                validacion_final = validacion_funcion_final(validacion_final,linea_modulo,archivo_modulo)
                if validacion_final:
                    linea_modulo = leer_linea_txt(archivo_modulo)

            linea_modulo = leer_linea_txt(archivo_modulo)
            
        lista_modulo_ordenada = sorted(funciones.items(), key = lambda tupla : tupla[0] , reverse=False)
        fh_modulo = open('m_' + nombre_modulo + '.csv','w')
        archivo_ruta_funciones.write('m_' + nombre_modulo + '.csv' + '\n')

        for nombre_funcion,parametros in lista_modulo_ordenada:
            fh_modulo.write(nombre_funcion + ',&' + parametros[0] + ',&' + nombre_modulo + ',&' + parametros[2] + ',&' + parametros[3] + ',&' + parametros[4] + ',&' + parametros[5] + '\n')

        fh_modulo.close()
        archivo_modulo.close()
        

        ruta_modulo = leer_linea_txt(archivo_fuente).rstrip('\n')

    archivo_ruta_funciones.close()

def apertura_archivos():

    ruta_modulos_ordenados = open('archivo_rutas_funciones.txt','r')
    lista_archivos = []

    for linea in  ruta_modulos_ordenados:
        ruta_modulo = linea.rstrip('\n')
        archivo = open(ruta_modulo,'r')
        lista_archivos.append(archivo)

    return lista_archivos

def cerrado_archivos(lista_archivos):
    for archivos in lista_archivos:
        archivos.close()

def leer_linea_mezcla(archivo, default):
    linea = archivo.readline()
    return linea.rstrip('\n').split(',&') if linea else default


'''
leer lineas de los archivos
validar que no allan llegado al fin de alguno de los archivos
traerme los nombre de las funciones 
ver cual es el menor 
buscar el indice en lista_lineas_archivo
grabar en comentarios y fuente unico
leer la siguiente linea de ese archivo porque ya tengo el indice
repetir hasta que se acabe
'''

def leer_lineas_archivos(lista_archivos,default):

    lista_lineas = []

    for archivo in lista_archivos:
        linea  = leer_linea_mezcla(archivo,default)
        lista_lineas.append(linea)

    return lista_lineas

def validar_fin_lineas(lista_lineas,Fin):
    
    validar = False
    cont_fin = 0 # cantidad de archivos que llegaron al fin

    for linea in lista_lineas:
        if linea[0] == Fin:
            cont_fin+=1

    cant_archivos = len(lista_lineas)
    if cont_fin != cant_archivos:
        validar = True

    return validar 

def calculo_nombres(lista_lineas):
    lista_nombres = []

    for nombre_funcion in lista_lineas:
        lista_nombres.append(nombre_funcion)

    return lista_nombres

def escritura_archivos(nombre_menor,a_comentario,fuente_unico):

    nombre_funcion = nombre_menor[0]
    parametros = nombre_menor[1]
    modulo = nombre_menor[2]
    relativo_funcion = nombre_menor[6]
    relativo_funcion_separado = relativo_funcion.split('$')
    separacion_relativo = ''

    for relativo in relativo_funcion_separado:
        agregado = ',' + relativo 
        separacion_relativo += agregado
    fuente_unico.write(nombre_funcion  + ',' +  parametros  + ',' + modulo  + ',' + separacion_relativo + '\n')

    autor = nombre_menor[3]
    ayuda = nombre_menor[4]
    comentarios_unicos = nombre_menor[5]
    comentarios_unicos_separados = comentarios_unicos.split('$')
    separacion_cometario = ''

    for comentario in comentarios_unicos_separados:
        agregado = ',' + comentario
        separacion_cometario += agregado
    a_comentario.write(nombre_funcion + ',' + autor + ',' + ayuda + ',' + separacion_cometario + '\n')


def calculo_nueva_lista_linea(lista_lineas,nombre_menor,default,lista_archivos):
    i=0
    nombre_comparativo = lista_lineas[i][0]
    nombre = nombre_menor[0]
    while nombre_comparativo != nombre:
        i+= 1
        nombre_comparativo = lista_lineas[i][0]

    nueva_linea = leer_linea_mezcla(lista_archivos[i],default)
    lista_lineas[i] = nueva_linea

    return lista_lineas


def mezcla(lista_archivos):
    Fin = 'zzzzzz9999'
    default = [Fin,'','','','','','']
    archivo_comentario = open('comentarios.csv','w')
    archivo_fuente_unico = open('fuente_unico.csv','w')

    lista_lineas = leer_lineas_archivos(lista_archivos,default)
    while validar_fin_lineas(lista_lineas,Fin):
        nombre_menor = min(lista_lineas, key =  lambda list : list[0])
        escritura_archivos(nombre_menor,archivo_comentario,archivo_fuente_unico) #escribe los campos para comentarios.csv y fuente unico.csv
        lista_lineas = calculo_nueva_lista_linea(lista_lineas,nombre_menor,default,lista_archivos)# esta es la que falta

    archivo_fuente_unico.close()
    archivo_comentario.close()


def mezcla_archivos_intermedios():
    lista_archivos = apertura_archivos()
    mezcla(lista_archivos)
    cerrado_archivos(lista_archivos)

def cargar_archivo():
    archivo_fuente = solicitar_archivo()
    funciones_por_modulo(archivo_fuente)
    mezcla_archivos_intermedios()


cargar_archivo()






