# Basico Clases

# class Perro:
#     def __init__(self, nombre, raza, edad):
#         self.nombre = nombre
#         self.raza = raza
#         self.edad = edad
    
#     def ladrar(self):
#         print(f"Guau guau!!")

#     def presentarse(self):
#         print(f"Soy {self.nombre}, un {self.raza} de {self.edad} anos")

# perro = Perro("Max", "Buldog", 7)
# perro.presentarse()
# perro.ladrar()
# print("-" * 30)

####
# EJERCICIO 2: Clase CuentaBancaria 💰
###

#Crea una clase CuentaBancaria con:
# class CuentaBancaria:
#     # Atributo: saldo (inicia en 0)
#     def __init__(self, nombre, saldo=0):
#         self.nombre = nombre
#         self.saldo = saldo


# # Método depositar(cantidad): suma dinero al saldo
#     def depositar(self, cantidad):
#         self.saldo += cantidad
#         return f"Ingresaste: ${cantidad:.2f}"
    
# # Método retirar(cantidad): resta dinero si hay suficiente
#     def retirar(self, cantidad):
#         if self.saldo >= cantidad:
#             self.saldo -= cantidad
#             return f"Retiraste: ${cantidad:.2f}"    

#         else:
#             return f"Insuficientes fondos"
# # Método ver_saldo(): retorna el saldo actual 
#     def ver_saldo(self):
#         return f"Hola {self.nombre}, tu saldo es de : ${self.saldo:.2f}"
    
# cuenta1 = CuentaBancaria("Jota")
# print(cuenta1.depositar(230))
# print(cuenta1.ver_saldo())
# print(cuenta1.retirar(100))
# print(cuenta1.ver_saldo())
# print(cuenta1.retirar(135))

###
# EJERCICIO 3: Clase Rectangulo 📐
###

""" EJERCICIO 3: Clase Rectangulo 📐
Crea una clase Rectangulo con:

Atributos: ancho, alto
Método calcular_area(): retorna ancho x alto
Método calcular_perimetro(): retorna 2 x (ancho + alto) """

class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        return self.alto * self.ancho
    
    def calcular_perimetro(self):
        return 2 * (self.ancho + self.alto)
    
    def es_cuadraro(self):
        return self.ancho == self.alto
    
    def escalar(self, factor=1):
        self.ancho *= factor
        self.alto *= factor
        #return self.ancho, self.alto
    
rectagulo = Rectangulo(5, 5)
print(f"El area es: {rectagulo.calcular_area()}")
print(f"El perimetro es: {rectagulo.calcular_perimetro()}")
print(f"Es un cuadrado? {rectagulo.es_cuadraro()}")

rectagulo.escalar(2)
print(rectagulo.calcular_area())