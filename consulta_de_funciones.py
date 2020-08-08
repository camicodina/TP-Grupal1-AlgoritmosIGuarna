import TableIt

def abrir_fuente_unico():
    """[Autor: Camila Codina]
       [Ayuda: Abre fuente_unico.csv y crea una lista con nombres de funciones (funciones). También, por cada línea leída, agrega elementos a la lista listar_funciones]
    """
    funciones = []
    listar_funciones =[]
    with open('fuente_unico.csv','r') as fuente_unico:
        for linea in fuente_unico:
            funciones.append(linea.rstrip("\n").split(",")[0])
            listar_funciones.append(linea.rstrip('\n'))
    return funciones,listar_funciones


def listar_fuente_unico(funciones,listar_funciones):
    """[Autor: Camila Codina]
       [Ayuda: Crea un diccionario que tomar por clave los nombres de las funciones recibidas y por valor una lista con sus parámetros, el módulo al que pertenece y una lista con el código]
    """
    parametros = []
    modulos = []
    codigos = []
    fuente_unico_funciones={}
    n=0
    i=0
    for funcion in listar_funciones:
        reemplazo_separar = funcion.replace('),', ')//').split('//')
        parametros.append(reemplazo_separar[0].lstrip(funciones[i]).replace(",", ""))
        i+=1
        modulo = reemplazo_separar[1].split(",")[0]
        modulos.append(modulo)
        codigo_funcion = reemplazo_separar[1].lstrip(modulo)
        codigos.append(codigo_funcion.split(","))
    for recibido in funciones:
        fuente_unico_funciones[recibido] = [parametros[n], modulos[n], codigos[n]]
        n+=1
    return fuente_unico_funciones


def abrir_comentarios():
    """[Autor: Camila Codina]
       [Ayuda: Abre comentarios.csv y crea una lista para cada línea leída, organizadas dentro de otra lista (lista_comentarios).]
    """
    lista_comentarios = []
    with open('comentarios.csv','r') as comentarios:
        for linea in comentarios:
            lista_comentarios.append(linea.rstrip("\n").split(","))
    return lista_comentarios


def listar_comentarios(lista_comentarios, funciones):
    """[Autor: Camila Codina]
       [Ayuda: Crea un diccionario que toma por claves los nombres de las funciones recibidas y por valor una lista con el autor y la ayuda.]
    """
    comentarios_funciones = {}
    autores = []
    ayudas = []
    n=0
    for x in lista_comentarios:
        autor = x[1]
        if "[Autor:" in autor:
            autor = autor[8:].rstrip("]")
        autores.append(autor)
        ayuda= ' '.join(x[2:])
        if "[Ayuda:" in ayuda:
            sep = "]"
            ayuda = ayuda.split(sep)[0]
            ayuda = ayuda[8:]
        ayudas.append(ayuda)
    for nombre_funcion in funciones:
         comentarios_funciones[nombre_funcion] = [autores[n], ayudas[n]]
         n+=1
    return comentarios_funciones


def crear_tabla(funciones):
    """[Autor: Camila Codina]
       [Ayuda: Genera una tabla con los nombres de las funciones que se podrían analizar]
    """
    Tabla = """
+--------------------------------------------------------------------+
|++++++++++++++++++++ FUNCIONES DEL PROGRAMA ++++++++++++++++++++++++|
|--------------------------------------------------------------------|
"""
    lista_nueva = []
    for i in range(0, len(funciones), 4):
        lista_nueva.append(funciones[i:i+4])
    for x in lista_nueva:
        while len(x) < 4:
            x.append(' ')
    print(Tabla)
    TableIt.printTable(lista_nueva)
    print("\n")
   

