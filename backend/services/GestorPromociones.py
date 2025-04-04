class Promocion:
    def __init__(self, nombre, porcentaje_descuento, puntos_requeridos):
        self.nombre = nombre
        self.porcentaje_descuento = porcentaje_descuento
        self.puntos_requeridos = puntos_requeridos

    def aplicar_descuento_por_puntos(self, cliente):
        if cliente.puntos_acumulados >= self.puntos_requeridos:
            descuento = cliente.calcular_total() * (self.porcentaje_descuento / 100)
            cliente.puntos_acumulados -= self.puntos_requeridos  # Restamos los puntos usados
            print(f"Descuento aplicado: ${descuento}")
            return descuento
        else:
            print("No tienes suficientes puntos para aplicar un descuento.")
            return 0
