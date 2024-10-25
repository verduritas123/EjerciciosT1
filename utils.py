def calcular_distancia(persona_a,persona_b):
    #raiz((persona1_x - persona2_x)^2+(persona1_y - persona2_y)^2)
    distancia= ((persona_a.posicion_x - persona_b.posicion_x)**2+(persona_a.posicion_y - persona_b.posicion_y)**2)**0.5
    return distancia
    
def estan_en_misma_posicion(persona_a, persona_b):
    return persona_a.posicion_x == persona_b.posicion_x and persona_a.posicion_y == persona_b.posicion_y

def contar_personas_en_espacio(espacio):
    lista_personas = espacio.personas
    numero_personas=(len(espacio.personas))
    return numero_personas

def persona_recoge_moneda(persona,moneda):
    if persona.posicion_x == moneda.posicion_x and persona.posicion_y == moneda.posicion_y:
        persona.monedero += 1  # Incrementa el monedero de la persona
        return True
    return False

def mover_personas(espacio, n_turnos):
    for turno in range(n_turnos):
        for persona in espacio.personas:
            persona.mover(espacio.ancho, espacio.largo)
            print(f"{persona.nombre} se ha movido a la posición ({persona.posicion_x}, {persona.posicion_y})")

def repartir_monedas(espacio, cantidad_monedas):
    for i in range(cantidad_monedas):
        moneda = Moneda(f"Moneda{i+1}", ancho_espacio=espacio.ancho, largo_espacio=espacio.largo)
        espacio.anadir_monedas(moneda)
        print(f"Moneda {moneda.nombre} añadida en posición ({moneda.x}, {moneda.y})")

