import random

class Moneda:
    def __init__(self, nombre, x=None, y=None, ancho_espacio=50, largo_espacio=50):
        # Si no se proporciona una posición x o y, generar una aleatoria dentro del espacio
        self.nombre = nombre
        self.x = x if x is not None else random.randint(0, ancho_espacio - 1)
        self.y = y if y is not None else random.randint(0, largo_espacio - 1)

    def posicion(self):
        return (self.x, self.y)