def usuario_ingresa_signo_pregunta(comentarios_funciones,fuente_unico_funciones, funcion_pedida):
    """[Autor: Camila Codina]
       [Ayuda: Respuesta en caso que el usuario pida "?". Imprimirá el nombre de la función elegida, su ayuda, sus parámetros, su módulo y su autor.]
    """
    signo_pregunta_funcion = {}
    ayuda_uso_funcion = comentarios_funciones[funcion_pedida][1]
    autor_funcion = comentarios_funciones[funcion_pedida][0]
    parametro_funcion = fuente_unico_funciones[funcion_pedida][0]
    parametro_funcion = parametro_funcion.replace(" ", ",")
    modulo_funcion = fuente_unico_funciones[funcion_pedida][1]
    signo_pregunta_funcion[funcion_pedida] = [ayuda_uso_funcion,parametro_funcion,modulo_funcion,autor_funcion]
    print("-------------------------------")
    print("Función:", funcion_pedida)
    print("Ayuda:",signo_pregunta_funcion[funcion_pedida][0])
    print("Parametros:",signo_pregunta_funcion[funcion_pedida][1])
    print("Modulo:",signo_pregunta_funcion[funcion_pedida][2])
    print("Autor:",signo_pregunta_funcion[funcion_pedida][3])
    print("-------------------------------")
    return signo_pregunta_funcion


def usuario_ingresa_numeral(comentarios_funciones,fuente_unico_funciones, funcion_pedida):
    """[Autor: Camila Codina]
       [Ayuda: Respuesta en caso que el usuario pida "#". Imprimirá el nombre de la función elegida, su ayuda, sus parámetros, su módulo y su autor. También imprimirá el código que la compone.]
    """
    codigo_funcion = fuente_unico_funciones[funcion_pedida][2]
    usuario_ingresa_signo_pregunta(comentarios_funciones,fuente_unico_funciones, funcion_pedida)
    print("Codigo de la funcion:")
    for x in codigo_funcion:
        print(x)
    print("-------------------------------")
    


def usuario_ingresa_signo_pregunta_todo(comentarios_funciones,fuente_unico_funciones,funciones):
    """[Autor: Camila Codina]
       [Ayuda: Respuesta en caso que el usuario pida "?todo". Imprimirá para cada función recibida de los csv (impresas en la tabla) lo que se imprime para una función en usuario_ingresa_signo_pregunta().]
    """
    for i in funciones:
        usuario_ingresa_signo_pregunta(comentarios_funciones,fuente_unico_funciones,i)


def usuario_ingresa_numeral_todo(comentarios_funciones,fuente_unico_funciones,funciones):
    """[Autor: Camila Codina]
       [Ayuda: Respuesta en caso que el usuario pida "#todo". Imprimirá para cada función recibida de los csv (impresas en la tabla) lo que se imprime para una función en usuario_ingresa_numeral().]
    """
    for i in funciones:
        usuario_ingresa_numeral(comentarios_funciones,fuente_unico_funciones, i)


def organizar_variables_archivo_ayuda_funciones(comentarios_funciones,fuente_unico_funciones,funcion):
    """[Autor: Camila Codina]
       [Ayuda: Utiliza el diccionario recibido de usuario_ingresa_signo_pregunta() para asignar variables que se utilizarán para crear el archivo ayuda_funciones.txt.]
    """ 
    signo_pregunta_funciones = usuario_ingresa_signo_pregunta(comentarios_funciones,fuente_unico_funciones,funcion)
    ayuda_uso_funcion = signo_pregunta_funciones[funcion][0]
    parametro_funcion = signo_pregunta_funciones[funcion][1]
    modulo_funcion = signo_pregunta_funciones[funcion][2]
    autor_funcion = signo_pregunta_funciones[funcion][3]
    return ayuda_uso_funcion, parametro_funcion, modulo_funcion, autor_funcion


