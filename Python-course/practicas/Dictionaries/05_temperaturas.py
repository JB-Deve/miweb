# ejercicio 5

temperaturas = {
    "Lunes": [22, 18, 20],      # mañana, tarde, noche
    "Martes": [24, 21, 19],
    "Miércoles": [23, 20, 18],
    "Jueves": [25, 22, 20],
    "Viernes": [26, 23, 21]
}

# TODO:
# 1. Calcula la temperatura promedio de cada día
def calcular_promedio(temperaturas):
    prom_dias = {}
    for dias, temps in temperaturas.items():
        promedio_temps = sum(temps) / len(temps)
        prom_dias[dias] = promedio_temps
    return prom_dias

promedios = calcular_promedio(temperaturas)
for clave, valor in promedios.items():
    print(f"{clave:<10}: {(valor):.1f}\u00B0C")
    
# ----------------------------------------------------
# ordenar promedio para obtener el mayor y menor en temperatura
def orden_por_temp(prom_dias):
    orden = sorted((values, key) for (key, values) in prom_dias.items())
    orden = list((key, values) for (values, key) in orden)

    return orden

max_min = orden_por_temp(promedios)

# 2. Encuentra el día más caluroso ----------------------------
a, b = max_min[-1]
print(f"\nEl dia mas culoroso es: {a} con {b:.1f}\u00B0C")

# 3. Encuentra el día más frío --------------------------------
c, d = max_min[0]
print(f"El dia mas frio es: {c} con {d:.1f}\u00B0C")

# 4. Calcula el promedio general de toda la semana-------------
def prom_general(promedios):
    return sum(promedios.values()) / len(promedios)    
    
prom_total = prom_general(promedios)
print(f"\nEl promedio semanal es: {prom_total:.1f}\u00B0C"
)
