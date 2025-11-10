#
import os
os.system("cls")

productos = {
    "galletas": 4,
    "jugo": 6,
    "queso": 10
}

carrito = ["galletas", "jugo", "jugo", "queso"]

# TODO: Calcula el total (debería ser 26)

total = 0
for item in carrito:
    precio = productos[item]
    total += precio


#for item in carrito:
contador = {}
for items in carrito:
    if items in contador:
        contador[items] += 1
    else:
        contador[items] = 1
print(contador)

for a, b in contador.items():
    print(b, a)
# -------

print(f"Total: ${total}")
descuento = total * 0.10
print("descuento de: ", descuento)
if total > 20:
    print(total - descuento)
else:
    print(total)