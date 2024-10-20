import os
import openai
import requests
import base64
import tempfile
import simpleaudio as sa
import wave

def getSummary(text):
    system_content = "You are a gourmet. Be descriptive and helpful."
    user_content = text  # Use the text provided as the user's input

    # Set the API key and base URL for Hyperbolic
    client = openai.OpenAI(
        api_key=os.getenv("HYPERBOLIC_API_KEY"),
        base_url="https://api.hyperbolic.xyz/v1"
    )

    # Create the chat completion
    chat_completion = client.chat.completions.create(
        model="meta-llama/Meta-Llama-3-70B-Instruct",
        messages=[
            {"role": "system", "content": system_content},
            {"role": "user", "content": user_content},
        ],
        temperature=0.7,
        max_tokens=1024,
    )

    # Extract the response text
    response = chat_completion.choices[0].message.content
    print("Response:\n", response)
    return response

def playResponse(response_text):
    API_KEY = os.getenv('HYPERBOLIC_API_KEY')

    if not API_KEY:
        print("Please set the HYPERBOLIC_API_KEY environment variable.")
        return

    # Prepare the request payload
    payload = {
        "text": response_text
    }

    # Prepare the headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    # Send the POST request to the audio generation API
    response = requests.post(
        "https://api.hyperbolic.xyz/v1/audio/generation",
        json=payload,
        headers=headers
    )

    # Check if the request was successful
    if response.status_code != 200:
        print(f"Request failed with status code {response.status_code}: {response.text}")
        return

    # Parse the JSON response
    data = response.json()

    # Get the base64-encoded audio data
    audio_base64 = data.get('audio')

    if not audio_base64:
        print("No audio data received.")
        return

    # Decode the base64 audio data
    audio_bytes = base64.b64decode(audio_base64)

    # Save the audio to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as temp_audio_file:
        temp_audio_file.write(audio_bytes)
        temp_audio_path = temp_audio_file.name

    # Play the audio
    wave_obj = sa.WaveObject.from_wave_file(temp_audio_path)
    play_obj = wave_obj.play()
    play_obj.wait_done()  # Wait until sound has finished playing

    # Optionally, save the audio to a file
    with open('result.wav', 'wb') as f:
        f.write(audio_bytes)

    print("Audio played and saved to result.wav")

# Main execution
if __name__ == "__main__":
    user_input = "Tell me about Chinese hotpot"
    response = getSummary(user_input)
    #playResponse(response)
