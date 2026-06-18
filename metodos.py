class celular: 
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    def llamar(self):
        print("Llamando...")
    def cortar(self):
        print("Llamada cortada.")
        
        
celular1 = celular("Samsung", "Galaxy S21", "108MP")
celular2 = celular("Apple", "iPhone 13 Pro", "12MP")

print(celular1.llamar())