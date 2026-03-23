"""
PLAN DE TRABAJO
1. Imprimimos un mensaje de bienvenida
2. Leer el nombre de estudiante por consola
3. Verificar que sea un nombre válido
4. Si es válido guardarlo en la lista global
5. Si es inválido, mostrar un mensaje en la consola

Primero lo hacemos en un bloque de código
y luego lo separamos en funciones para mejorar la organización y reutilización del código.

"""
# Declaramos una lista global para almacenar los nombres de los estudiantes
estudiantes = []

# Mostramos un mensaje de bienvenida
print("Bienvenido al sistema de gestión de estudiantes.\n")

# Armamos un bucle infinito para permitir ingresar múltiples estudiantes
while True:
    # Leer nombre del estudiante por consola
    nuevo_estudiante = input("Ingrese el nombre del estudiante: ")

    # Verificar que el nombre sea válido (no esté vacío)
    check_nombre = True if nuevo_estudiante.strip() != "" else False

    # Si el nombre es válido, lo agregamos a la lista global, sino mostramos un mensaje de error
    if check_nombre:
        estudiantes.append(nuevo_estudiante)
        print(f"El estudiante '{nuevo_estudiante}' ha sido agregado a la lista.")
    else:
        print("Nombre inválido. Por favor, ingrese un nombre válido.")  

    # Mostramos la lista de estudiantes actualizada
    print("Lista de estudiantes:")
    for estudiante in estudiantes: 
        print(estudiante)

    # Preguntamos al usuario si desea ingresar otro estudiante o salir del programa
    continuar = input("¿Desea ingresar otro estudiante? (s/n): ")
    if continuar.lower() != "s":
        break