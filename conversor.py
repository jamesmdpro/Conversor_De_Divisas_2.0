class Conversor:
    def __init__(self, pesos, dolares, soles, pesosmxn, trm):
        self.pesos = pesos
        self.dolares = dolares
        self.soles = soles
        self.pesosmxn = pesosmxn
        self.trm = trm

    def convert_to_dollars(self):
        return self.pesos / self.trm

    def convert_to_pesos(self):
        return self.dolares * self.trm

    def convert_to_dollarsMXN(self):
        return self.pesosmxn / self.trm

    def convert_to_pesosMXN(self):
        return self.dolares * self.trm

    def convert_to_dollarsPEN(self):
        return self.soles / self.trm

    def convert_to_pesosPEN(self):
        return self.dolares * self.trm

# todos los cambios están basados en el trm del dólar vs el precio de la moneda puntual.
