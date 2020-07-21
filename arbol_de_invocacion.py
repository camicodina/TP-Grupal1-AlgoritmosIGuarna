from consulta_de_funciones import listar_funciones

def leer_archivo(archivo):
    diccionario_de_funciones = listar_funciones()
    contador1 = 0
    contador2 = 1
    for linea in archivo:
        lista_linea = linea.rstrip("\n").split(",")
        diccionario_de_funciones[lista_linea[0]] = [str(len(lista_linea)-3)]
        for campo in lista_linea[3:]:
            if campo in diccionario_de_funciones and campo not in diccionario_de_funciones[lista_linea[0]]:
                diccionario_de_funciones[lista_linea[0]].append(campo)
    return diccionario_de_funciones

def buscar_main(archivo):
    dicc_main = leer_archivo(archivo)
    i = 0
    main = ""
    encontro_main = False
    while i < len(list(dicc_main.keys())) and not encontro_main:
        if list(dicc_main.keys())[i] in dicc_main.values():
            encontro_main = False
        else:
            encontro_main = True
            main = list(dicc_main.keys())[i]           
    return main

def dibujar_arbol(archivo):
    dicc_arbol = leer_archivo(archivo)
    principio = buscar_main(archivo)
    lista_de_seguimiento = []
    posiciones = [1]
    flecha = "--->"
    indentacion = ""
    arbol = principio + "({})".format(dicc_arbol[principio][0])
    k, n = principio, 0
    while posiciones[0] < len(dicc_arbol[principio]):
        nl = False
        while len(dicc_arbol[k]) > 1 and posiciones[n] < len(dicc_arbol[k]) and posiciones[0] < len(dicc_arbol[principio]):
            posiciones.append(1)
            lista_de_seguimiento.append(k)
            if arbol[-1:] == "\n":
                indentacion = (n)*4*" "
                for campo in lista_de_seguimiento:
                    indentacion += len(campo)*" "+(len(dicc_arbol[campo][0])+2)*" "
                arbol += indentacion
            k = dicc_arbol[k][posiciones[n]]
            n += 1
            arbol += flecha + k + "({})".format(dicc_arbol[k][0])
            nl = True
        if nl:
            arbol += "\n"
        
        posiciones[n-1] += 1
        k = lista_de_seguimiento[-1]
        if posiciones[n-1] > 1:
            lista_de_seguimiento.pop(-1)
            posiciones.pop(-1)
            n -= 1             
    return arbol

        
        
def leer():
    fuente_unico= open('fuente_unico.csv','r' )
    print(dibujar_arbol(fuente_unico))
    fuente_unico.close()
    
leer()
