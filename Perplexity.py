from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ.get("PERPLEXITY_API_KEY"),
    base_url="https://api.perplexity.ai"
)

def perplexityResponse(topic):
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant that provides information and links to reputable websites."
        },
        {
            "role": "user",
            "content": f"Help me research {topic}. Give me some links to reputable websites that provide information on this topic."
        }
    ]
    try:
        response = client.chat.completions.create(
            model="llama-3.1-sonar-huge-128k-online",
            messages=messages,
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error in perplexityResponse: {str(e)}")
        return None

# chat completion with streaming
'''response_stream = client.chat.completions.create(
    model="llama-3-sonar-large-32k-online",
    messages=messages,
    stream=True,
)
for response in response_stream:
    print(response)
'''
