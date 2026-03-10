import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
genai.configure(api_key="GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-3-flash-preview")

def analyze_image(image):

    prompt = """
    You are an AI surveillance analyst.

    Analyze the CCTV image and generate a short security report.

    Mention:
    - suspicious activity
    - objects
    - people presence
    - security risk level
    """

    response = model.generate_content([prompt, image])

    return response.text