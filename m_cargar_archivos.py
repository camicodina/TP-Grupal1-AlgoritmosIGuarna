#INDICES DEL DICCIONARIO DE ARCHIVOS INTERMEDIOS
INDICE_PARAMENTROS = 0
INDICE_NOMBRE_MODULO = 1
INDICE_AUTOR = 2
INDICE_AYUDA = 3
INDICE_LINEAS_COMENTARIOS = 4
INDICE_LINEAS_CODIGO = 5

#INDICES DE LA FUNCION MENOR ELEGIDA PARA GRABAR
INDICE_NOMBRE_FUNCION_MENOR = 0
INDICE_PARAMENTROS_FUNCION_MENOR = 1
INDICE_NOMBRE_MODULO_FUNCION_MENOR = 2
INDICE_AUTOR_FUNCION_MENOR = 3
INDICE_AYUDA_FUNCION_MENOR = 4
INDICE_LINEAS_COMENTARIOS_FUNCION_MENOR = 5
INDICE_LINEAS_CODIGO_FUNCION_MENOR = 6


def leer_linea_txt(archivo):
    '''[Autor:Andres Guerrero]
       [Ayuda:lee linea del archivo que contiene las rutas] 
    '''
    linea = archivo.readline()
    #Devuelve 1 string si la linea no tiene nada vacios
    return linea if linea else ('') 
    
def calculo_nombre_modulo(ruta_modulo):
    '''[Autor:Andres Guerrero]
       [Ayuda: extraccion del nombre del modulo con el que se esta trabajando] 
    '''
    division_ruta = ruta_modulo.split('\\')
    tamano_division_ruta = len(division_ruta)-1
    nombre_modulo = division_ruta[tamano_division_ruta].rstrip('.py')

    return nombre_modulo

def validacion_inicio_funcion(linea_modulo):
    '''[Autor:Andres Guerrero]
       [Ayuda:valida si la funcion a iniciado para abrir el ciclo] 
    ''' 
    return linea_modulo.startswith('def ')

def validacion_final_funcion(validacion_final,linea_modulo):
    '''[Autor:Andres Guerrero]
       [Ayuda:busca si a finalizado la funcion para darle cierre al ciclo] 
    '''
    validacion_final = True

    if linea_modulo.startswith('    return'):
        validacion_final = False
    elif linea_modulo[0:4] != '    ' and linea_modulo != '\n' and not linea_modulo.startswith('def '): 
        validacion_final = False              
    elif linea_modulo.startswith('def '):
        validacion_final = False
        
    return validacion_final

def calculo_nombre_parametros_funcion(linea_modulo):
    '''[Autor:Andres Guerrero]
       [Ayuda:extrae de la primera linea de funcion su nombre y parametros] 
    '''
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
    '''[Autor:Andres Guerrero]
       [Ayuda:abre una nueva clave para cada funcion que se va encontrando en el codigo
       y lo guarda en un diccionario] 
    '''
    autor = ''
    ayuda = ''
    comentario_simple = ''
    lineas_funcion = ''
    nombre_funcion,parametros = calculo_nombre_parametros_funcion(linea_modulo)

    if nombre_funcion != '':
        funciones[nombre_funcion] = [parametros,nombre_modulo,autor,ayuda,comentario_simple,lineas_funcion]

    return nombre_funcion
        
def extraccion_corchetes(linea_comentario,archivo_modulo): 
    '''[Autor:Andres Guerrero]
       [Ayuda:extrae lo que este entre corchetes sea el autor o ayuda] 
    '''
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
    '''[Autor:Andres Guerrero]
       [Ayuda:diferencia si es un comentario multiple y ahi elige si es un autor,
       ayuda o linea simple y guarda en el diccionario, con su clave respectiva] 
    '''
    comentario_multiple1 = "'''" 
    comentario_multiple2 = '"""'
    linea_comentario = linea_modulo

    if comentario_multiple1 in linea_comentario or comentario_multiple2 in linea_comentario:
        comentario_multiple_cierre = True
        while comentario_multiple_cierre:
            if '[Autor:' in linea_comentario:
                autor,linea_comentario = extraccion_corchetes(linea_comentario,archivo_modulo) 
                funciones[nombre_funcion][INDICE_AUTOR] = autor
            elif '[Ayuda:' in linea_comentario:
                ayuda,linea_comentario = extraccion_corchetes(linea_comentario,archivo_modulo)
                funciones[nombre_funcion][INDICE_AYUDA] = ayuda
            elif not linea_comentario:
                separador_linea = linea_comentario + '$'
                funciones[nombre_funcion][INDICE_LINEAS_COMENTARIOS] += separador_linea
           
            if comentario_multiple1 in linea_comentario or comentario_multiple2 in linea_comentario:  #Si encuentra el segundo """ se sale del ciclo
                comentario_multiple_cierre = False
    return funciones

