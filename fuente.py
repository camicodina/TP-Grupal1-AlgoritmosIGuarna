def listar_fuente_unico():
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
    print(fuente_unico_funciones)
    return fuente_unico_funciones

listar_fuente_unico()

