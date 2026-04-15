# ============================================================
# OPERACIONES CRUD BÁSICAS (con diccionarios)
# ============================================================

# CRUD = Create, Read, Update, Delete
# Son las 4 operaciones fundamentales sobre cualquier conjunto de datos.

# Declaramos e incializamos una lista global productos
# Donde cadad producto posee la siguiente estructura:
# Atributos: id_producto | categoria | nombre | precio_unitario

productos = [
    {
        "id_producto": 1,
        "categoria": "Escritura",
        "nombre": "Lápiz negro HB",
        "precio_unitario": 350,
    },
    {
        "id_producto": 2,
        "categoria": "Escritura",
        "nombre": "Bolígrafo azul",
        "precio_unitario": 500,
    },
]

# Visualizamos la lista global productos inicializada 
# print(productos)


# CREATE (Alta de producto) 
"""
1. Crear un nuevo producto (producto_3). 
2. Agregarlo a la lista productos utilizando el método append(). 
3. Mostrar un mensaje confirmando la operación. 
"""


# READ (Búsqueda de producto por id) 
"""
1. Buscar un producto a partir de su id_producto. 
2. Utilizar un for para recorrer la lista. 
3. Guardar el resultado en una variable. 
4. Mostrar el producto encontrado. 
"""


# UPDATE (Modificación de un producto según su id) 
"""
1. Recorrer la lista de productos. 
2. Identificar un producto por su id. 
3. Modificar su precio_unitario. 
4. Mostrar el producto actualizado. 
"""



# DELETE (Eliminación de un producto según su id) 
"""
1. Buscar un producto por su id_producto. 
2. Eliminarlo de la lista utilizando remove(). 
3. Mostrar la lista final de productos. 
"""

