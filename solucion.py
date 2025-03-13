

def obtener_estudiantes():
    # Inicialización de variables
    reporte_estudiantes = "\nListado de Estudiantes\n"  # Cadena para almacenar la lista de jugadores
    contador = 0  # Contador para numeración de jugadores
    bandera = True  # Variable de control para el ciclo while
    

    elementos = input("Ingrese el número de estudiantes a generar: ")  # Se solicita la edad del jugador
    elementos = int(elementos)  # Conversión a entero
    contador = 1
    # Uso de listas para almacenar datos de los jugadores y sus edades
    lista_estudiantes = []  # Lista para almacenar la información de los jugadores (nombre, posición, edad, estatura)
    
    # Bucle para ingreso de datos
    while contador <= elementos:
        print("\nIngrese la información del estudiante:")
        nombre = input("Nombre del estudiante: ")  # Se solicita el nombre del jugador
        apellido = input("Apellidos del estudiante: ")  # Se solicita la posición del jugador
        correo = input("Correo del estudiante: ")  # Se solicita la posición del jugador
        edad = input("Edad del estudiante: ")  # Se solicita la edad del jugador
        edad = int(edad)  # Conversión a entero
    
        # Uso de listas para almacenar la información de cada jugador
        lista = [nombre, apellido, correo, edad]  # Se almacena la información en una lista
        lista_estudiantes.append(lista)  # Se agrega la lista del jugador a la lista principal
    
        contador = contador + 1  # Se incrementa el contador para numerar a los jugadores
    
    # Construcción del reporte de jugadores a partir de la lista de jugadores
    for i in lista_estudiantes:
        reporte_estudiantes = f"{reporte_estudiantes}{i[0]} {i[1]} -correo:{i[2]}-, edad:{i[3]}\n"
    
    
    # Impresión del reporte final
    print(reporte_estudiantes)  # Se imprime el listado de jugadores


def obtener_docentes():
    # Inicialización de variables
    reporte = "\nListado de Docentes\n"  # Cadena para almacenar la lista de jugadores
    contador = 0  # Contador para numeración de jugadores
    bandera = True  # Variable de control para el ciclo while
    

    elementos = input("Ingrese el número de docentes a generar: ")  # Se solicita la edad del jugador
    elementos = int(elementos)  # Conversión a entero
    contador = 1
    # Uso de listas para almacenar datos de los jugadores y sus edades
    lista_docentes = []  # Lista para almacenar la información de los jugadores (nombre, posición, edad, estatura)
    
    # Bucle para ingreso de datos
    while contador <= elementos:
        print("\nIngrese la información del docente:")
        nombre = input("Nombre del docente: ")  # Se solicita el nombre del jugador
        apellido = input("Apellidos del docente: ")  # Se solicita la posición del jugador
        ciudad = input("Ciudad de residencia: ")  # Se solicita la edad del jugador
    
        # Uso de listas para almacenar la información de cada jugador
        lista = [nombre, apellido, ciudad]  # Se almacena la información en una lista
        lista_docentes.append(lista)  # Se agrega la lista del jugador a la lista principal
    
        contador = contador + 1  # Se incrementa el contador para numerar a los jugadores
    
    # Construcción del reporte de jugadores a partir de la lista de jugadores
    for i in lista_docentes:
        reporte = f"{reporte}{i[0]} {i[1]} -ciudad de residencia:{i[2]}\n"
    
    
    # Impresión del reporte final
    print(reporte)  # Se imprime el listado de jugadores



if __name__ == "__main__":
    
    mensaje = "Menú\nIngrese 1 para generar estudiantes; 2 para generar docentes: "
    opcion = input(mensaje)
    opcion = int(opcion)
    if opcion == 1:
        obtener_estudiantes()
    else:
        if opcion == 2:
            obtener_docentes()
        else:
            print("Opción correcto")
