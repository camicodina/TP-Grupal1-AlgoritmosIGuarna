import csv
import TableIt

def listar_fuente_unico():
    """[Autor: Camila Codina]
       [Ayuda: Toma valores de fuente_unico.csv y crea una lista]
    """

    with open('fuente_unico.csv', newline='') as fu:
        reader = csv.reader(fu)
        fuente_unico_funciones = list(reader)
    print(fuente_unico_funciones)
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
+--------------------------------------------------------------+
|+++++++++++++++++ FUNCIONES DEL PROGRAMA +++++++++++++++++++++|
|--------------------------------------------------------------|
"""
    lista_nueva = []
    for i in range(0, len(nombres_funciones_ordenadas), 3):
        lista_nueva.append(nombres_funciones_ordenadas[i:i+3])
    print(Tabla)
    
    # Tabla = (Tabla.format('\n'.join("  {0}     {1}       {2}  ".format(*fila) for fila in lista_nueva)))
    # print(Tabla)
    TableIt.printTable(lista_nueva)
    return


def signo_pregunta(comentarios_funciones,fuente_unico_funciones, funcion_elegida):
    signo_pregunta = {}
    ayuda_uso_funcion = comentarios_funciones[funcion_elegida][1]
    for i in fuente_unico_funciones:
        if i[0] == funcion_elegida:
            parametro_funcion = fuente_unico_funciones[i][1]
            modulo_funcion = fuente_unico_funciones[i][2]
    autor_funcion = comentarios_funciones[funcion_elegida][0]
    signo_pregunta[funcion_elegida] = [ayuda_uso_funcion,parametro_funcion,modulo_funcion,autor_funcion]
    print("-------------------------------")
    print("Función:", signo_pregunta[funcion_elegida])
    print("Ayuda:",signo_pregunta[funcion_elegida][0])
    print("Parametros:",signo_pregunta[funcion_elegida][1])
    print("Modulo:",signo_pregunta[funcion_elegida][2])
    print("Autor:",signo_pregunta[funcion_elegida][2])
    print("-------------------------------")
    return signo_pregunta
    
def numeral(comentarios_funciones,fuente_unico_funciones, funcion_elegida):
    relativo_funcion = []
    for i in fuente_unico_funciones:
        if i[0] == funcion_elegida:
            relativo_funcion.append(i[3:])
    signo_pregunta(comentarios_funciones,fuente_unico_funciones, funcion_elegida)
    print("Codigo de la funcion:", "\n", relativo_funcion)
    return relativo_funcion
 

def signo_pregunta_todo(comentarios_funciones,fuente_unico_funciones):
    signo_pregunta_todo = []
    for i in comentarios_funciones:
        signo_pregunta(comentarios_funciones,fuente_unico_funciones, i)
        signo_pregunta_todo.append(signo_pregunta)
    return 


def numeral_todo(comentarios_funciones,fuente_unico_funciones):
    numeral_todo = []
    for i in comentarios_funciones:
        numeral(comentarios_funciones,fuente_unico_funciones, i)
        numeral_todo.append(numeral)
    return numeral_todo


def crear_ayuda_funciones(comentarios_funciones,fuente_unico_funciones):
    """[Autor: Camila Codina]
       [Ayuda: Crea archivo ayuda_funciones.txt con info de ?todo]
    """
    llamado_todo = signo_pregunta_todo(comentarios_funciones,fuente_unico_funciones)
    with open('ayuda_funciones.txt','w') as crear_ayuda:
        crear_ayuda.write(llamado_todo)
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
            print(signo_pregunta_todo(comentarios_funciones,fuente_unico_funciones))
        elif funcion_input == "#todo":
            print(numeral_todo(comentarios_funciones,fuente_unico_funciones))
        elif funcion_input == "imprimir ?todo":
            print(crear_ayuda_funciones(comentarios_funciones,fuente_unico_funciones))
        else:
            print("Función inexistente y/o carácter inválido. Intente nuevamente.")
        funcion_input = input(str("Función: "))
        pedido = funcion_input.split(" ")
    return



################### Bloque Principal ###################

funcion_input = input(str("Función: "))
pedido = funcion_input.split(" ")
comentarios_funciones,nombres_funciones_ordenadas = listar_comentarios()
fuente_unico_funciones = listar_fuente_unico()
crear_tabla(nombres_funciones_ordenadas)
respuesta_input(funcion_input,pedido,comentarios_funciones,fuente_unico_funciones)

