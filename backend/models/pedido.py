import datetime

class pedido:
    def __init__(self, lista_productos_pedido, total):
        self.lista_productos_pedido = lista_productos_pedido
        self.total = total
        self.fecha = datetime.datetime.now()