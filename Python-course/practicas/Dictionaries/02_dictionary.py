# TODO:
# 1. Imprime cada estudiante con su nota
# 2. Calcula el promedio de todas las notas
# 3. Encuentra quién tiene la nota más alta

notas = {
    "Ana": 85,
    "Carlos": 92,
    "Diana": 78,
    "Eduardo": 88
}

# 1. IMPRIMIR
# este metodo consume un poco mas de tiempo al ejecutarse
    # def lista_estudiantes(notas):
    #     for estudiante in notas:
    #         nota = notas[estudiante] # cada que se pide itera todo
    #         print(f"{estudiante}: {nota}")
    # lista_estudiantes(notas)

# metodo mas directo variabres para clave, valor.
def mostrar_notas(notas):
    for nombre, nota in notas.items(): # .items() da pares (clave, valor) 'tupla'
        print(f"{nombre} obtuvo: {nota}") # f-string, mas moderno

# 2. PROMEDIO
def calcular_promedio(notas):
    return sum(notas.values()) / len(notas) # suma todos los valores

# 3. MAXIMO
def mejor_estudiante(notas):
    nomber_max = max(notas, key=notas.get) # encuentra la clave con valor maximo
    return nomber_max, notas[nomber_max]

# -------------------------------------------------------------------------------
print("=== NOTAS ===")
mostrar_notas(notas)

print("\n=== PROMEDIO ===")
print(F"Promedio: {calcular_promedio(notas):.2f}") # .2f dos decimales


print("\n=== MEJOR ESTUDIANTE ===")
nombre, nota = mejor_estudiante(notas)
print(f"{nombre} tiene la nota mas alta ({notas})")
