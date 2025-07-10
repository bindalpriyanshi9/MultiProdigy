from transformers import pipeline

class HuggingFaceClient:
    def __init__(self, model_name="gpt2"):
        try:
            print(f"🔄 Loading model: {model_name} ... (first time may take a few mins)")
            self.generator = pipeline("text-generation", model=model_name)
            print(f"✅ Model loaded: {model_name}")
        except Exception as e:
            print(f"❌ Error loading model '{model_name}':", e)
            self.generator = None

    async def generate(self, prompt: str):
        if not self.generator:
            return "❌ Model not available."
        try:
            result = self.generator(prompt, max_length=50, num_return_sequences=1)
            return result[0]["generated_text"]
        except Exception as e:
            return f"❌ Error generating text: {str(e)}"
