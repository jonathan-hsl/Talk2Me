import reflex as rx
from ..server import State

def create_styled_text(text_color, font_size, content):
    return rx.text(
        content,
        color=text_color,
        font_size=font_size,
        line_height="1.75rem",
    )


def create_icon(alt_text, icon_name):
    return rx.icon(
        alt=alt_text,
        tag=icon_name,
        height="1.25rem",
        color="white",
        margin_right="0.5rem",
        width="1.25rem",
    )


def create_welcome_header():
    return rx.box(
        rx.heading(
            "Talk to a...",
            font_weight="700",
            margin_bottom="1rem",
            font_size="2.25rem",
            line_height="2.5rem",
            color="#1F2937",
            as_="h1",
        ),
        create_styled_text(
            text_color="#4B5563",
            font_size="1.25rem",
            content="Choose a relevant persona to begin the social experience.",
        ),
        margin_bottom="3rem",
        text_align="center",
    )


def create_get_started_button():
    return rx.el.button(
        create_icon(
            alt_text="Get Started Icon", icon_name="rocket"
        ),
        " Interviewer ",
        background_color="#3B82F6",
        transition_duration="300ms",
        display="flex",
        font_weight="700",
        _hover={"background-color": "#2563EB"},
        align_items="center",
        padding_left="1.5rem",
        padding_right="1.5rem",
        padding_top="0.75rem",
        padding_bottom="0.75rem",
        border_radius="0.5rem",
        color="#ffffff",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )


def create_learn_more_button():
    return rx.el.button(
        create_icon(
            alt_text="Learn More Icon",
            icon_name="book-open",
        ),
        " Friend ",
        background_color="#10B981",
        transition_duration="300ms",
        display="flex",
        font_weight="700",
        _hover={"background-color": "#059669"},
        align_items="center",
        padding_left="1.5rem",
        padding_right="1.5rem",
        padding_top="0.75rem",
        padding_bottom="0.75rem",
        border_radius="0.5rem",
        color="#ffffff",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )


def create_contact_us_button():
    return rx.el.button(
        create_icon(
            alt_text="Contact Us Icon", icon_name="heart"
        ),
        " Date ",
        background_color="#8B5CF6",
        transition_duration="300ms",
        display="flex",
        font_weight="700",
        _hover={"background-color": "#7C3AED"},
        align_items="center",
        padding_left="1.5rem",
        padding_right="1.5rem",
        padding_top="0.75rem",
        padding_bottom="0.75rem",
        border_radius="0.5rem",
        color="#ffffff",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )


def create_main_content():
    return rx.box(
        create_welcome_header(),
        rx.flex(
            create_get_started_button(),
            create_learn_more_button(),
            create_contact_us_button(),
            display="flex",
            flex_direction=rx.breakpoints(
                {"0px": "column", "768px": "row"}
            ),
            gap="1.5rem",
            align_items="center",
            justify_content="center",
            margin_bottom="3rem",
        ),
        rx.box(
            rx.text(
                "Join thousands of satisfied users and transform the way you work",
                margin_bottom="1rem",
                color="#374151",
                font_size="1.125rem",
                line_height="1.75rem",
            ),
            create_styled_text(
                text_color="#374151",
                font_size="1.125rem",
                content="Start your journey today and experience the difference!",
            ),
            text_align="center",
        ),
        width="100%",
        style=rx.breakpoints(
            {
                "640px": {"max-width": "640px"},
                "768px": {"max-width": "768px"},
                "1024px": {"max-width": "1024px"},
                "1280px": {"max-width": "1280px"},
                "1536px": {"max-width": "1536px"},
            }
        ),
        margin_left="auto",
        margin_right="auto",
        padding_left="1rem",
        padding_right="1rem",
        padding_top="4rem",
        padding_bottom="4rem",
    )


def personas():
    return rx.fragment(
        rx.el.link(
            href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css",
            rel="stylesheet",
        ),
        rx.el.style(
            """
            @font-face {
                font-family: 'LucideIcons';
                src: url(https://unpkg.com/lucide-static@latest/font/Lucide.ttf) format('truetype');
            }
            body {
                background: linear-gradient(30deg, #ff6b6b, #4ecdc4, #45b7d1, #f7b731);
                background-size: 400% 400%;
                animation: gradientBG 15s ease infinite;
            }
            @keyframes gradientBG {
                0% {background-position: 0% 50%;}
                50% {background-position: 100% 50%;}
                100% {background-position: 0% 50%;}
            }
            """
        ),
        rx.box(
            create_main_content(),
            display="flex",
            font_family='system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"',
            align_items="center",
            justify_content="center",
            min_height="100vh",
        ),
    )