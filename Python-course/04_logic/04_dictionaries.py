###
# 04 - Dictionaries
# Los diccionarios son colecciones de pares clave-valor.
# Sirven para almacenar datos relacionados.
###

# ejemplo tipico de diccionario
persona = {
    "nombre": "Jota",
    "edad": 26,
    "es_estudiante": True,
    "clasificaciones": [7, 8, 9],
    "sociales":{
        "twiter": "@jota",
        "instagram": "@jota"
    }
}

# Para acceder a los valores
print(persona["nombre"])
print(persona["clasificaciones"][2]) # accedemos al sub-valor de poscicion
print(persona["sociales"]["twiter"]) # accedemos al sub-valor

# cambiar valores al acceder
persona["nombre"] = "nox"
persona["clasificaciones"][2] = 10

# eliminar completamente una propiedad
del persona["edad"]
#print(persona)

es_estudiante = persona.pop("es_estudiante")
print(f"es_estudiante: {es_estudiante}")
print(persona)

# sobreescribir un diccionario con otro diccionario
a = { "name": "Jota", "age": 25 }
b = { "name": "Nox", "es_estudiante": True }

a.update(b) # los valores de B prevalecen y agrega lo que no tenga en B
print(a)

# comprobar si existe una propiedad
print("name" in persona) # False
print("nombre" in persona) # Trues

# obtener todas las claves
print("\nkeys:")
print(persona.keys())

# obtener todas los valores
print("\nvalues:")
print(persona.values())

# obtener tanto clave como valor
print("\nitems:")
print(persona.items())

for key, value in persona.items():
    print(f"{key}: {value}")
