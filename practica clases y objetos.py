class Personaje:
    def __init__(self, nombre, vida, ataque):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        
personaje1 = Personaje("yasuo", "1500", "hoja al viento")       
personaje2 = Personaje("sion", "3000", "impacto aniquilador")  
personaje3 = Personaje("jhin", "1300", "granada bailarina")  

print ("Nombre = " , personaje1.nombre , " Vida = " , personaje1.vida)
print ("Nombre = " , personaje2.nombre , " Vida = " , personaje2.vida)
print ("Nombre = " , personaje3.nombre , " Vida = " , personaje3.vida)