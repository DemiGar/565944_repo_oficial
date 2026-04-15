"""
CONSIGNA:
Se nos solicita crear un bloque de código que realice lo siguiente:

1. Imprimir un mensaje de bienvenida
2. Leer el nombre de un estudiante por consola
3. Verificar que sea un nombre válido
4. Si es válido guardarlo en la lista global
5. Si es inválido, mostrar un mensaje en la consola
6. A fin de poder repetir el flujo, incluir el código dentro de un bucle while
"""


estudiantes = []

while True:
    print("BIENVENIDO...")
    nombre = input("ingrese su nombre: ")

    if nombre.strip() != "":
        print("TRUE")
        estudiantes.append(nombre)
    else:
        print("Nombre no puede quedar en blanco")


    flag = input("Ingrese 's' para terminar")
    if flag == "s":
        break

