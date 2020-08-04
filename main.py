import TableIt
from m_cargar_archivos import cargar_archivo
from panel_de_funciones import generacion_archivo
from consulta_de_funciones import consulta_de_funciones
from analizador import generar_analizador
from arbol_de_invocacion import leer
from info_desarrollador import generacion_participacion


def opciones_usuario():
    """[Autor: Camila Codina]
       [Ayuda: Redirecciona a los módulos]
    """
    usuario_input = input("Seleccione un número:")
    while usuario_input != "":
        if usuario_input == "1":
            generacion_archivo()
        elif usuario_input == "2":
            consulta_de_funciones()
        elif usuario_input == "3":
            generar_analizador()
        elif usuario_input == "4":
            leer()
        elif usuario_input == "5":
            generacion_participacion()
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
    cargar_archivo()
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
