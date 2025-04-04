class Producto:
    def __init__(self, nombre, precio, info, ingredientes, puntos=0):
        self.nombre = nombre
        self.precio = precio
        self.info = info
        self.ingredientes = ingredientes
        self.puntos = puntos
    
    def disponibilidad(self):
        for ingrediente, cantidad_necesaria in self.ingredientes:
            if ingrediente.cantidad < cantidad_necesaria:
                return False
        return True

    def descripcion(self):
        print(f"Nombre: {self.nombre} \nPrecio: ${self.precio} \nDescripción: {self.info}\nIngredientes:")
        for ingrediente, cantidad_necesaria in self.ingredientes:
            print(f"- {ingrediente.nombre}, cantidad necesaria: {cantidad_necesaria}")
        print(f"Puntos por compra: {self.puntos}")  


