import reflex as rx
from rxconfig import config
from Perplexity import perplexityResponse
class State(rx.State):
    """The app state."""
    
    persona: str = ""
    
    def set_persona(self, persona):
        self.persona = persona
        
    