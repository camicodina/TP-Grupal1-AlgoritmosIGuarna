# Ver nombres de las funciones uno al lado del otro encolumnados

def tabla_nombre_funciones(comentarios):
    tabla = {}
    #diccionario con el nombre de la funcion y un
    return tabla

# Mensaje: "Funcion:" esperando uno de los nombres listados
# Seguido por 
# ?: descripción asociada al uso de la función en comillas triples
# (+ parámetros formales que espera, el módulo al que pertenece, y el autor)
# #: Todo lo relativo a la funcion
# Continua preguntando hasta que enter


def signo_pregunta(funcion):
    return 

def todo(funcion):
    return

# Si usuario ingresa "?todo": ? pero para toda funcion

def pregunta_todo(funcion):
    return

# "#todo"

def todo_todo(funcion):
    return


def respuesta_input(funcion):
    funcion_input = input("Función: ")
    while funcion_input != "":
        if "?todo":
            pregunta_todo(funcion)
        elif "#todo":
            todo_todo(funcion)
        elif "?":
            signo_pregunta(funcion)
        elif "#":
            todo(funcion)
        elif "imprimir ?todo":
            print(ayuda)
        else:
            print("Función inexistente y/o carácter inválido. Intente nuevamente.")
        funcion_input = input("Función: ")
          
    return






################### Bloque Principal ###################


comentarios = open("comentarios.csv")
ayuda = open("ayuda_funciones.txt")
respuesta_input(comentarios)
comentarios.close()
ayuda.close()

