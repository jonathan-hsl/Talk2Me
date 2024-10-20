import reflex as rx

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