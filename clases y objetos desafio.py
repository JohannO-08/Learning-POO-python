class estudiante:
    def __init__(self, nombre, semestre, carrera, promedio):
        self.nombre = nombre
        self.semestre = semestre
        self.carrera = carrera
        self.promedio = promedio 
        
estudiante1 = estudiante("juan", "5to", "informatica", "9.5")
estudiante2 = estudiante("maria", "3ro", "medicina", "8.7")
estudiante3 = estudiante("pedro", "7mo", "derecho", "9.0")
estudiante4 = estudiante("lucia", "2do", "arquitectura", "8.2")
estudiante5 = estudiante("carlos", "4to", "ingenieria", "9.3")

print ("Nombre = " , estudiante1.nombre , " Promedio = ", estudiante1.promedio)
print ("Nombre = " , estudiante2.nombre , " Promedio = ", estudiante2.promedio)
print ("Nombre = " , estudiante3.nombre , " Promedio = ", estudiante3.promedio)
print ("Nombre = " , estudiante4.nombre , " Promedio = ", estudiante4.promedio)
print ("Nombre = " , estudiante5.nombre , " Promedio = ", estudiante5.promedio)