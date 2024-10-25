class Espacio:
    def __init__(self,nombre,largo=10,ancho=10):
        self.nombre=nombre
        self.personas=[]
        self.monedas=[]
        self.largo=largo
        self.ancho=ancho


    def anadir_personas(self, persona):
        self.personas.append(persona)
        print(f"He añadido a {persona} al espacio{self.nombre}")

    def anadir_monedas(self, moneda):
        self.monedas.append(moneda)
        print(f"He añadido a {moneda} al espacio{self.nombre}")

    def __str__(self):
        return f"Este espacio es: {self.nombre} y mide {self.ancho} metros por {self.largo} metros de largo"