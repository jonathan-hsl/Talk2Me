import reflex as rx
from Perplexity import perplexityResponse
from rxconfig import config
from Gemini import geminiResponse

class State(rx.State):
    """The app state."""
    
    def run(persona):
        gemini_research = geminiResponse(persona)
        perplexity_research = perplexityResponse(persona)

        return 