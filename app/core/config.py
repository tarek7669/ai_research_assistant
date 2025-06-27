import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")
    HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")
    LLM_MODEL_NAME = os.getenv("LLM_MODEL_NAME", "microsoft/phi-2")
    USE_FP16 = os.getenv("USE_FP16")
    

settings = Settings()