# analisis de examen

respuestas_estudiantes = {
    "Ana": ['A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E'],
    "Bob": ['A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E'],
    "Carlos": ['B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E', 'A'],
    "Diana": ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A']
}

respuestas_correctas = ['A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E']

# TODO:
# 1. Calcula la calificación de cada estudiante (0-100%)
# 2. Asigna letras: A (90-100%), B (80-89%), C (70-79%), D (60-69%), F (<60%)
# 3. Ordena estudiantes por calificación
# 4. Encuentra qué pregunta fue la más difícil (más errores)
# 5. Muestra estadísticas: promedio del grupo, mejor y peor estudiante

"""
**Ejemplo de salida:**

=== CALIFICACIONES ===
Ana: 100% - Letra: A
Bob: 100% - Letra: A
Carlos: 20% - Letra: F
Diana: 10% - Letra: F

=== ESTADÍSTICAS ===
Promedio del grupo: 57.5%
Mejor estudiante: Ana (100%)
Peor estudiante: Diana (10%)
Pregunta más difícil: Pregunta 5 (50% de errores)
"""
