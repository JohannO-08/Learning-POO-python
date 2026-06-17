class mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre   
        self.especie = especie
        self.edad = edad
        
mascota1 = mascota("Firulais", "Perro", "5")
mascota2 = mascota("Michi", "Gato", "3")
mascota3 = mascota("rabbit", "conejo", "1")

print ("Nombre = " , mascota1.nombre , " Especie = " , mascota1.especie, " Edad = ", mascota1.edad)
print ("Nombre = " , mascota2.nombre , " Especie = " , mascota2.especie, " Edad = ", mascota2.edad)
print ("Nombre = " , mascota3.nombre , " Especie = " , mascota3.especie, " Edad = ", mascota3.edad)