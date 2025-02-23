from bs4 import BeautifulSoup
from dotenv import load_dotenv
from openai import OpenAI
import re
import os

def generate_summary(html):

    # Obtain text information from the HTML
    soup = BeautifulSoup(html, "html.parser")

    # Remove all of the scripts and styling information
    for script in soup(["script", "style"]):
        script.extract()
    text = soup.get_text()

    # Clean up the text obtained from the file
    clean_text = preprocess_text(text)

    # Return AI-generated summary
    return summarize_text(clean_text)

def preprocess_text(text):
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text)

    # Remove special characters
    text = re.sub(r'[^\w\s]', '', text)

    # Remove leading and trailing whitespace
    return text.replace("*", '').strip()

def summarize_text(clean_text):
    # Load in user's OpenRouter API key
    load_dotenv()
    API_KEY = os.getenv('OPENROUTER_API_KEY')
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=API_KEY
    )

    try:
        # Generate response from GPT-3.5 Turbo model
        response = client.chat.completions.create(
            model="deepseek/deepseek-r1:free",
            messages=[
                {"role": "system", "content": "You are an AI that summarizes webpage content concisely."},
                {"role": "user", "content": f"Summarize this text from a webpage: {clean_text}"} 
            ]
        )

        # Return AI-generated summary
        return response.choices[0].message.content
    
    except Exception as e:
        # If there was an error accessing the AI, return error message
        return f"Oh no! Call to AI failed! Error: {str(e)}"
