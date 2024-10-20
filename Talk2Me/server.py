import reflex as rx
from Perplexity import perplexityResponse
from rxconfig import config
from Gemini import geminiResponse

class State(rx.State):
    """The app state."""
    persona: str = ""

    def set_persona(self, persona):
        self.persona = persona
    
    def run(self, persona):
        gemini_research = geminiResponse(persona)
        perplexity_research = perplexityResponse(persona)
        
        return 