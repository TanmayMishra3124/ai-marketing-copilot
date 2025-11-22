import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "database", "campaigns.db")
MODEL_NAME = "llama-3.3-70b-versatile"
