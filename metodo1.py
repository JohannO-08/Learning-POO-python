#etso es una practica de metodos 
class Persona:
    def __init__(self, nombre, edad, altura):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
    def saludar(self):
        print("Hola, mi nombre es " + self.nombre)
persona1 = Persona("Juan", 30, 1.75)
persona2 = Persona("Maria", 25, 1.65)

if persona1.edad > 18:
    print(persona1.nombre + " es mayor de edad.")

if persona2.edad > 18:
    print(persona2.nombre + " es mayor de edad.")

print(persona1.saludar())
print(persona2.saludar())
print(persona1.nombre + " tiene " + str(persona1.edad) + " años y mide " + str(persona1.altura) + " metros.")
print(persona2.nombre + " tiene " + str(persona2.edad) + " años y mide " + str(persona2.altura) + " metros.")