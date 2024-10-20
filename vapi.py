import os
from vapi_python import Vapi

VAPI_PUBLIC_KEY = os.environ.get('VAPI_PUBLIC_KEY')
vapi = Vapi(api_key=VAPI_PUBLIC_KEY)

def start_assistant(persona, context):
  assistant = {
    'firstMessage': 'Hey, how are you?',
    'context': f"pretend you are a {persona}, please help me with my questions using the following context: {context}",
    'model': 'gpt-3.5-turbo',
    'voice': 'jennifer-playht',
    "recordingEnabled": True,
    "interruptionsEnabled": False
  }
  vapi.start(assistant=assistant)

def stop_assistant():
  vapi.stop()
