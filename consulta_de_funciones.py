import TableIt

def listar_fuente_unico():
    """[Autor: Camila Codina]
       [Ayuda: Toma valores de fuente_unico.csv y crea un diccionario]
    """
    listar_funciones =[]
    funciones = []
    parametros = []
    modulos = []
    codigos = []
    fuente_unico_funciones={}
    n=0
    with open('fuente_unico.csv','r') as fuente_unico:
        for linea in fuente_unico:
            funciones.append(linea.rstrip("\n").split(",")[0])
            parametros.append(linea[linea.find("(")+1:linea.rfind(")")])
            listar_funciones.append(linea.rstrip('\n'))
        for funcion in listar_funciones:
            a = funcion
            a = a.replace('),', ')//').split('//')
            modulo = a[1].split(",")[0]
            modulos.append(modulo)
            codigo_funcion = a[1].lstrip(modulo)
            codigos.append(codigo_funcion.split(","))
        for recibido in funciones:
            fuente_unico_funciones[recibido] = [parametros[n], modulos[n], codigos[n]]
            n+=1
    return fuente_unico_funciones


def listar_comentarios():
    """[Autor: Camila Codina]
       [Ayuda: Toma valores de comentarios.csv y crea un diccionario]
    """
    with open('comentarios.csv','r') as comentarios:
        comentarios_funciones = {}
        nombres_funciones_ordenadas = []
        for linea in comentarios:
            nombre_funcion, autor, ayuda_uso, otro= linea.rstrip("\n").split(",")
            comentarios_funciones[nombre_funcion] = [autor, ayuda_uso, otro]
            nombres_funciones_ordenadas.append(nombre_funcion)
    return comentarios_funciones,nombres_funciones_ordenadas

def crear_tabla(nombres_funciones_ordenadas):
    """[Autor: Camila Codina]
       [Ayuda: Genera una tabla con los nombres de las funciones que se podrían analizar]
    """
    Tabla = """
       +--------------------------------------------------------------------+
       |++++++++++++++++++++ FUNCIONES DEL PROGRAMA ++++++++++++++++++++++++|
       |--------------------------------------------------------------------|
"""
    lista_nueva = []
    for i in range(0, len(nombres_funciones_ordenadas), 4):
        lista_nueva.append(nombres_funciones_ordenadas[i:i+4])
    for x in lista_nueva:
        while len(x) < 4:
            x.append(' ')
    print(Tabla)
    TableIt.printTable(lista_nueva)
    print("\n")
    return


def signo_pregunta(comentarios_funciones,fuente_unico_funciones, funcion_pedida):
    """[Autor: Camila Codina]
       [Ayuda: Respuesta en caso que el usuario pida "?"]
    """
    signo_pregunta_funcion = {}
    ayuda_uso_funcion = comentarios_funciones[funcion_pedida][1]
    autor_funcion = comentarios_funciones[funcion_pedida][0]
    parametro_funcion = fuente_unico_funciones[funcion_pedida][0]
    modulo_funcion = fuente_unico_funciones[funcion_pedida][1]
    signo_pregunta_funcion = {funcion_pedida:[ayuda_uso_funcion,parametro_funcion,modulo_funcion,autor_funcion]}
    print("-------------------------------")
    print("Función:", funcion_pedida)
    print("Ayuda:",signo_pregunta_funcion[funcion_pedida][0])
    print("Parametros:",signo_pregunta_funcion[funcion_pedida][1])
    print("Modulo:",signo_pregunta_funcion[funcion_pedida][2])
    print("Autor:",signo_pregunta_funcion[funcion_pedida][3])
    print("-------------------------------")
    return signo_pregunta_funcion
    
def numeral(comentarios_funciones,fuente_unico_funciones, funcion_pedida):
    """[Autor: Camila Codina]
       [Ayuda: Respuesta en caso que el usuario pida "#"]
    """
    codigo_funcion = fuente_unico_funciones[funcion_pedida][2]
    signo_pregunta(comentarios_funciones,fuente_unico_funciones, funcion_pedida)
    print("Codigo de la funcion:")
    for x in codigo_funcion:
        print(x)
    print("-------------------------------")
    return
 

