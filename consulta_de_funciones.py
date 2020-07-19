def listar_fuente_unico():
    """[Autor: Camila Codina]
       [Ayuda: Toma valores de comentarios.csv]
    """
    with open('fuente_unico.csv','r') as fuente_unico:
        fuente_unico_funciones = []
        for linea in fuente_unico:
            fuente_unico_funciones.append([linea.rstrip('\n')])
        # for i in fuente_unico_funciones:
        #     nombre_funcion_fu = fuente_unico_funciones[i][0]
        #     parametro = fuente_unico_funciones[i][1]
        #     modulo = fuente_unico_funciones[i][2]
    return fuente_unico_funciones

def listar_comentarios():
    """[Autor: Camila Codina]
       [Ayuda: Toma valores de fuente_unico.csv]
    """
    with open('comentarios.csv','r') as comentarios:
        comentarios_funciones = {}
        for linea in comentarios:
            nombre_funcion, autor, ayuda_uso, otro= linea.rstrip("\n").split(",")
            comentarios_funciones[nombre_funcion] = [autor, ayuda_uso, otro]
    return comentarios_funciones


def crear_tabla(funciones):
    """[Autor: Camila Codina]
       [Ayuda: Genera una tabla con los nombres de las funciones que se podrían analizar]
    """
    Tabla = """\
        +---------------------------------------------------------------------+
        |    +++++++++++++++++ FUNCIONES DEL PROGRAMA ++++++++++++++++++++    |
        |---------------------------------------------------------------------|
            {}
        +---------------------------------------------------------------------+\
        """
        # for funcion in funciones:
        #     Tabla = Tabla.format("\n".join("{1}{0}{1} {1}{0}{1} {1}{0}{1} {1}{0}{1}").format(funcion, "|"))
    print(Tabla)
    return

def signo_pregunta(comentarios_funciones,fuente_unico_funciones, funcion_elegida):
    ayuda_uso_funcion = comentarios_funciones[funcion_elegida][1]
    for i in fuente_unico_funciones:
        if i[0] == funcion_elegida:
            parametro_funcion = fuente_unico_funciones[i][1]
            modulo_funcion = fuente_unico_funciones[i][2]
    autor_funcion = comentarios_funciones[funcion_elegida][0]
    signo_pregunta = {funcion_elegida: [ayuda_uso_funcion,parametro_funcion,modulo_funcion,autor_funcion]}
    return signo_pregunta

def numeral(comentarios_funciones,fuente_unico_funciones, funcion_elegida):
    relativo_funcion = []
    for i in fuente_unico_funciones:
        if i[0] == funcion_elegida:
            relativo_funcion.append(i)
    relativo_funcion.append(comentarios_funciones[funcion_elegida][1])
    relativo_funcion.append(comentarios_funciones[funcion_elegida][2])
    return relativo_funcion

def signo_pregunta_todo(comentarios_funciones,fuente_unico_funciones):
    signo_pregunta_todo = []
    for i in comentarios_funciones:
        signo_pregunta_todo.append(signo_pregunta(comentarios_funciones,fuente_unico_funciones, i))
    return signo_pregunta_todo

def numeral_todo(comentarios_funciones,fuente_unico_funciones):
    numeral_todo = []
    for i in comentarios_funciones:
        numeral_todo.append(numeral(comentarios_funciones,fuente_unico_funciones, i))
    return numeral_todo


def crear_ayuda_funciones(signo_pregunta_todo):
    """[Autor: Camila Codina]
       [Ayuda: Crea archivo ayuda_funciones.txt con info de ?todo]
    """
    with open('ayuda_funciones.txt','w') as crear_ayuda:
        crear_ayuda.write(signo_pregunta_todo)
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
        # for i in fuente_unico_funciones:
        #     nombre_funcion_fu = fuente_unico_funciones[i][0]
        #     parametro = fuente_unico_funciones[i][1]
        #     modulo = fuente_unico_funciones[i][2]
        print(ayuda)
    return 

def respuesta_input(funcion_input,pedido,fuente_unico_funciones,comentarios_funciones):
    """[Autor: Camila Codina]
       [Ayuda: Input del usuario y respuesta del programa]
    """
    while funcion_input != "":
        if pedido[0] in comentarios_funciones:
            if pedido[1] == "?":
                print(signo_pregunta(fuente_unico_funciones,comentarios_funciones, pedido[0]))
            elif pedido[1] == "#":
                print(numeral(fuente_unico_funciones,comentarios_funciones, pedido[0]))
            else:
                print("Carácter inválido. Intente nuevamente.")
        elif funcion_input == "?todo":
            print(signo_pregunta_todo())
        elif funcion_input == "#todo":
            print(numeral_todo())
        elif funcion_input == "imprimir ?todo":
            print(crear_ayuda(signo_pregunta_todo))
        else:
            print("Función inexistente y/o carácter inválido. Intente nuevamente.")
        funcion_input = input(str("Función: "))
        pedido = funcion_input.split(" ")
    return

################### Bloque Principal ###################

funcion_input = input(str("Función: "))
pedido = funcion_input.split(" ")
comentarios_funciones = listar_comentarios()
fuente_unico_funciones = listar_fuente_unico()
signo_pregunta_todo(comentarios_funciones,fuente_unico_funciones)
respuesta_input(funcion_input,pedido,comentarios_funciones,fuente_unico_funciones)
# respuesta_input(comentarios)
# comentarios.close()
listar_fuente_unico()