def crear_archivo_ayuda_funciones(comentarios_funciones,fuente_unico_funciones,funciones):
    """[Autor: Camila Codina]
       [Ayuda: Crea archivo ayuda_funciones.txt con info de ?todo de manera que no se escriban mas de 80 caracteres por linea.]
    """   
    n=80
    with open('ayuda_funciones.txt','w') as crear_ayuda:
        for funcion in funciones:
            ayuda_uso_funcion, parametro_funcion, modulo_funcion, autor_funcion = organizar_variables_archivo_ayuda_funciones(comentarios_funciones,fuente_unico_funciones,funcion) 
            crear_ayuda.write(" Función:")
            crear_ayuda.write(funcion)
            crear_ayuda.write("\n Ayuda:")
            if len(ayuda_uso_funcion) > 80:
                ayuda_separada = [ayuda_uso_funcion[i:i+n] for i in range(0, len(ayuda_uso_funcion), n)]
                crear_ayuda.write(ayuda_separada[0])
                crear_ayuda.write("\n ")
                crear_ayuda.write(ayuda_separada[1])
            else: 
                crear_ayuda.write(ayuda_uso_funcion)
            crear_ayuda.write("\n Parametros:")
            crear_ayuda.write(parametro_funcion)
            crear_ayuda.write("\n Modulo:")
            crear_ayuda.write(modulo_funcion)
            crear_ayuda.write("\n Autor:")
            crear_ayuda.write(autor_funcion)
            crear_ayuda.write("\n ------------------------------- \n")       
   

def imprimir_ayuda_funciones():
    """[Autor: Camila Codina]
       [Ayuda: Imprime ayuda_funciones.txt.]
    """
    with open('ayuda_funciones.txt','r') as ayuda:
        for linea in ayuda:
            ayuda = linea.rstrip('\n')
            print(ayuda)
    

def respuesta_input(funcion_input,pedido,fuente_unico_funciones,comentarios_funciones, funciones):
    """[Autor: Camila Codina]
       [Ayuda: Input del usuario y respuesta del programa]
    """
    while funcion_input != "":
        if pedido[0] in funciones:
            if pedido[1] == "?":
                usuario_ingresa_signo_pregunta(comentarios_funciones,fuente_unico_funciones, pedido[0])
            elif pedido[1] == "#":
                usuario_ingresa_numeral(comentarios_funciones,fuente_unico_funciones, pedido[0])
            else:
                print("Carácter inválido. Intente nuevamente.")
        elif funcion_input == "?todo":
            usuario_ingresa_signo_pregunta_todo(comentarios_funciones,fuente_unico_funciones,funciones)
        elif funcion_input == "#todo":
            usuario_ingresa_numeral_todo(comentarios_funciones,fuente_unico_funciones,funciones)
        elif funcion_input == "imprimir ?todo":
            crear_archivo_ayuda_funciones(comentarios_funciones,fuente_unico_funciones,funciones)
            imprimir_ayuda_funciones()
        else:
            print("Función inexistente y/o carácter inválido. Intente nuevamente.")
        funcion_input = input(str("Función: "))
        pedido = funcion_input.split(" ")
    


def consulta_de_funciones():
    """[Autor: Camila Codina]
       [Ayuda: Bloque Principal]
    """
    funciones,listar_funciones = abrir_fuente_unico()
    fuente_unico_funciones = listar_fuente_unico(funciones,listar_funciones)

    lista_comentarios = abrir_comentarios()
    comentarios_funciones = listar_comentarios(lista_comentarios, funciones)
    
    crear_tabla(funciones)
    
    print("Se debe ingresar una de las funciones identificadas seguido de:")
    print("'?': muestra la descripción asociada al uso de la función, los parámetros que espera, el módulo y su autor.")
    print("'#': muestra todo lo relativo a la función")
    print("'?todo' y '#todo' listan esto para todas las funciones. 'imprimir ?todo' exporta a un archivo .txt '?todo' \n")
    
    funcion_input = input(str("Función: "))
    pedido = funcion_input.split(" ")

    respuesta_input(funcion_input,pedido,fuente_unico_funciones,comentarios_funciones,funciones)
    


