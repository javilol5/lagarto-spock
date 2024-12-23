"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
import random
from rxconfig import config
from lagarto_spock.proyecto import maquina

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

@rx.page(route="/", title="lagarto_spock")
def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.vstack(
        rx.color_mode.button(position="top-right"),
        opciones(),
        #rx.box(
        #rx.box(question, text_align="right"),
        #rx.box(answer, text_align="left"),
        #margin_y="1em",
        #    ),
        #rx.box(
        #rx.foreach(
        #    State.chat_history,
        #    lambda messages: qa(messages[0], messages[1]),
        #    )
        #),
        rx.flex(rx.card(
                rx.image(src='vacio.png'),
            ),
            rx.card(
                rx.image(src= maquina + '.png'),
            ),
        ),
        rx.logo(),
    ),)


app = rx.App()
app.add_page(index)
