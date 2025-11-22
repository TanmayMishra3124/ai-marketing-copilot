import os
from groq import Groq
from config.settings import GROQ_API_KEY, MODEL_NAME

# Initialize Groq client
# Ensure API key is available
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is not set in environment variables or settings.py")

client = Groq(api_key=GROQ_API_KEY)

def load_prompt_template():
    prompt_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', 'prompts', 'marketing_prompt.txt')
    with open(prompt_path, 'r') as f:
        return f.read()

def generate_content(brand, audience, platform, tone, goal):
    template = load_prompt_template()
    prompt = template.format(brand=brand, audience=audience, platform=platform, tone=tone, goal=goal)
    
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model=MODEL_NAME,
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        print(f"DEBUG: API Error: {e}")
        return f"Error generating content: {str(e)}"