def lineas_restantes(funciones,linea_modulo,nombre_funcion):
    '''[Autor:Andres Guerrero]
       [Ayuda:guarda una linea que no este en comentario multiple, es decir del codigo y
       selecciona la parte del comentario simple y la de codigo] 
    '''
    comentario_multiple1 = "'''" 
    comentario_multiple2 = '"""'
    nueva_linea = linea_modulo.replace('\n','')
    linea_codigo_vacia = linea_modulo.replace('\n','').strip(' ')
    
    if '#' in nueva_linea:
        pos = nueva_linea.find('#')
        linea_comentario_simple_cambio = nueva_linea[pos:]
        linea_comentario_simple = nueva_linea[pos:] + '$'
        linea_codigo = nueva_linea.replace(linea_comentario_simple_cambio,'').lstrip(' ') + '$'
        funciones[nombre_funcion][INDICE_LINEAS_COMENTARIOS] += linea_comentario_simple
        if linea_codigo != '$':
            funciones[nombre_funcion][INDICE_LINEAS_CODIGO] += linea_codigo

    elif not comentario_multiple1 in nueva_linea or not comentario_multiple2 in nueva_linea and linea_codigo_vacia and not nueva_linea.startswith('def ') and nueva_linea.startswith('    '):
        linea_codigo = nueva_linea.lstrip(' ') + '$'
        funciones[nombre_funcion][INDICE_LINEAS_CODIGO] += linea_codigo
    return funciones


def ordenar_grabar_funciones(funciones,nombre_modulo,archivo_modulo,archivo_ruta_funciones):
    '''[Autor:Andres Guerrero]
       [Ayuda:ordena y guarda en un archivo intermedio lo relativo a la funcion] 
    '''
    lista_modulo_ordenada = sorted(funciones.items(), key = lambda tupla : tupla[0] , reverse=False)
    fh_modulo = open('m_' + nombre_modulo + '.csv','w')
    archivo_ruta_funciones.write('m_' + nombre_modulo + '.csv' + '\n')
    
    for nombre_funcion,campos in lista_modulo_ordenada:
        parametros = campos[INDICE_PARAMENTROS]
        nombre_modulo = campos[INDICE_NOMBRE_MODULO]
        autor = campos[INDICE_AUTOR]
        ayuda = campos[INDICE_AYUDA]
        comentario = campos[INDICE_LINEAS_COMENTARIOS]
        lineas_codigo = campos[INDICE_LINEAS_CODIGO].rstrip('$')
        fh_modulo.write(nombre_funcion + ',&' + parametros + ',&' + nombre_modulo + ',&' + autor + ',&' + ayuda + ',&' + comentario + ',&' + lineas_codigo + '\n')

    fh_modulo.close()
    archivo_modulo.close()

def calculo_funcion(linea_modulo,funciones,nombre_modulo,archivo_modulo):
    while linea_modulo != '':
        validacion_inicio = validacion_inicio_funcion(linea_modulo)
        validacion_final = True
        while validacion_inicio and validacion_final:
 
            if linea_modulo.startswith('def '):
                nombre_guardado = crear_funcion(linea_modulo,funciones,nombre_modulo)

            funciones = calculo_comentario_multiples(linea_modulo,funciones,nombre_guardado,archivo_modulo)
            funciones = lineas_restantes(funciones,linea_modulo,nombre_guardado)  
            linea_modulo = leer_linea_txt(archivo_modulo)

            validacion_final = validacion_final_funcion(validacion_final,linea_modulo)
            if not validacion_final:       
                lineas_restantes(funciones,linea_modulo,nombre_guardado)

        #salida de la funcion que se esta analizando
        if not linea_modulo.startswith('def '):
            linea_modulo = leer_linea_txt(archivo_modulo)
    
    return funciones


def funciones_por_modulo():
    '''[Autor:Andres Guerrero]
       [Ayuda:estructura que se encarga de cargar y hacer los cortes por rutas de los modulos,
       modulo en el que se trabaja,funcion_analizada] 
    '''
    archivo_fuente = open(r'.\programa_prueba\programas.txt','r')
    ruta_modulo = leer_linea_txt(archivo_fuente).rstrip('\n')
    archivo_ruta_funciones = open('archivo_rutas_funciones.txt','w')

    while ruta_modulo != '':  
        nombre_modulo = calculo_nombre_modulo(ruta_modulo)
        archivo_modulo = open(ruta_modulo,'r')
        linea_modulo = leer_linea_txt(archivo_modulo)
        funciones = {}
        funciones = calculo_funcion(linea_modulo,funciones,nombre_modulo,archivo_modulo) 
        #salida del modulo_n que se esta analizando
        ordenar_grabar_funciones(funciones,nombre_modulo,archivo_modulo,archivo_ruta_funciones)
        ruta_modulo = leer_linea_txt(archivo_fuente).rstrip('\n')

    #cerrado del archivo que contiene las rutas de los archivos intermedios
    archivo_ruta_funciones.close()
    archivo_fuente.close()


