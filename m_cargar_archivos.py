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

def validacion_funcion_final(validacion_final,linea_modulo,archivo_modulo,nombre_funcion):
    validacion_final = True

    if linea_modulo.startswith('    return'):
        validacion_final = False

    if linea_modulo[0:4] != '    ': 
        if linea_modulo != '\n':
            if not linea_modulo.startswith('def ') :
                validacion_final = False
                
    if linea_modulo.startswith('def '):
                    validacion_final = False
        
    return validacion_final

def calculo_nombre_parametros_funcion(linea_modulo):
    nombre_funcion = ''
    parametros = ''
    if linea_modulo.startswith('def '):
        linea = linea_modulo.replace('def ','').replace(':\n','') # quita el def y renplaza  :\n en la linea con un vacio
        inicio_parametros = linea.find('(')
        final_parametros = linea.find(')') + 1
        parametros = linea[inicio_parametros:final_parametros]
        nombre_funcion = linea.replace(parametros,'')

    return nombre_funcion,parametros

def crear_funcion(linea_modulo,funciones,nombre_modulo):
    autor = ''
    ayuda = ''
    comentario_simple = ''
    lineas_funcion = ''
    nombre_funcion,parametros = calculo_nombre_parametros_funcion(linea_modulo)

    if nombre_funcion != '':
        funciones[nombre_funcion] = [parametros,nombre_modulo,autor,ayuda,comentario_simple,lineas_funcion]

    return nombre_funcion
        
def extraccion_corchetes(linea_comentario,archivo_modulo): # extrae lo que este entre corchetes sea el autor o ayuda
    extraccion = ''
    pos = linea_comentario.find('[') # posicion del primer corchete
    linea_nueva = linea_comentario[pos:].replace('\n',' ') # le quito el salto de linea a la linea de comentario
    linea_final = True
    pos = 0
    letra = linea_nueva[0] # la letra esta inicializada en el primer corchete
    while linea_final:
        tamano = len(linea_nueva) - 1 
        extraccion += letra
        if letra == ']' or not pos < tamano:
            if letra == ']':
                linea_final = False
                linea_nueva = leer_linea_txt(archivo_modulo).replace('\n',' ')
            elif not pos < tamano:
                linea_nueva = ' ' + leer_linea_txt(archivo_modulo).replace('\n',' ').lstrip(' ')
                pos = 0
                letra = linea_nueva[0]
        else:
            pos +=1
            letra = linea_nueva[pos] 

    linea_nueva = linea_nueva.rstrip(' ')
    return extraccion,linea_nueva
    
def calculo_comentario_multiples(linea_modulo,funciones,nombre_funcion,archivo_modulo):
    c_multiple = '"""' 
    linea_comentario = linea_modulo

    if c_multiple in linea_comentario:
        c_multiple_cierre = True
        while c_multiple_cierre:
            if '[Autor:' in linea_comentario:
                autor,linea_comentario = extraccion_corchetes(linea_comentario,archivo_modulo) 
                funciones[nombre_funcion][2] = autor
            elif '[Ayuda:' in linea_comentario:
                ayuda,linea_comentario = extraccion_corchetes(linea_comentario,archivo_modulo)
                funciones[nombre_funcion][3] = ayuda
            elif not linea_comentario:
                separador_linea = linea_comentario + '$'
                funciones[nombre_funcion][4] += separador_linea
           
            if c_multiple in linea_comentario:  #Si encuentra el segundo """ se sale del ciclo
                c_multiple_cierre = False

def lineas_restantes(funciones,linea_modulo,nombre_funcion):
    nueva_linea = linea_modulo.replace('\n','')
    linea_codigo_vacia = linea_modulo.replace('\n','').strip(' ')
    
    if '#' in nueva_linea:
        pos = nueva_linea.find('#')
        linea_comentario_simple_cambio = nueva_linea[pos:]
        linea_comentario_simple = nueva_linea[pos:] + '$'
        linea_codigo = nueva_linea.replace(linea_comentario_simple_cambio,'').lstrip(' ') + '$'
        funciones[nombre_funcion][4] += linea_comentario_simple
        if linea_codigo != '$':
            funciones[nombre_funcion][5] += linea_codigo

    elif not '"""' in nueva_linea and linea_codigo_vacia and not nueva_linea.startswith('def '):
        linea_codigo = nueva_linea.lstrip(' ') + '$'
        funciones[nombre_funcion][5] += linea_codigo

def ordenar_grabar_funciones(funciones,nombre_modulo,archivo_modulo,archivo_ruta_funciones):
    lista_modulo_ordenada = sorted(funciones.items(), key = lambda tupla : tupla[0] , reverse=False)
    fh_modulo = open('m_' + nombre_modulo + '.csv','w')
    archivo_ruta_funciones.write('m_' + nombre_modulo + '.csv' + '\n')
    
    for nombre_funcion,campos in lista_modulo_ordenada:
        parametros = campos[0]
        autor = campos[2]
        ayuda = campos[3]
        comentario = campos[4]
        lineas_codigo = campos[5].rstrip('$')
        fh_modulo.write(nombre_funcion + ',&' + parametros + ',&' + nombre_modulo + ',&' + autor + ',&' + ayuda + ',&' + comentario + ',&' + lineas_codigo + '\n')

    fh_modulo.close()
    archivo_modulo.close()

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
            while validacion_inicio and validacion_final:
                #inicializa el diccionario con el nombre de la funcion actual
                nombre_funcion = crear_funcion(linea_modulo,funciones,nombre_modulo,)

                if nombre_funcion != '': #guarda el nombre de la funcion que se esta guardando en el dic
                    nombre_guardado = nombre_funcion
                calculo_comentario_multiples(linea_modulo,funciones,nombre_guardado,archivo_modulo) #guarda comentarios multiples / separa autor y ayuda
                lineas_restantes(funciones,linea_modulo,nombre_guardado) # divide entre comentario simple y resto de funcion
                linea_modulo = leer_linea_txt(archivo_modulo)

                validacion_final = validacion_funcion_final(validacion_final,linea_modulo,archivo_modulo,nombre_funcion)
                
            #salida de la funcion que se esta analizando
            if not linea_modulo.startswith('def '):
                linea_modulo = leer_linea_txt(archivo_modulo)
        #salida del modulo_n que se esta analizando
        ordenar_grabar_funciones(funciones,nombre_modulo,archivo_modulo,archivo_ruta_funciones)#toma el diccionario de el modulo_n y lo ordena creando un archivo intermedio
        ruta_modulo = leer_linea_txt(archivo_fuente).rstrip('\n')
    #cerrado del archivo que contiene las rutas de los archivos intermedios
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
    fuente_unico.write(nombre_funcion  + ',' +  parametros  + ',' + modulo  + separacion_relativo + '\n')

    autor = nombre_menor[3]
    ayuda = nombre_menor[4]
    comentarios_unicos = nombre_menor[5]
    comentarios_unicos_separados = comentarios_unicos.split('$')
    separacion_cometario = ''

    for comentario in comentarios_unicos_separados:
        agregado = ',' + comentario
        separacion_cometario += agregado
    a_comentario.write(nombre_funcion + ',' + autor + ',' + ayuda + separacion_cometario + '\n')


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






# Numero de Legajo ---------105692-----------