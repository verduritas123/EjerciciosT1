from clase_persona import Persona
from clase_espacio import Espacio
from clase_moneda import Moneda
from utils import calcular_distancia, contar_personas_en_espacio, estan_en_misma_posicion, persona_recoge_moneda, repartir_monedas, mover_personas

persona1 = Persona("Fulano", 1996, 2, 3 , "la fisica", "el baloncesto")
persona2 = Persona("Mengano", 1998, 1, 2, "la ingeniería", "el fútbol", [4, 5])
persona3 = Persona("Claudio", 2002, 1, 2, "el amor", "la aviación", [2, 3])
persona4 = Persona("Fausto", 2007, 1, 2, "la pescadería", "la política", [1, 1])
persona5 = Persona("Peggy", 1991, 1, 2, "la calle", "la vida", [3, 2])


espacio1= Espacio("UAX Villanueva de la Cañada", 50, 50)
espacio2= Espacio("Madrid", 4, 70)

espacio1.anadir_personas(persona1)
espacio2.anadir_personas(persona2)
espacio1.anadir_personas(persona3)
espacio1.anadir_personas(persona4)
espacio1.anadir_personas(persona5)

moneda1 = Moneda("Moneda1", 2, 3)
moneda2 = Moneda("Moneda2", 2, 3)
moneda3 = Moneda("Moneda3", 2, 3)
moneda4 = Moneda("Moneda4", 2, 3)
moneda5 = Moneda("Moneda5", 2, 3)

repartir_monedas(espacio1, 5)  # Repartir 5 monedas

numero_personas = contar_personas_en_espacio(espacio1)
print(f"En {espacio1.mostrar_informacion()} hay {numero_personas} personas")


n_turnos = 5
mover_personas(espacio1, n_turnos)


for persona in espacio1.personas:
    for moneda in espacio1.monedas:
        if persona_recoge_moneda(persona, moneda):
            print(f"{persona.nombre} recogió la {moneda.nombre}. Ahora tiene {persona.monedero} monedas.")
        else:
            print(f"{persona.nombre} no recogió la {moneda.nombre}.")


numero_personas= contar_personas_en_espacio(espacio1)
print(f"En {espacio1} hay {numero_personas} personas")


distancia = calcular_distancia(persona1, persona2)
print(f"La distancia entre {persona1.nombre} y {persona2.nombre} es de {distancia} unidades")


misma_posicion = estan_en_misma_posicion(persona1, persona2)
if misma_posicion:
    print(f"{persona1.nombre} y {persona2.nombre} están en la misma posición")
else:
    print(f"{persona1.nombre} y {persona2.nombre} NO están en la misma posición")





