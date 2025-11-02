###
# 05 - Bucles (while)
# permiten ejecutar un bloque de codigo repetidamente mientras se cumpla la condicion
###
import os
os.system("cls")

# print("\n Bucle while:")

# # Bucle con una simple condicion
# contador = 0

# while contador < 5:
#     print(contador)
#     contador += 1 # es super importante para evitar un bucle infinito

# # utilizando la palabra break, para romper el bucle
# print("\n Bucle while con break")
# contador = 0
# while True:
#     print(contador)
#     contador += 1
#     if contador == 5:
#         break # sale del bucle

# # continue, lo que hace es saltar esa iteracion en concreto
# # y continuar con el bucle
# print("\n Bucle con continue")
# contador = 0
# while contador < 10:
#     contador += 1

#     if contador % 2 == 0:
#         continue # continua con la iteracion: es igual a 0 (si go up) (no print)

#     print(contador)

# # else, esta condicion cuando se ejecuta
# print("\n Bucle while con else")
# contador = 0
# while contador < 5:
#     print(contador)
#     contador += 1
#     break # evita la ejecucion de todo lo que esta abajo
# else:
#     print("El bucle ha terminado")

# # pedirle al usuario un numero que tiene
# # que ser positivo si no, no le dejamos en paz

# numero = -1
# while numero < 0:
#     try:
#         numero = int(input("Escribe un numero positivo: "))
#         if numero < 0:
#             print("El numero debe ser positivo. Intentalo de nuevo!!")
#     except ValueError:
#         print("Lo que introduces, debe ser un numero, que si no peta!")

# print(f"El numero que has introducido es {numero}")
# muy util try y except ValueError:

###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
# print("\nEjercicio 1:")
# numero = 10
# while numero >= 1:
#     print(numero)
#     numero -= 1

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")

# numero = 1
# suma_pares = 0
# while numero <= 20:
#     if numero % 2 == 0:
#         suma_pares += numero
#     numero += 1

# print(f"La suma de los números pares hasta 20 es: {suma_pares}")
# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")
# numero = int(input("Introduce un número entero positivo: "))
# factorial = 1
# contador = 1

# while contador <= numero:
#     factorial *= contador
#     contador += 1

# print(f"El factorial de {numero} es: {factorial}")

# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
# print("\nEjercicio 4:")
# contrasena = ""
# while len(contrasena) < 8:
#     contrasena = input("Introduce una contraseña (al menos 8 caracteres): ")
#     if len(contrasena) < 8:
#         print("La contraseña debe tener al menos 8 caracteres. Inténtalo de nuevo.")

# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
# print("\nEjercicio 5:")
# numero = int(input("Introduce un número: "))
# multiplicador = 1

# while multiplicador <= 10:
#     resultado = numero * multiplicador
#     print(f"{numero} x {multiplicador} = {resultado}")
#     multiplicador += 1
# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6:")
