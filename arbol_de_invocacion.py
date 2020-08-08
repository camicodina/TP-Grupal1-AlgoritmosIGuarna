def leer_archivo(archivo):
    """[Autor: Mateo Villarinos]
       [Ayuda: funcion que toma un modulo para devolver un diccionario con el nombre de las funciones
       y como valor en la cantidad de lineas y las invocaciones]
    """
    diccionario_de_funciones = {}
    diccionario_final = {}
    for linea in archivo:
        lista_linea = linea.rstrip("\n").split(",")
        diccionario_de_funciones[lista_linea[0]] = lista_linea[3:]
    lista_de_funciones = list(diccionario_de_funciones.keys())
    for titulo in lista_de_funciones:
        diccionario_final[titulo] = [str(len(diccionario_de_funciones[titulo]))]
        for key in diccionario_de_funciones:
            i = 0
            while i < len(diccionario_de_funciones[titulo]):
                if key in diccionario_de_funciones[titulo][i]:
                    diccionario_final[titulo].append(key)
                    i += 1
                else:
                     i += 1
    return diccionario_final

def buscar_main(diccionario):
    """[Autor: Mateo Villarinos]
       [Ayuda: funcion que buscar cual es la funcion principal del programa]
    """
    i = 0
    main = ""
    for key in diccionario:
        no_encontro_main = True
        if no_encontro_main:
            for lista in diccionario:
                if key in diccionario[lista]:
                    no_encontro_main = False
            if no_encontro_main:
                main = key
    return main
            


def dibujar_arbol(archivo):
    """[Autor: Mateo Villarinos]
       [Ayuda: funcion que va determinando las bases del arbol]
    """
    dicc_arbol = leer_archivo(archivo)
    principio = buscar_main(dicc_arbol)
    lista_de_seguimiento = []
    posiciones = [1]
    flecha = " ---> "
    indentacion = ""
    arbol = principio + "({})".format(dicc_arbol[principio][0])
    k, n = principio, 0
    while posiciones[0] < len(dicc_arbol[principio]):
        nl = False
        while len(dicc_arbol[k]) > 1 and posiciones[n] < len(dicc_arbol[k]) and posiciones[0] < len(dicc_arbol[principio]):
            posiciones.append(1)
            lista_de_seguimiento.append(k)
            nl,n,k,indentacion,arbol = analizar_arbol(arbol,indentacion,k,n,nl,dicc_arbol,posiciones,flecha,lista_de_seguimiento)
        if nl:
            arbol += "\n"
        posiciones[n-1] += 1
        k = lista_de_seguimiento[-1]
        if posiciones[n-1] > 1:
            lista_de_seguimiento.pop(-1)
            posiciones.pop(-1)
            n -= 1             
    return arbol

def analizar_arbol(arbol,indentacion,k,n,nl,dicc_arbol,posiciones,flecha,lista_de_seguimiento):
    """[Autor: Mateo Villarinos]
       [Ayuda: funcion que mediante diferentes algoritmos va dibujando el arbol]
    """
    if arbol[-1:] == "\n":
        indentacion = (n)*6*" "
        for campo in lista_de_seguimiento:
            indentacion += len(campo)*" "+(len(dicc_arbol[campo][0])+2)*" "
        arbol += indentacion
    k = dicc_arbol[k][posiciones[n]]
    n += 1
    arbol += flecha + k + "({})".format(dicc_arbol[k][0])
    nl = True
    return nl,n,k,indentacion,arbol
      
def leer():
    """[Autor: Mateo Villarinos]
       [Ayuda: funcion main]
    """
    fuente_unico= open('fuente_unico.csv','r' )
    print(dibujar_arbol(fuente_unico))
    fuente_unico.close()

