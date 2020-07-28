import TableIt
import m_cargar_archivos as ca
import panel_de_funciones as pf
import consulta_de_funciones as cf
import analizador
import arbol_de_invocacion as adi
import info_desarrollador as infod


def opciones_usuario():
    """[Autor: Camila Codina]
       [Ayuda: Redirecciona a los módulos]
    """
    usuario_input = input("Seleccione un número:")
    while usuario_input != "":
        if usuario_input == "1":
            pf.generacion_archivo()
        elif usuario_input == "2":
            cf.consulta_de_funciones()
        elif usuario_input == "3":
            analizador.generar_analizador()
        elif usuario_input == "4":
            adi.leer()
        elif usuario_input == "5":
            infod.generacion_participacion()
        else:
            print("Número no válido. Intente nuevamente")
        usuario_input = input("Seleccione un número:")
    print("Gracias por testear nuestro MVP!")
    return

def main():
    """[Autor: Camila Codina]
       [Ayuda: Frontend de la aplicación]
    """
    print("Ingrese un archivo en formato .txt con los nombres de los archivos a analizar")
    ca.cargar_archivo()
    print("Seleccione el número de la función a realizar")
    print("ENTER para salir")
    opciones = [
    ["1) Panel de funciones"],
    ["2) Consulta de Funciones"],
    ["3) Analizador de Reutalizacion de codigo"],
    ["4) Arbol de invocacion"],
    ["5) Informacion por desarrollador"]
    ]
    TableIt.printTable(opciones)
    opciones_usuario()
    return 

main()
