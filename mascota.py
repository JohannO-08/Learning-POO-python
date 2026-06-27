class mascota:
    def __init__ (self, nombre, especie, hambre):
        self.nombre = nombre
        self.especie = especie
        self.hambre = hambre
    
    def alimentar (self, cantidad):
      
        if cantidad > self.hambre:
            print("No se pouede realizar la opracion")
        else: 
            self.hambre -= cantidad

        
    def jugar (self, cantidad):
    
        if self.hambre + cantidad > 100:
            print("El hambre de tu mascota no puede superar el numero 100")
        else:
              self.hambre += cantidad
    
    def mostrar_estado (self):
        if self.hambre >= 67 and self.hambre <= 100:
            print("Tu mascota tiene mucha hambre")
        elif self.hambre >= 34 and self.hambre <= 66:
            print("Tu mascota tiene un hambre moderada") 
        elif self.hambre >= 0 and self.hambre <= 33:
            print("Tu mascota tiene poca hambre")  

           
mascota1 = mascota("luna", "Perro", 50 )

mascota1.alimentar (50)
mascota1.jugar(60)
mascota1.alimentar(200)
mascota1.mostrar_estado()
        
        

    