def signo_pregunta_todo(comentarios_funciones,fuente_unico_funciones,nombres_funciones_ordenadas):
    """[Autor: Camila Codina]
       [Ayuda: Respuesta en caso que el usuario pida "?todo"]
    """
    signo_pregunta_todas_funciones = []
    for i in nombres_funciones_ordenadas:
        signo_pregunta(comentarios_funciones,fuente_unico_funciones, i)
        signo_pregunta_funcion = signo_pregunta(comentarios_funciones,fuente_unico_funciones, i)
        signo_pregunta_todas_funciones.append(signo_pregunta_funcion)
    return signo_pregunta_todas_funciones


def numeral_todo(comentarios_funciones,fuente_unico_funciones,nombres_funciones_ordenadas):
    """[Autor: Camila Codina]
       [Ayuda: Respuesta en caso que el usuario pida "#todo"]
    """
    for i in nombres_funciones_ordenadas:
        numeral(comentarios_funciones,fuente_unico_funciones, i)
    return 


def crear_ayuda_funciones(comentarios_funciones,fuente_unico_funciones,nombres_funciones_ordenadas):
    """[Autor: Camila Codina]
       [Ayuda: Crea archivo ayuda_funciones.txt con info de ?todo]
    """
    llamado_todo = signo_pregunta_todo(comentarios_funciones,fuente_unico_funciones,nombres_funciones_ordenadas)
    with open('ayuda_funciones.txt','w') as crear_ayuda:
        for x in llamado_todo:
            for i in nombres_funciones_ordenadas:
                crear_ayuda.write("-------------------------------")
                crear_ayuda.write(i)
                crear_ayuda.write("Ayuda:")
                crear_ayuda.write(x[i][0])
                crear_ayuda.write("Parámetros:")
                crear_ayuda.write(x[i][1])
                crear_ayuda.write("Módulo:")
                crear_ayuda.write(x[i][2])
                crear_ayuda.write("Autor:")
                crear_ayuda.write(x[i][3])
                crear_ayuda.write("-------------------------------")    
    return


def leer_ayuda_funciones():
    """[Autor: Camila Codina]
       [Ayuda: Formatea ayuda_funciones.txt para que no aparezcan mas de 80 caracteres por linea con info de ?]
    """
    with open('ayuda_funciones.txt','r') as ayuda:
        todo_ayuda = ayuda.readlines()
        ayuda = todo_ayuda[0]
        n = 80
        ayuda = [ayuda[i:i+n] for i in range(0, len(ayuda), n)]
        print(ayuda)
    return 


def respuesta_input(funcion_input,pedido,fuente_unico_funciones,comentarios_funciones, nombres_funciones_ordenadas):
    """[Autor: Camila Codina]
       [Ayuda: Input del usuario y respuesta del programa]
    """
    funcion_elegida = ''
    while funcion_input != "":
        if pedido[0] in nombres_funciones_ordenadas:
            if pedido[1] == "?":
                signo_pregunta(comentarios_funciones,fuente_unico_funciones, pedido[0])
            elif pedido[1] == "#":
                numeral(comentarios_funciones,fuente_unico_funciones, pedido[0])
            else:
                print("Carácter inválido. Intente nuevamente.")
        elif funcion_input == "?todo":
            signo_pregunta_todo(comentarios_funciones,fuente_unico_funciones,nombres_funciones_ordenadas)
        elif funcion_input == "#todo":
            numeral_todo(comentarios_funciones,fuente_unico_funciones,nombres_funciones_ordenadas)
        elif funcion_input == "imprimir ?todo":
            crear_ayuda_funciones(comentarios_funciones,fuente_unico_funciones,nombres_funciones_ordenadas)
        else:
            print("Función inexistente y/o carácter inválido. Intente nuevamente.")
        funcion_input = input(str("Función: "))
        pedido = funcion_input.split(" ")
    return



def consulta_de_funciones():
    """[Autor: Camila Codina]
       [Ayuda: Bloque Principal]
    """
    comentarios_funciones,nombres_funciones_ordenadas = listar_comentarios()
    fuente_unico_funciones = listar_fuente_unico()
    crear_tabla(nombres_funciones_ordenadas)
    funcion_input = input(str("Función: "))
    pedido = funcion_input.split(" ")
    respuesta_input(funcion_input,pedido,fuente_unico_funciones,comentarios_funciones, nombres_funciones_ordenadas)
    return

consulta_de_funciones()

