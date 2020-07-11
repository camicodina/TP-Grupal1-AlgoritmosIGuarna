"""
fuente_unico.csv(alfabeticamente_nombre_funcion)
nombre_funcion,(paramentros,formales),nombre_modulo,linea_codigo,linea_codigo.....

comentaios.csv(alfabeticamente_nombre_funcion)

nombre_funcion,nombre_autor-[Autor: Juan Perez]-,ayuda- [Ayuda: Obtener deuda del cliente en base a la tasa de
actualización y totales adeudados recibidos]-,"comentario adicionales"
"""
# Definición de Funciones

#Análisis de Fuente Único
def analisis_fuente_unico(lista):

    lineas_codigo= len(lista)-2
    c_returns=0 #no debería ser 1????
    c_if=0
    c_for=0
    c_while=0
    c_break=0
    c_exit=0

    for i in range (2, len(lista)):
        if 'if ' in lista[i] or 'elif ' in lista[i]:
            c_if+=1

        elif 'for ' in lista[i]:
            c_for+=1

        elif 'while ' in lista[i]:
            c_while+=1

        elif 'break' in lista[i]:
            c_break+=1

        elif 'exit' in lista[i]:
            c_exit+=1
        
         
    return [lineas_codigo, c_returns, c_if, c_for, c_while, c_break, c_exit]

def analisis_comentarios(lista):

        comentarios=len(lista)-3
        
        autor= lista[1]

        ayuda= 'Si'
        if lista[2]=='':
            ayuda='No'

    return [comentarios, ayuda, autor]

def panel_de_funciones(fuente_unico, comentarios):
    columnas=[Nombre de la Función.Módulo, Cantidad de Parámetros Formales, Cantidad de líneas de código, Cantidad de invocaciones a la función, Cantidad de Puntos de Salida, Cantidad de If, Cantidad de For, Cantidad de While, Cantidad de Break, Cantidad de Exit, Cantidad de líneas de comentarios, Indicador de Descripción Función, Autor/Responsable]

     writer=csv.DictWriter(panel_general, fieldnames=columnas)

     writer.writeheader()

     for linea in fuente_unico:
         analisis_fuente_unico(linea)

         analisis_comentarios(linea)
        
         writer.writerow({'Nombre de la Función.Módulo': linea[0], 'Cantidad de Parámetros Formales': len(linea[1])},'Cantidad de líneas de código': analisis_fuente_unico(linea)[0], 'Cantidad de invocaciones a la función': 000, 'Cantidad de Puntos de Salida':analisis_fuente_unico(linea)[1], 'Cantidad de If':analisis_fuente_unico(linea)[2], 'Cantidad de For':analisis_fuente_unico(linea)[3], 'Cantidad de While':analisis_fuente_unico(linea)[4], 'Cantidad de Break':analisis_fuente_unico(linea)[5], 'Cantidad de Exit':analisis_fuente_unico(linea)[6], 'Cantidad de líneas de comentarios':analisis_comentarios(linea)[0] , 'Indicador de Descripción Función':analisis_comentarios(linea)[1], 'Autor/Responsable':analisis_comentarios(linea)[2]   )

    return 






#Main
import csv
fuente_unico= open('fuente_unico.csv','r' )

comentarios= open('comentaios.csv','r' )

panel_general= open('panel_general.csv','w', newline='' )


fuente_unico.close()

comentarios.close()

panel_general.close()
