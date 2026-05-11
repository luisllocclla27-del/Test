class PasarelaExterna:
    def autorizar(self, monto):
        # Simula una llamada a una API bancaria lenta
        pass

class ProcesadorPagos:
    def __init__(self, pasarela):
        self.pasarela = pasarela
        self.limite_diario = 1000.0

    def procesar_transaccion(self, monto_base):
        if monto_base <= 0:
            raise ValueError("El monto debe ser positivo")

        # Cálculo de impuesto (18% IGV)
        total = monto_base * 1.18

        if total > self.limite_diario:
            return False, "Excede límite diario"

        # Dependencia del mock
        autorizado = self.pasarela.autorizar(total)
        return autorizado, "Transacción completada" if autorizado else "Rechazada por el banco"
