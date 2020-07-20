from consulta_de_funciones import listar_funciones

def dicc_a_lista():
    diccionario_de_funciones = listar_funciones()
    lista = list(diccionario_de_funciones.keys())
    return lista

def leer_archivo():
    lista_de_invocaciones = []
    dicc_de_invocaciones ={}
    lista_de_funciones = dicc_a_lista()
    fuente_unico= open('fuente_unico.csv','r' )
    contador1 = 0
    contador2 = 1
    for linea in fuente_unico:
        lista_linea = linea.rstrip("\n").split(",")
        dicc_de_invocaciones[lista_linea[0]] = len(lista_linea[3:])
        while (len(lista_linea[3:]) >= contador1) and (contador2 < len(lista_de_funciones)):
            if lista_de_funciones[contador2] in lista_linea[3:]:
                lista_de_invocaciones.append((lista_linea[0],lista_de_funciones[contador2]))
                contador2 += 1
                contador1 +=1
            else:
                contador2 += 1
        else:
            contador2 = 0
            contador1 = 0
    fuente_unico.close()
    return lista_de_invocaciones , dicc_de_invocaciones

def invocaciones_y_lineas():
    lista_final, dicc = leer_archivo()
    i,x = 0,0
    while x < 2:
        while i < len(lista_final):
            if lista_final[i][x] in dicc.keys():
                lista_final[i] = list(lista_final[i])
                lista_final[i][x] = "{}({})".format(lista_final[i][x],dicc[lista_final[i][x]])
            else:
                i += 1
        else:
            x += 1
            i = 0
    return lista_final

def arbol_invocador():
    lista_arbol = invocaciones_y_lineas()
    funcion_actual = buscar_main()
    actual = funcion_actual
    siguiente, espacio_actual = "-->", ""
    print(funcion_actual, end = "")
    j,k,n = 0,0,4
    while len(lista_arbol) != 0:
        if j != len(lista_arbol) and funcion_actual in lista_arbol[j][0]:
            print(siguiente,lista_arbol[j][1], end = "")
            funcion_actual = lista_arbol[j][1]
            j = 0
        elif j != len(lista_arbol) and funcion_actual not in lista_arbol[j][0]:
            j += 1
        elif j == len(lista_arbol):
            seguir = True
            while seguir and k < (len(lista_arbol)):
                if funcion_actual in lista_arbol[k][1]:
                    print("")
                    espacio_actual += " " * (len(funcion_actual)+n)
                    print(espacio_actual, end = "")
                    n += 2
                    funcion_actual,actual = actual,lista_arbol[k][0]
                    lista_arbol.remove(lista_arbol[k])
                    j,k = 0,0
                    seguir = False
                else:
                    k += 1 
    
def buscar_main():
    invocaciones = invocaciones_y_lineas()
    falta_main = True
    main = ""
    cont1,cont2 = 0,1
    while falta_main:
        if not invocaciones[cont1][0] in invocaciones[cont2][1]:
            cont2 += 1
            if cont2 == len(invocaciones):
                main = invocaciones[cont1][0]
                falta_main = False
        else: 
            cont1 += 1
    return main
arbol_invocador()
