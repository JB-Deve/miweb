# TODO:
# 1. Crea un diccionario que cuente cuántas veces aparece cada palabra
# 2. Imprime el diccionario
# 3. Encuentra la palabra más repetida

texto = "python es genial python es poderoso python es fácil"

palabras = texto.split() # comvierte el string en listas
#print(palabras)

contador = {} # crea una libreria vacia

for palabra in palabras:
    if palabra in contador:
        contador[palabra] = contador[palabra] + 1 
    else:
        contador[palabra] = 1

print(contador)

palabra_mas_repetida = None
max_repeticiones = 0

for palabra in contador:
    repeticiones = contador[palabra]

    if repeticiones > max_repeticiones:
        max_repeticiones = repeticiones
        palabra_mas_repetida = palabra

print("Palabras mas repetidas:", palabra_mas_repetida, "(", max_repeticiones, "veces )")
