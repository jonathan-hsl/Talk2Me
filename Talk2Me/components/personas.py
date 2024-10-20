import reflex as rx
from .server import State

def personas():
    
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.hstack(
            rx.grid(
                # Box 1: Interviewer
                rx.button(
                    rx.heading("Interviewer", size="lg", color="white"),
                    border="0.5px solid white",  # Thinner white outline
                    border_radius="10px",  # Rounded corners
                    padding="20px",
                    text_align="center",
                    width="100%",  # Ensure equal width
                    height="200px",  # Set fixed height
                    on_click=State.set_persona("interviewer"),
                ),
                # Box 2: Date
                rx.button(
                    rx.heading("Date", size="lg", color="white"),
                    border="0.5px solid white",  # Thinner white outline
                    border_radius="10px",  # Rounded corners
                    padding="20px",
                    text_align="center",
                    width="100%",  # Ensure equal width
                    height="200px",  # Set fixed height
                    on_click=State.set_persona("date"),
                ),
                # Box 3: Stranger
                rx.button(
                    rx.heading("Stranger", size="lg", color="white"),
                    border="0.5px solid white",  # Thinner white outline
                    border_radius="10px",  # Rounded corners
                    padding="20px",
                    text_align="center",
                    width="100%",  # Ensure equal width
                    height="200px",  # Set fixed height
                    on_click=State.set_persona("stranger"),
                ),
                template_columns="repeat(3, 1fr)",  # Ensure three equal columns
                gap="20px",  # Spacing between boxes
                width="100%",  # Make grid responsive
                margin="auto",
                justify_items="center",
                align_items="center",  # Vertically align items
                columns='3'
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )
