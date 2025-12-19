import os 
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET-KEY",'dev-secret-key')

    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL","sqlite:app.db")

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY","")