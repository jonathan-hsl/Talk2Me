import reflex as rx
from Perplexity import perplexityResponse
from rxconfig import config
from Gemini import geminiResponse
from OpenAI import openai_response

class State(rx.State):
    """The app state."""
    persona: str = ""
    
    def set_persona(self, persona):
        self.persona = persona
        self.run(persona)

    def run(self, persona):
        gemini_research = geminiResponse(persona)
        perplexity_research = perplexityResponse(persona)
        text_contents = gemini_research + perplexity_research
        # get summaryconvert to txt
        summary = openai_response(text_contents)
        
        #self.convert_txt(summary)
           
        return 
    
    def convert_txt(text: str):
        # save summary to file
        return 
