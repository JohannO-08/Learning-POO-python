class carro:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        
carro1 = carro("Toyota", "Corolla", "Rojo")
carro2 = carro("Chevrolet", "Camaro", "Azul")

print("Marca = ", carro1.marca, "Modelo =", carro1.modelo, " Color =", carro1.color)
print("Marca = ", carro2.marca, "Modelo =", carro2.modelo, " Color =", carro2.color)
        
        
   