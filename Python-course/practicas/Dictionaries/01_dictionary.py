###
# inventario - almacen
###

inventario = {
    "manzanas": 50,
    "naranjas": 30,
    "plátanos": 45,
    "uvas": 20
}

# TODO:
# 1. Crea una función que imprima cada producto y su cantidad
# 2. Crea una función que devuelva el total de productos en stock
# 3. Crea una función que encuentre el producto con menos stock

def mostrar_inventario(inventario):
    for producto in inventario:
        cantidad = inventario[producto]
        print(producto + ":", cantidad, "unidades")

mostrar_inventario(inventario)

# 2 -----------------------------------------------

def calcular_total(invetario):
    total = 0

    for producto in inventario:
        cantatidad = invetario[producto]
        total = total + cantatidad

    return total

# metodo mas directo
# def calcular_total(inventario):
#     return sum(inventario.values())

total_productos = calcular_total(inventario)
print("Tienes una cantidad total de: ", total_productos, "productos.")

# 3 ------------------------------------------------

def producto_minimo(inventario):
    producto_menor = None
    cantidad_menor = float('inf') # representa un numero infinito 

    # leemos nuestro dict
    for producto in inventario:
        cantidad = inventario[producto]

        # comparamos si nuestro pdt(cantidad) es menor a infinito
        if cantidad < cantidad_menor:
            # comvierte none en clave que es key=procucto
            producto_menor = producto
            # comvierte infinito en en valor de nuestro pdt(seleccionado)
            cantidad_menor = cantidad           
            # inicia el loop hasta que no queden productos

    # salvamos los valores
    return producto_menor, cantidad_menor

# version mas corta
# def producto_minimo(inventario):
#     producto_menor = min(inventario, key=inventario.get)
#     return producto_menor, inventario[producto_menor]

# creamos key, value y le pasamos nuestro dict como valor
nombre, cantidad = producto_minimo(inventario)
# imprimimos key=nombre, value=cantidad
print("Producto con menos stock: ", nombre, "(", cantidad, ")")
