# tienda

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def subtotal(self):
        return self.precio * self.cantidad
    
    def aplicar_descuento(self):
        # Regla: 2 iguales 5% descuento
        if self.cantidad == 2:
            porcentaje_descuento = 0.05
            descuento_total = self.subtotal() * porcentaje_descuento
            total = self.subtotal() - descuento_total

            print(f"Descuento: {porcentaje_descuento * 100:.0f}%")
            print(f"Descuento aplicado: -{descuento_total:.2f}")
        else:
            porcentaje_descuento = 0.0
            total = self.subtotal()
            print(f"No descuentos aplicados")
        return total
        # if self.cantidad ==2:
        #     return self.subtotal() * 0.95
        # else:
        #     return self.subtotal()

    def mostrar_info(self):
        print(f"Producto: {self.nombre}")
        print(f"Cantidad: {self.cantidad}")
        print(f"Subtotal: {self.subtotal():.2f}")

        total = self.aplicar_descuento()
        print(f"TOTAL: {total:.2f}")
        #print(f"Total con descuento: ${self.aplicar_descuento():.2f}")
        print("-" * 30)

p1 = Producto("Polo", 50, 2)
p2 = Producto("Zapas", 80, 1)

p1.mostrar_info()
p2.mostrar_info()