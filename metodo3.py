#automovil 
class automovil:
    def __init__(self, marca, modelo, velocidadActual):
        self.marca = marca
        self.modelo = modelo
        self.velocidadActual = velocidadActual
        
    def acelerar(self, cantidad):
        if cantidad <=0:
            print ("No se puede acelerar")
        else:
            self.velocidadActual += cantidad
            
    def frenar(self, cantidad):
        if cantidad <=0:
            print("No se puede frenar")
        else:
            self.velocidadActual -= cantidad
            
    def mostrarVelocidad(self):
        print(self.velocidadActual)
            
automovil1 = automovil("KIA", "Picanto", 20)
automovil2 = automovil("KIA", "Picy", 40)

automovil1.acelerar (25)
automovil1.acelerar (18)
automovil1.acelerar (10)

automovil1.frenar (50)

automovil1.mostrarVelocidad()


            
               
        