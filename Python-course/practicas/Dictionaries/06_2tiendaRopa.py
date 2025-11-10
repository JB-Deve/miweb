# Tienda de ropa

# TODO:
# 1. Calcula el subtotal
# 2. Cuenta cuántas prendas de cada tipo se compraron
# 3. Aplica descuentos por cantidad:
#    - 2 del mismo artículo: 5% descuento
#    - 3 o más del mismo: 10% descuento
# 4. Calcula el total con descuentos
# 5. Si el total supera $100, envío gratis (ahorra $10)

import os
os.system("cls")

ropa = {
    "camisa": 25,
    "pantalon": 40,
    "zapatos": 60,
    "gorra": 15,
    "calcetines": 5
}

compras = ["camisa", "pantalon", "calcetines", "calcetines", "zapatos"]

print("=== TICKET DE COMPRA ===\n")
# =======================
# 1. Calcula el subtotal
# =======================
subtotal = 0
for item in compras:
    price = ropa[item]
    subtotal += price
    print(f"{item}: ${price}")

print(f"\nSubtotal: ${subtotal}")
# ====================================================
# 2. Cuenta cuántas prendas de cada tipo se compraron
# ====================================================
contador = {}
for elemento in compras:
    if elemento in contador:
        contador[elemento] += 1
    else: # se ejecuta primero agregando los values a 1, luego if:
        contador[elemento] = 1

print("\n=== UNIDADES POR ARTICULO ===")
for articulo, cantidad in contador.items():
    print(f"{articulo}: {cantidad} unidad(es)")

# =======================================
# 3 y 4. Aplica descuentos por cantidad
# =======================================
total_descuentos = 0
print("\n=== DESCUENTOS APLICADOS ===")
for articulo, cantidad in contador.items():
    precio_unitario = ropa[articulo]
    
    if cantidad == 2:
        # 5% de descuento al articulo
        descuento = precio_unitario * cantidad * 0.05 # 5/100
        total_descuentos += descuento 
        print(f"{articulo} (x{cantidad}: -${descuento:.2f} (5% desc)")
    elif cantidad >= 3:
        # 10% de descuento al articulo
        descuento = precio_unitario * cantidad * 0.10 # 10/100
        total_descuentos += descuento
        print(f"{articulo} (x{cantidad}): -${descuento:.2f}")

if total_descuentos == 0:
    print("No hay descuentos aplicables")

# Total despues de descuentos por cantidad
total = subtotal - total_descuentos
print(f"\nTotal con descuentos: ${total:.2f}")

# =======================================
# 5. Envio gratis si supera $100
# =======================================
if total > 100:
    print(f"Envio gratis (ahorro: $10)")
    total = total - 10
    print(f"\nTOTAL FINAL: ${total:.2f}")
else:
    print(f"TOTAL FINAL: ${total}")

# ------------------------------------------------------

