import reflex as rx
from .components.personas import personas

from rxconfig import config

from .server import State

# Frontend
def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.flex(
            rx.hstack(
                rx.vstack(
                    rx.heading("Talk2Me: An innovative tool to improve social comfort.", size="9", margin_bottom="2rem", text_shadow="rgba(191,0,255,0.47) 0px 0px 31px"),
                    rx.hstack(
                        rx.text(
                            """
                            Talk2Me is a novel AI-powered software that allows users to improve public speaking, hone interpersonal connections,
                            and ace behavioral interviews with empathetic, fine-tuned models. Engage with custom-engineered Personas to simulate
                            conversations with a wide breadth of characters, including friends, hiring managers, and dates.
                            """,
                            size="5",
                            margin_bottom="2rem",
                        )
                    ),
                    rx.hstack(
                        rx.button(
                            "Personas",
                            on_click=rx.redirect(
                                "/personas",
                            ),
                            color_scheme="purple",
                            cursor="pointer",
                            margin_bottom="2rem",
                        ),
                        rx.button(
                            "Documentation",
                            on_click=rx.redirect(
                                "https://github.com/jonathan-hsl/Talk2Me",
                            ),
                            color_scheme="purple",
                            cursor="pointer",
                            margin_bottom="2rem",
                        ),
                    ),
                ),
                rx.image(src="/hero.png", width="50%", height="50%"),
            ),
            spacing="5",
            height="100vh",
            width="115%",
            margin="auto",
            flex_direction="column",
            justify_content="space-between",
            margin_top="7rem",
        ),
        rx.vstack(
            rx.heading("Driving real connections with a human-first approach.", size="9", text_align="right", text_shadow="rgba(191,0,255,0.47) 0px 0px 31px"),
            rx.hstack(
                rx.text(
                    """
                    Talk2Me implements text-based LLM APIs from OpenAI, Perplexity, and Gemini. It also leverages Hume's eLLM, an
                    LLM designed to parse emotional context and nuance—essential for our Personas to actually promote growth in social skills.
                    Our pipeline is connected with FetchAI's RAG and langchain agent and the website is developed fully in Reflex.
                    """
                , text_align="right")
            ),
            spacing="5",
            min_height="50vh",
            width="115%",
            margin="auto",
        ),
    )

app = rx.App()
app.add_page(personas, route="/personas")
app.add_page(index)