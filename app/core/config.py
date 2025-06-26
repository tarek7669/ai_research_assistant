import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")
    LLM_MODEL = os.getenv("LLM_MODEL")
    USE_FP16 = os.getenv("USE_FP16")
    

settings = Settings()