import csv
import os

class Cliente:
    def __init__(self):
        self.rol = "cliente"
        self.lista_productos_pedido = []

    def calcular_total(self):
        cantidad_total = sum(producto.precio for producto in self.lista_productos_pedido)
        return cantidad_total

    def agregar_producto_pedido(self, producto):
        self.lista_productos_pedido.append(producto)

    def quitar_producto_pedido(self, producto):
        if producto in self.lista_productos_pedido:
            self.lista_productos_pedido.remove(producto)
        else:
            return False


class ClienteRegistrado(Cliente):
    def __init__(self, id_cliente, nombre, telefono, email, puntos_acumulados=0):
        super().__init__()
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.lista_pedidos = []
        self.puntos_acumulados = puntos_acumulados

    def acumular_puntos(self):
        puntos_totales = sum(producto.puntos for producto in self.lista_productos_pedido)
        self.puntos_acumulados += puntos_totales
        print(f"Puntos acumulados: {self.puntos_acumulados}")


class GestorClientes:
    def __init__(self, archivo_csv="clientes.csv"):
        self.archivo_csv = archivo_csv
        self.clientes = []
        self.cargar_clientes()

    def cargar_clientes(self):
        """Carga los clientes desde un archivo CSV."""
        if not os.path.exists(self.archivo_csv):
            with open(self.archivo_csv, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Nombre", "Teléfono", "Email", "Puntos"])
            return

        with open(self.archivo_csv, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                cliente = ClienteRegistrado(
                    id_cliente=row["ID"],
                    nombre=row["Nombre"],
                    telefono=row["Teléfono"],
                    email=row["Email"],
                    puntos_acumulados=int(row["Puntos"])
                )
                self.clientes.append(cliente)

    def guardar_cliente(self, cliente):
        """Guarda un nuevo cliente en el CSV."""
        if isinstance(cliente, ClienteRegistrado):
            self.clientes.append(cliente)

            with open(self.archivo_csv, mode="a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow([cliente.id_cliente, cliente.nombre, cliente.telefono, cliente.email, cliente.puntos_acumulados])

    def obtener_clientes(self):
        """Devuelve la lista de clientes registrados."""
        return self.clientes
