import csv
import os
from models.cliente import ClienteRegistrado

class GestorClientes:
    def __init__(self, archivo_csv="data/clientes.csv"):
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
