"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
import random
from rxconfig import config
from lagarto_spock.proyecto import maquina
from lagarto_spock.proyecto import persona

class State(rx.State):
      def a():
            rx.button(),
    

def opciones():
        return rx.flex(
            rx.card(
                rx.image(src='piedra.png'),
            ),
            rx.card(
                rx.image(src='papel.png'),
            ),
            rx.card(
                rx.image(src='tijeras.png'),
            ),
            rx.card(
                rx.image(src='lagarto.png'),
            ),
            rx.card(
                rx.image(src='spock.png'),
            ),
        ),

def elecciones():
      return rx.flex(
            rx.card(
                rx.text(persona),
                rx.image(src= persona + '.png'),
            ),
            rx.card(
                rx.text(maquina),
                rx.image(src= 'r' + maquina + '.png'),
            ),
        ),

@rx.page(route="/", title="lagarto_spock")
def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.vstack(
        rx.color_mode.button(position="top-right"),
        opciones(),
        elecciones(),
        rx.logo(),
        ),
    )


app = rx.App()
app.add_page(index)
