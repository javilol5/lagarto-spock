import random
import reflex
#from lagarto_spock.lagarto_spock import persona

opciones = ['piedra', 'papel', 'tijera', 'lagarto', 'spock']
reglas = {
    'piedra': ['tijera', 'lagarto'],
    'papel': ['piedra', 'spock'],
    'tijera': ['papel', 'lagarto'],
    'lagarto': ['spock', 'papel'],
    'spock': ['tijera', 'piedra']
}

maquina = random.choice(opciones)
#persona = input(f"Elige entre {', '.join(opciones)}: ").lower()

#print(f"Tú elegiste: {persona}")
#print(f"La máquina eligió: {maquina}")
#
#if persona not in opciones:
#    print(f"Elección no válida. Por favor, elige entre {', '.join(opciones)}.")
#elif persona == maquina:
#    print("¡Es un empate!")
#elif maquina in reglas[persona]:
#    print("¡Ganaste!")
#else:
#    print("Perdiste, mejor suerte la próxima vez.")


def vaiables():
    if persona not in opciones:
        respuesta = f"Elección no válida. Por favor, elige entre {', '.join(opciones)}."
    elif persona == maquina:
        respuesta = "¡Es un empate!"
    elif maquina in reglas[persona]:
        respuesta = "¡Ganaste!"
    else:
        respuesta = "Perdiste, mejor suerte la próxima vez."
 

texto_chulo = respuesta