from Hyperbolic import getSummary
import reflex as rx
from Perplexity import perplexityResponse
from rxconfig import config
from Gemini import geminiResponse
from OpenAI import openai_response
from vapi import start_assistant

class State(rx.State):
    """The app state."""
    persona: str = ""
    
    def set_persona(self, persona):
        self.persona = persona
        self.run(persona)

    def run(self, persona):
        # gemini_research = geminiResponse(persona)
        # perplexity_research = perplexityResponse(persona)
        # text_contents = gemini_research + perplexity_research
        # print("text_contents:", text_contents)
        #summary = getSummary(text_contents)

        summaries = {
            "interviewer": "You are a hiring manager interviewing a candidate for a role. You are going to ask behavioral questions as a hiring manager normally would. Use the user responses to inform your follow-up questions. At the end, when the user says 'done', give a brief critique of their performance and what they can work on.",
            "date": "You are a person on a date. You are going to ask questions and carry a conversation like two people on a date normally would. Use the user responses to inform your statements and questions. At the end, when the user says 'done', give a brief critique of their performance and what they can work on.",
            "stranger": "You are a random person the user is introducing themselves to. You are going to introduce yourself with a random name and background, and ask inquisitive but normal questions. Use the user responses to inform your statements and questions. At the end, when the user says 'done', give a brief critique of their performance and what they can work on."
        }

        # summary = openai_response(text_contents)
        print("summary:", summaries[persona])
        start_assistant(persona, summaries[persona])

        

