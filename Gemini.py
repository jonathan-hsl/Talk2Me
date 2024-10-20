import google.generativeai as genai 
import os
genai.configure(api_key=os.environ["API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")
class Documents(typing.TypedDict):
    doc_name: str
    contents: list[str]
def geminiResponse(topic):
    response = model.generate_content(
        f"Help me research {topic}. Give me some links to reputable websites that provide information on {topic}", # HERE, WE HAVE TO PASS IN SOME STANDARDIZED INPUT BASED ON WHATEVER THE USER SELECTS FROM THE DROPDOWN
        generation_config=genai.types.GenerationConfig(
            # Only one candidate for now.
            candidate_count=1,
            stop_sequences=["x"],
            max_output_tokens=3,
            temperature=1.0,
            response_mime_type="application/json", response_schema = list[Documents]
        ),
    )
    print(response.text)
    return response.text

