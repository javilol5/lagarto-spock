import random
import reflex as rx
import lagarto_spock.lagarto_spock as ls

opciones = ['piedra', 'papel', 'tijera', 'lagarto', 'spock']
reglas = {
    'piedra': ['tijera', 'lagarto'],
    'papel': ['piedra', 'spock'],
    'tijera': ['papel', 'lagarto'],
    'lagarto': ['spock', 'papel'],
    'spock': ['tijera', 'piedra']
}

maquina = random.choice(opciones)
class State(rx.State):
    def answer(self):
                        
        if ls.persona == maquina:
            self.answers = "¡Es un empate!"
        elif maquina in reglas[ls.persona]:
            self.answers = "¡Ganaste!"
        else:
            self.answers = "Perdiste, mejor suerte la próxima vez."
        
        self.chat_history = []  # reinicia el historial de chat a un chat vacio
        self.chat_history.append((self.answers))