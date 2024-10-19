"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

from .server import State

# Frontend
def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("An innovative tool to improve social comfort.", size="9"),
            rx.text(
                "Choose a persona to #Talk2.",
                size="5",
            ),
            rx.link(
                rx.button("Let's get chatting.", color_scheme="purple", cursor="pointer"),
                href="/personas",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )

def personas():
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Personas:", size="9"),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )


app = rx.App()
app.add_page(personas, route="/personas")
app.add_page(index)
