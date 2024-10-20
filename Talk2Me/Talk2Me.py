"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from .components.personas import personas

from rxconfig import config

from .server import State

# Frontend
def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("An innovative tool to improve social comfort.", size="9"),
            rx.button(
                "Choose a Persona to Talk2.",
                on_click=rx.redirect(
                    "/personas",
                ),
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )

app = rx.App()
app.add_page(personas, route="/personas")
app.add_page(index)
