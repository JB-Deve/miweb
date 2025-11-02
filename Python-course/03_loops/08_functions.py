###
# 04 - functions
# Bloque de codigo reutilizables y parametrizables para hacer tareas especificas
###
""" Definicion de una funcion

def nombre_de _la_funcion(parametro1, parametro2, ...):
    # docstring
    # cuerpo de la funcion
    return valor_de_retorno # opcional
"""
import os
os.system("clear")

# ejemplo de una funcion para imprimir algo en consola
# def saludar():
#     print("Hola!")

# saludar()

# #Ejemplo de un funcion con parametro
# def saludar_a(nombre):
#     print(f"Hola {nombre}!")

# saludar_a("pepito")
# saludar_a("paco")
# saludar_a("pancho")

# # Funciones con mas parametro
# def sumar(a, b):
#     suma = a + b
#     return suma

# result = sumar(2, 3)
# print(result)

# # Documentar las functions con docstring
# def restar(a, b):
#     """Resta dos numeros y devuelve el resultado""" # buen metodo para dejar saber lo que hacemos
#     return a - b

# print(restar(7, 9))
# #print(restar.__doc__) # para ver el docstring ingresado
# #help(restar)

# #parametros por defecto
# def multiplicar(a, b = 2):
#     return a * b

# print(multiplicar(5))
# print(multiplicar(2, 3))

# Argumentos por posicion
def describir_persona(nombre, edad, sexo):
    print(f"Soy {nombre}, tengo {edad} y me considero {sexo}.")

describir_persona("Pepe", 18, "boy")
describir_persona(18, "boy", "pepe") # el orden importa
describir_persona(edad=18, sexo="boy", nombre="Pepe") # si lo pasamos con el nombre del parametro NO importa el orden

# Argumentos de longitud de variables (+args)
def sumar_numeros(*args):
    suma = 0
    for numero in args:
        suma += numero
    return suma

print(sumar_numeros(1, 2, 3, 4, 5))
print(sumar_numeros(1, 2))
print(sumar_numeros(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# Argumentos de clave-valor variable (**kwargs):
def mostrar_informacion_de(**kwargs):
    """ puedo agregar variable y valor al mismo tiempo"""
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_informacion_de(nombre="pepe", edad=25, sexo="gato")
mostrar_informacion_de(nombre="paco", edad=21, country="Spain")
mostrar_informacion_de(nick="Nox", es_sub=True, is_rich=True)
mostrar_informacion_de(super_name="hero", es_modo=True, gatos=40)

# Ejercicios
# Volver a los ejercicios anteriores
# y convertirlos en funciones
# e intentar utilizar todos los casos y conceptos
# que hemos visto hasta ahora
