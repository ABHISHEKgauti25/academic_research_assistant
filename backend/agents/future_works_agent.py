# agents/future_works_agent.py
from transformers import pipeline

# Load a language model for text generation
generator = pipeline('text-generation', model='gpt2')

def generate_future_works(topic: str):
    prompt = f"Based on recent advancements in {topic}, suggest potential future research directions and improvements."
    future_works = generator(prompt, max_length=200, num_return_sequences=1)
    return future_works[0]['generated_text']
