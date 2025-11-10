# first

class Personas:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

    def presentarse(self):
        print(f"Hola me llamo {self.nombre}, tengo {self.edad} y vivo en {self.ciudad}.")

    def a_nacimiento(self, a_actual):
        a_nacimiento = a_actual - self.edad
        return a_nacimiento
    
    def es_mayor(self):
        if self.edad >= 18:
            return "Soy mayor de edad."
        else:
            return "Aun soy menor de edad."



p1 = Personas("Jota", 21, "Valencia")
p2 = Personas("Carlos", 11, "Valencia")
p3 = Personas("Paco", 31, "Mallorca")
p4 = Personas("Nox", 29, "Londres")
# crear lista con los objetos creados
Personas = [p1, p2, p3, p4]

for p in Personas:
    p.presentarse()
    print(p.es_mayor())
    print(p.a_nacimiento(2025))
    print("-" * 30)