# TODO:
# 1. Procesa la lista votos_recibidos y actualiza el diccionario
#    ("A" → "Candidato A", "B" → "Candidato B", etc.)
# 2. Ordena los candidatos por número de votos (mayor a menor)
# 3. Imprime los resultados
# 4. Declara al ganador

# import os
# os.system("cls")

votos = {
    "Candidato A": 0,
    "Candidato B": 0,
    "Candidato C": 0
}

# Simula votos
votos_recibidos = ["A", "B", "A", "C", "A", "B", "C", "A", "A"]

# 1 -----------------------------------
for voto in votos_recibidos:
    if voto == "A":
        votos["Candidato A"] += 1
    elif voto == "B":
        votos["Candidato B"] += 1
    elif voto == "C":
        votos["Candidato C"] += 1
print(votos)
# 2------------------------------------------
# sorted() ordena de forma accendente
# items() encapsula la 'clave, valor'
# key=lambda x: x[1] escoge 'clave=0' o 'valor=1' para el orden
# votos_ordenados = sorted(votos.items(), key=lambda x: x[1], reverse=True)
# print(votos_ordenados)
# ordenamos por value
votos_ordenados = sorted((value, key) for (key, value) in votos.items())
# intercambiamos posciciones de los items
votos_ordenados = list((key, value) for (value, key) in votos_ordenados)
# invertimos el orden
votos_ordenados = votos_ordenados[::-1]

print(votos_ordenados)

# 3 -----------------------------------------
for candidato, num_votos in votos_ordenados:
    print(f"{candidato}: {num_votos} votos")

# 4 -----------------------------------------
# simplemente imprimimos una parte de la lista en este caso '0'
ganador, votos_ganador = votos_ordenados[0]
print(f"{ganador} con {votos_ganador}")



"""
**Ejemplo de salida:**

Candidato A: 5 votos
Candidato B: 2 votos
Candidato C: 2 votos
¡Ganador: Candidato A con 5 votos!
"""
