import datetime

class GestionPago:
    def __init__(self, cliente):
        self.cliente = cliente

    def pagar(self, nombre_completo, numero_tarjeta, fecha_vencimiento, cvv):
        fecha_actual = datetime.date.today()

        if len(nombre_completo) > 5 and self.verificar_tarjeta(numero_tarjeta) and fecha_actual < fecha_vencimiento and cvv <= 4:
            print("Pago exitoso.")
            return True
        else:
            print("Pago fallido. Verifique los detalles de pago.")
            return False

    @classmethod
    def verificar_tarjeta(cls, numero_tarjeta):
        numero_tarjeta = ''.join(filter(str.isdigit, numero_tarjeta))
        n_digitos = len(numero_tarjeta)
        n_sum = 0
        es_segundo_digito = False
        for i in range(n_digitos - 1, -1, -1):
            d = int(numero_tarjeta[i])
            if es_segundo_digito:
                d *= 2
                if d > 9:
                    d -= 9
            n_sum += d
            es_segundo_digito = not es_segundo_digito
        return (n_sum % 10) == 0
