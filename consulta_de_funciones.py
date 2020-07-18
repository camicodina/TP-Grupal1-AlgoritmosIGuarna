def listar_funciones():
    """[Autor: Camila Codina]
       [Ayuda: Toma valores de comentarios.csv]
    """
    with open('comentarios.csv','r') as comentarios:
        funciones = {}
        for linea in comentarios:
            nombre_funcion, autor, ayuda_uso, otro= linea.rstrip("\n").split(",")
            funciones[nombre_funcion] = [autor, ayuda_uso, otro]

    return funciones

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


def respuesta_input(funciones):
    """[Autor: Camila Codina]
       [Ayuda: Input del usuario y respuesta del programa]
    """
    funcion_input = input(str("Función: "))
    pedido = funcion_input.split(" ")
    while funcion_input != "":
        if pedido[0] in funciones:
            if pedido[1] == "?":
                print(funciones[pedido[0]][1])
            elif pedido[1] == "#":
                print(funciones[pedido[0]])
            else:
                print("Carácter inválido. Intente nuevamente.")
        elif funcion_input == "?todo":
            for i in funciones:
                print(i, "\n" ,funciones[i][1])
        elif funcion_input == "#todo":
            for i in funciones:
                print(i, "\n" ,funciones[i])
        elif funcion_input == "imprimir ?todo":
            print(ayuda(ayuda))
        else:
            print("Función inexistente y/o carácter inválido. Intente nuevamente.")
        funcion_input = input(str("Función: "))
        pedido = funcion_input.split(" ")
    return

def ayuda(ayuda):

    return




################### Bloque Principal ###################


# comentarios = open("comentarios.csv")
ayuda = open("ayuda_funciones.txt")
funciones = listar_funciones()
respuesta_input(funciones)
# respuesta_input(comentarios)
# comentarios.close()
ayuda.close()

