from csv import reader


def fuente_unico():
    listar_funciones =[]
    fuente_unico=[]
    with open('fuente_unico.csv','r') as fuente_unico:
        for linea in fuente_unico:
            listar_funciones.append([linea.rstrip('\n')])
    for x in listar_funciones:
        for line in reader(x):
            temp = line
            fuente_unico.append(temp)
    
        print(listar_funciones)
        print(fuente_unico)
        
    return

fuente_unico()