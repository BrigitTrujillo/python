class Producto:
    def __init__(self, nombre, precio, marca):
        self.nombre = nombre
        self.precio = precio
        self.marca = marca
        
    def toDBCollection(self):
        return{
            'nombre': self.nombre,
            'precio': self.precio,
            'marca': self.marca
            
        }