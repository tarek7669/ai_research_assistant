from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers.pipelines import pipeline
from app.core.config import settings
import torch
from typing import List

class QAEngine:
    def __init__(self):

        print("Trying to Login to Hugging Face")

        assert "phi" in settings.LLM_MODEL_NAME.lower(), f"Wrong model still being used!: {settings.LLM_MODEL_NAME}"
        # Login to Hugging Face
        from huggingface_hub import login
        login(token=settings.HUGGINGFACE_TOKEN)

        print("Initializing QAEngine.")
        print(f"Loading LLM: {settings.LLM_MODEL_NAME} (FP16={settings.USE_FP16})")

        # Load Model and tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(settings.LLM_MODEL_NAME)

        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        dtype = torch.float16 if torch.cuda.is_available() else torch.float32

        self.model = AutoModelForCausalLM.from_pretrained(
            settings.LLM_MODEL_NAME,
            torch_dtype=dtype
        ).to(device)

        self.generator = pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
            device=0 if torch.cuda.is_available() else -1
        )

    def generate_answer(self, question: str, context_chunks: List[str]) -> str:
        
        context = '\n'.join(context_chunks)
        
        prompt = f"""
        You are an expert assistant.
        You will asnwer the question using only the information in the context below.

        ### Context:
        {context}

        ### Question:
        {question}

        ### Answer:
        """

        response = self.generator(prompt, max_new_tokens=256, do_sample=False)[0]['generated_text'] # type: ignore
        
        # Remove the prompt from the answer
        answer = response.split("### Answer:")[-1].strip() # type: ignore

        return answer