class Persona:
    def __init__(self, nombre,año,hermanos, hermanas, profesion, intereses,posicion=[0,0]):
        self.nombre = nombre
        self.año= año
        self.posicion_x=posicion[0]
        self.posicion_y=posicion[1]
        self.edad=2024-año
        self.hermanos=hermanos
        self.hermanas=hermanas
        self.profesion=profesion
        self.intereses=intereses
        self.monedero =0


    def saludar(self, frase=""):
        print(f"Hola me llamo {self.nombre}, soy de {self.ciudad} y tengo {self.edad} años{frase}")

    def parientes(self):
        print(f"Tengo {self.hermanos} hermanos y {self.hermanas} hermanas")

    def trabajo(self):
        print(f"Me dedico a {self.profesion} y me gusta {self.intereses}")

    def __str__(self):
        return f"Nombre:{self.nombre}, posicion: x={self.posicion_x}y={self.posicion_y}"

#persona1=Persona("Fulano", 1996, 2, 1, "la fisica", "el baloncesto")
#persona2=Persona("Peter", 1996, 2, 1, "la fisica", "el baloncesto")
#persona1.saludar(" y soy muy majo")
#persona1.parientes()
#persona1.trabajo()
