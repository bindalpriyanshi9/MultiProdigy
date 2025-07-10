import asyncio

# ✅ Import clients correctly
from MultiProdigy.llm.clients import OpenAIClient, GeminiClient, OllamaClient
from MultiProdigy.llm.huggingface_client import HuggingFaceClient

# ✅ HuggingFace (offline model)
async def demo_huggingface():
    try:
        client = HuggingFaceClient(model_name="distilgpt2")  # or "gpt2"
        result = await client.generate("Tell me about Artificial Intelligence.")
        print(f"\n🟡 HuggingFace (Offline) Response: {result}")
    except Exception as e:
        print(f"❌ HuggingFace Error: {e}")

# ✅ Simulated OpenAI
async def demo_openai():
    client = OpenAIClient()
    result = await client.generate("Hello from OpenAI")
    print(f"\n🔷 OpenAI Response: {result}")

# ✅ Simulated Gemini
async def demo_gemini():
    client = GeminiClient()
    result = await client.generate("Hello from Gemini")
    print(f"\n🟣 Gemini Response: {result}")

# ✅ Real Ollama
async def demo_ollama():
    client = OllamaClient(model="tinyllama")  # or any local model like llama3
    result = await client.generate("Hello from Ollama")
    print(f"\n🟢 Ollama Response: {result}")

# ✅ Main orchestrator
async def main():
    print("🌐 Running all LLM Clients Demo...\n")
    await demo_openai()
    await demo_gemini()
    await demo_huggingface()
    await demo_ollama()
    print("\n✅ All clients ran successfully!")

# ✅ Run the main function
if __name__ == "__main__":
    asyncio.run(main())
