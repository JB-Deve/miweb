# Pedir algo

import os
os.system("cls")

###
# inventario - almacen
###

inventario = {
    "manzanas": 50,
    "naranjas": 30,
    "plátanos": 45,
    "uvas": 20,
    "fresas": 35,
    "peras": 15,
    "anana": 21
}

# TODO: # pylint: disable=W0511
# 1. Crea una función que imprima cada producto y su cantidad
# 2. Crea una función que devuelva el total de productos en stock
# 3. Crea una función que encuentre el producto con menos stock

# 1. Iprimir en pantalla el inventario
# def productos_list(inventariov):

#     for producto in inventariov:
#         cantidad = inventariov[producto]
#         print(f"{producto}: {cantidad}")

# productos_list(inventario)
# print()

# # Suma de productos
# def productos_total(inventarioa):
#     totalx = 0
#     for cantidad in inventarioa:
#         cantidad = inventarioa[cantidad]
#         totalx += cantidad

#     return totalx

# total = productos_total(inventario)
# print(f"Total productos en almacen: {total}\n")

# Ordenar, accendente por 'clave'
def ordenar_lista(inventarion):
#     for producto in inventario:
#         productos = inventario[producto]
#         productos = sorted(inventario.items())
#         # Orden decendente por 'clave'
#         productos = productos[::-1]
#         #a, b = productos
#         return productos

# ordenar_lista(inventario)

# Orden, accendente por 'valor'
    for producto in inventarion.values():
        #productos = inventarion[producto]
        productos = sorted((values, key) for (key, values) in inventarion.items())
        productos = list((key, values) for (values, key) in productos)
        productos = productos[::-1]

    return productos
muestra = ordenar_lista(inventario)
print(muestra)
#ordenar_lista(inventario)

# def lista_orden(ordenar_listax):
#     for candidato, num_votos in ordenar_listax:
#         print(f"{candidato}: {num_votos} votos")

# lista_orden(ordenar_lista(inventario))

# # -----------------------------------
# # productos low stock

# def producto_bajo (inventariox):
#     minimo_producto = None
#     minimo_cantidad = float("inf")

#     for productos in inventariox:
#         cantidad = inventariox[productos]

#         if cantidad < minimo_cantidad:
#             minimo_producto = productos
#             minimo_cantidad = cantidad

#     return minimo_producto, minimo_cantidad

# clave, valor = producto_bajo(inventario)
# print(f"\nLow stock de -> {clave}: ({valor})")