def apertura_archivos():
    '''[Autor:Andres Guerrero]
       [Ayuda:abre los archivos guardados en un txt con las ruta de los archivos intermedios] 
    '''

    ruta_modulos_ordenados = open('archivo_rutas_funciones.txt','r')
    lista_archivos = []

    for linea in  ruta_modulos_ordenados:
        ruta_modulo = linea.rstrip('\n')
        archivo = open(ruta_modulo,'r')
        lista_archivos.append(archivo)

    return lista_archivos

def cerrado_archivos(lista_archivos):
    '''[Autor:Andres Guerrero]
       [Ayuda:cierra los archivos intermedios] 
    '''
    for archivos in lista_archivos:
        archivos.close()


def leer_linea_mezcla(archivo, default):
    '''[Autor:Andres Guerrero]
       [Ayuda:lee una linea de los archivos que se esta mezclando] 
    '''
    linea = archivo.readline()
    return linea.rstrip('\n').split(',&') if linea else default


def leer_lineas_archivos(lista_archivos,default):
    '''[Autor:Andres Guerrero]
       [Ayuda:lee las lineas de cada uno de los archivos] 
    '''

    lista_lineas = []

    for archivo in lista_archivos:
        linea  = leer_linea_mezcla(archivo,default)
        lista_lineas.append(linea)

    return lista_lineas

def validar_fin_lineas(lista_lineas,Fin):
    '''[Autor:Andres Guerrero]
       [Ayuda:adentro de la parte de mezcla anliza cual de las lineas a llegado al fin] 
    '''

    cont_fin = 0 # cantidad de archivos que llegaron al fin

    for linea in lista_lineas:
        if linea[0] == Fin:
            cont_fin+=1

    cant_archivos = len(lista_lineas)

    return cont_fin != cant_archivos


def escritura_archivos(nombre_menor,a_comentario,fuente_unico):
    '''[Autor:Andres Guerrero]
       [Ayuda:al conseguir la funcion que es la menor entre todas graba los campos en 
       comentarios.csv y fuente_unico.csv] 
    '''

    nombre_funcion = nombre_menor[INDICE_NOMBRE_FUNCION_MENOR]
    parametros = nombre_menor[INDICE_PARAMENTROS_FUNCION_MENOR]
    modulo = nombre_menor[INDICE_NOMBRE_MODULO_FUNCION_MENOR]
    relativo_funcion = nombre_menor[INDICE_LINEAS_CODIGO_FUNCION_MENOR]
    relativo_funcion_separado = relativo_funcion.split('$')
    separacion_relativo = ''

    for relativo in relativo_funcion_separado:
        agregado = ',' + relativo 
        separacion_relativo += agregado
    fuente_unico.write(nombre_funcion  + ',' +  parametros  + ',' + modulo  + separacion_relativo + '\n')

    autor = nombre_menor[INDICE_AUTOR_FUNCION_MENOR]
    ayuda = nombre_menor[INDICE_AYUDA_FUNCION_MENOR]
    comentarios_unicos = nombre_menor[INDICE_LINEAS_COMENTARIOS_FUNCION_MENOR]
    comentarios_unicos_separados = comentarios_unicos.split('$')
    separacion_cometario = ''

    for comentario in comentarios_unicos_separados:
        agregado = ',' + comentario
        separacion_cometario += agregado
    a_comentario.write(nombre_funcion + ',' + autor + ',' + ayuda + separacion_cometario + '\n')


def calculo_nueva_lista_linea(lista_lineas,nombre_menor,default,lista_archivos):
    '''[Autor:Andres Guerrero]
       [Ayuda:ve cual linea fue usada y se trae una nueva linea de ese archivo para 
       actualizar las lineas a analizar de cada archivo] 
    '''
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
    '''[Autor:Andres Guerrero]
       [Ayuda: realiza un ciclo que busca el minimo entre los n archivos y graba comentario.csv 
       y fuente_unico.csv] 
    '''
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
    '''[Autor:Andres Guerrero]
       [Ayuda: estructura main de la mezcla] 
    '''
    lista_archivos = apertura_archivos()
    mezcla(lista_archivos)
    cerrado_archivos(lista_archivos)

def cargar_archivo():
    '''[Autor:Andres Guerrero]
       [Ayuda:estructura main del modulo] 
    '''
    funciones_por_modulo()
    mezcla_archivos_intermedios()


cargar_archivo()

#buscar nombres buenos ,recortar codigo con devolucion de expresiones
#preguntar lo que no entendi