from openai import OpenAI

YOUR_API_KEY = "PERPLEXITY_API_KEY"

client = OpenAI(api_key=YOUR_API_KEY, base_url="https://api.perplexity.ai")

# chat completion without streaming
def perplexityResponse(topic):
    messages = [
    {
        "role": "system",
        "content": (
            f"Help me research {topic}. Give me some links to reputable websites that provide information on {topic}", # HERE, WE HAVE TO PASS IN SOME STANDARDIZED INPUT BASED ON WHATEVER THE USER SELECTS FROM THE DROPDOWN"
        ),
    },
    {
        "role": "user",
        "content": (
            "How many stars are in the universe?" # THIS HERE IS GOING TO BE THE INPUT TOPIC BASED ON WHATEVER THE USER SELECTS ON THE FRONT END DROPDOWN
        ),
    },
]
    response = client.chat.completions.create(
        model="llama-3-sonar-large-32k-online",
        messages=messages,
    )
    return response
    print(response)

# chat completion with streaming
'''response_stream = client.chat.completions.create(
    model="llama-3-sonar-large-32k-online",
    messages=messages,
    stream=True,
)
for response in response_stream:
    print(response)
'''