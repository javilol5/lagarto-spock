import reflex as rx
import random
from rxconfig import config
from lagarto_spock.proyecto import maquina


class State(rx.State):
    """Estado de la aplicación."""
    # Rutas de imágenes
    img_src_piedra: str = "piedra.png"
    img_src_papel: str = "papel.png"
    img_src_tijera: str = "tijera.png"
    img_src_lagarto: str = "lagarto.png"
    img_src_spock: str = "spock.png"

    # Elección del usuario
    persona: str = "vacio"  # Por defecto, ninguna elección

    def set_persona(self, eleccion: str):
        """Actualizar la elección del usuario."""
        self.persona = eleccion


def opciones():
    """Genera las opciones clicables."""
    return rx.flex(
        rx.card(
            rx.image(
                src="piedra.png",
                on_click=lambda: State.set_persona("piedra"),
            ),
        ),
        rx.card(
            rx.image(
                src="papel.png",
                on_click=lambda: State.set_persona("papel"),
            ),
        ),
        rx.card(
            rx.image(
                src="tijera.png",
                on_click=lambda: State.set_persona("tijera"),
            ),
        ),
        rx.card(
            rx.image(
                src="lagarto.png",
                on_click=lambda: State.set_persona("lagarto"),
            ),
        ),
        rx.card(
            rx.image(
                src="spock.png",
                on_click=lambda: State.set_persona("spock"),
            ),
        ),
    )


def elecciones():
    """Muestra las elecciones del usuario y la máquina."""
    return rx.flex(
        rx.card(
            rx.text("Tu elección"),
            rx.image(src=State.persona + ".png"),
        ),
        rx.card(
            rx.text(if persona not in opciones:
                        print(f"Elección no válida. Por favor, elige entre {', '.join(opciones)}.")
elif persona == maquina:
    print("¡Es un empate!")
elif maquina in reglas[persona]:
    print("¡Ganaste!")
else:
    print("Perdiste, mejor suerte la próxima vez.")'),
        ),
        rx.card(
            rx.text(maquina),
            rx.image(src="r" + maquina + ".png"),
        ),
    )


@rx.page(route="/", title="Lagarto Spock")
def index() -> rx.Component:
    """Página principal."""
    return rx.container(
        rx.vstack(
            rx.color_mode.button(position="top-right"),
            opciones(),
            elecciones(),
            rx.logo(),
        ),
    )


# Crear la app
app = rx.App()
app.add_page(index)