from openai import OpenAI
client = OpenAI()

def openai_response(text_contents): # this function is gonna take in the txt file/its contents
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": f"Go through each of the links contained in here: '{text_contents}'. Summarize them and give me detailed notes about them."
            }
        ]
    )
    print(completion.choices[0].message)
    return completion.choices[0].message
    