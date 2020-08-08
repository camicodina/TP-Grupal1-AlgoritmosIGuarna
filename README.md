# Trabajo Práctico Grupal Nº1 - Algoritmos I, Cátedra Guarna, FIUBA


## Descripción General 

Se deberá tomar el conjunto de programas que formen la aplicación a analizar, y realizar una serie de operaciones, que permitan la generación de información, con el objetivo de evaluar si la construcción obedece a los paradigmas del diseño modular y la programación estructurada. 
Los programas que forman parte de la aplicación a analizar, vendrán informados en un archivo, denominado, programas.txt (dentro de la carpeta programa_prueba). Cada línea en este archivo contendrá el camino completo al programa, incluido su nombre. En la primera línea del archivo, debe ir el programa en el que se encuentra el bloque principal de ejecución de la aplicación. Las líneas subsiguientes, contendrán aquellos programas que correspondan a librerías o módulos codificados por el usuario, y que también formen parte de la aplicación en cuestión. 

## Descripción de las prestaciones 

Al inicio, la aplicación deberá tomar el conjunto de programas que se encuentran en programas.txt y procesarlos de forma tal de obtener como salida dos archivos: 

1. fuente_unico.csv: contendrá sólo código. Debe excluir todo tipo de comentario. Incluirá todas las funciones que forman parte de la aplicación, en orden alfabético. 
   - El primer campo será el nombre de la función y dará el orden al archivo alfabéticamente. 
   - El segundo campo serán los parámetros formales, incluidos los paréntesis. 
   - El tercer campo será el nombre del módulo al que pertenece la función. 
   - El resto de los campos, serán cada una de las instrucciones de código que forman parte de la función. Cada línea de código será un nuevo campo, por lo tanto se encontrarán separadas por una “,” y la cantidad será variable, ya que dependerá de la cantidad de líneas de código que formen parte de la función.

2. comentarios.csv: contendrá sólo comentarios y el nombre de la función.
    - El primer campo será el nombre de la función y dará el orden al archivo alfabéticamente.
    - El segundo campo será el nombre del autor/responsable de la función. Para obtener esta información se debe extraer de la sección que se encuentra entre comillas triples e inmediatamente después de la firma de la función; lo que esté identificado con el siguiente marcado, a modo de ejemplo [Autor: Juan Perez].
    - El tercer campo será la descripción de ayuda de uso de la función, que de igual modo será identificada, por ejemplo, [Ayuda: Obtener deuda del cliente en base a la tasa de actualización y totales adeudados recibidos]
    - El resto de los campos, existirán, si hay algún otro tipo de comentario en la función. En este caso, cada comentario, aparecerá como un dato nuevo, separado por una “,” de otro, si es que hay más de un comentario. 
  

Una vez realizado el proceso mencionado y habiendose generado los archivos correspondientes, se ofrecerá un menú de opciones que permita acceder a las funcionalidades:

  1) Panel de funciones
  2) Consulta de Funciones
  3) Analizador de Reutalizacion de codigo
  4) Arbol de invocacion
  5) Informacion por desarrollador 

### 1. Panel General de Funciones

Mediante esta opción se mostrará por pantalla, una tabla con la siguiente información por columna:
  - Nombre de la Función.Módulo (FUNCION)
  - Cantidad de Parámetros Formales (Parámetros)
  - Cantidad de líneas de código (Líneas)
  - Cantidad de invocaciones a la función (Invocaciones)
  - Cantidad de Puntos de Salida (Returns)
  - Cantidad de if/elif (If/elif)
  - Cantidad de For (for)
  - Cantidad de While (while)
  - Cantidad de Break (Break)
  - Cantidad de Exit (Exit)
  - Cantidad de líneas de comentarios (Coment)
  - Indicador de Descripción Función (Ayuda)
  - Autor/Responsable (Autor) 
  
También genera el archivo “panel_general.csv”, en el cual cada línea del archivo contiene la información descripta en cada uno de los puntos.

### 2. Consulta de Funciones

Muestra una tabla con cada uno de los nombres de las funciones recibidas.

Debajo de la tabla, aparecerá el mensaje “Función: “, a la espera del ingreso de uno de los nombres listados seguido por alguno de los siguientes caracteres:

  - "?" - Indica que se debe mostrar la descripción asociada al uso de la función, los parámetros formales que espera la función, el módulo al que pertenece, y el autor y/o responsable de la función.
  - "#" - Indica que se quiere ver todo lo relativo a la función.

Continua solicitando el ingreso de nombres de funciones, hasta que el usuario sólo de enter.

Si el usuario ingresa “?todo”, se lista la información descripta, pero para cada una de las funciones por pantalla. De igual modo, si ingresa “#todo”.

Si el usuario ingresa “imprimir ?todo”, se envía al archivo "ayuda_funciones.txt" el contenido correspondiente.

### 3. Analizador de Reutilización de Código

Refleja mediante una tabla, quien invoca a quien/es, y quien es invocado por quien/es.

### 4. Árbol de Invocación 

Dibuja un diagrama que gráfica la interacción entre las funciones, indicando quien llama a qué función.

### 5. Información por Desarrollador 

Muestra por pantalla datos sobre la participación de cada uno de los integrantes en el desarrollo de la aplicación. 

También genera la misma salida al archivo “participacion.txt” 

# Consideraciones

Para correr esta aplicación deberá verificar que la ruta provista en "m_cargar_archivos.py" refleje la ruta que esté utilizando actualmente para que pueda ejecutarse la creación de los archivos .csv desde el archivo programas.txt.

Linea 209:
```python
def funciones_por_modulo():
    '''[Autor:Andres Guerrero]
       [Ayuda:estructura que se encarga de cargar y hacer los cortes por rutas de los modulos,
       modulo en el que se trabaja,funcion_analizada] 
    '''
    archivo_fuente = open(r'.\programa_prueba\programas.txt','r')
```



