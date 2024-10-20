import reflex as rx
from Perplexity import perplexityResponse
from rxconfig import config
from Gemini import geminiResponse

class State(rx.State):
    """The app state."""
    persona: str = ""
    
    def set_persona(self, persona):
        self.persona = persona
        self.run(persona)

    def run(persona):
        gemini_research = geminiResponse(persona)
        perplexity_research = perplexityResponse(persona)
        print(gemini_research)
        print(perplexity_research)

        return gemini_research, perplexity_research

