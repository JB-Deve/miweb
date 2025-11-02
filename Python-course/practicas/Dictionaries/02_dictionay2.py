###
# Ejercicios guiados
###
import os
os.system("cls")

notas = {
    "Ana": 85,
    "Carlos": 92,
    "Diana": 78,
    "Eduardo": 88
}

# TODO:
# 1. Imprime cada estudiante con su nota
def lista_estudiantes(notas):
    # .items() muy importante para cuando se llame por clave, valor
    for nombre, nota in notas.items():
        print(f"{nombre}: {nota}")

# 2. Calcula el promedio de todas las notas
def promedio_notas(notas):
    total = 0
    # contador reemplaza len()
    #contador = 0
    for nota in notas.values():
        total += nota
        #contador += 1
    print(f"\npromedio: {total / len(notas)}")

# 3. Encuentra quién tiene la nota más alta
def maxima_nota(notas):
    # iterator = iter(notas.items())
    # maxima_clave, maxima_nota = next(iterator)
    maxima_clave = None
    maxima_nota = 0
    # for std, nota in iterator():
    for std, nota in notas.items():
        if nota > maxima_nota:
            maxima_clave = std
            maxima_nota = nota
    print(f"\n{maxima_clave} tiene el puntaje mayor ({maxima_nota})")

# ejecutables
lista_estudiantes(notas)
promedio_notas(notas)
maxima_nota(notas)

# cuando usamos inputs() tenemos que convertir los numbers en int() or float()
