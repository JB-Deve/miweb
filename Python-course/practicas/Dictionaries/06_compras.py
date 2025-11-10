# 06 - carrito de compra

productos = {
    "laptop": 800,
    "mouse": 25,
    "teclado": 50,
    "monitor": 300
}

carrito = ["laptop", "mouse", "teclado", "mouse"]

# TODO:
# 1. Calcula el total a pagar
def calcular_total(carrito, productos):
    total = 0
    for item in carrito:
        precio = productos[item]
        total += precio
    return total
#print(f"Total: {suma}\n")

# 2. Muestra cada producto en el carrito con su precio
def motrar_carrito(carrito, productos):
    for item in carrito:
        precio = productos[item]
        print(f"{item:<8}: ${precio:>8.2f}")

# 3. Cuenta cuántas unidades de cada producto hay
def contador_unidades(carrito):
    contador = {}
    for item in carrito:
        if item in contador:
            contador[item] += 1
        else:
            contador[item] = 1
    return contador
    
# 4. Aplica un descuento del 10% si el total supera $500 -------
def aplicar_descuento(subtotal): 
    if  subtotal > 500:
        text = "TOTAL"
        descuento = subtotal * 0.10 # 10/100 = 0.10
        total_final = subtotal - descuento
        return descuento, total_final
    else:
        return 0, subtotal
    
# 5 callers --------------------------------------
# mostrar carrito
motrar_carrito(carrito, productos)
# calcular subtotal
subtotal = calcular_total(carrito, productos)
print(f"Subtotal: ${subtotal:>8.2f}")

# contar unidades
unidades = contador_unidades(carrito)
for producto, cantidad in unidades.items():
    print(f"{producto}: {cantidad} unidad(es)")

# aplicar descuento
descuento, total_final = aplicar_descuento(subtotal)
if descuento > 0:
    print(f"\nDescuento (10%): ${descuento:>8.2f}")
    print(f"\nTotal a pagar  : ${total_final:>8.2f}")
else:
    print(f"\nTotal a pagar: ${descuento:>8.2f}")



"""
**Ejemplo de salida:**

laptop: $800.00
mouse: $25.00
teclado: $50.00
mouse: $25.00
Subtotal: $900.00
Descuento (10%): $90.00
Total a pagar: $810.00
"""