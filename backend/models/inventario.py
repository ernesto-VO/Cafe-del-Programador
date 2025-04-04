class Inventario:
    lista_ingredientes=[]

    def __init__(self, id, nombre, cantidad):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        Inventario.lista_ingredientes.append(self)

    def agregar_mas(self, cantidad_agregar):
        self.cantidad += cantidad_agregar

    def quitar_cantidad(self, cantidad_quitar):
        self.cantidad -= cantidad_quitar

    @classmethod
    def mostrar_inventario(cls):
        for ingrediente in Inventario.lista_ingredientes:
            print(f"id:{ingrediente.id}, nombre:{ingrediente.nombre}, cantidad: {ingrediente.cantidad}")