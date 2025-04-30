from transformers import pipeline, set_seed

# Tek seferlik yükleme
generator = pipeline('text-generation', model='distilgpt2')
set_seed(42)

def generate_response(prompt, max_length=150):
    results = generator(prompt, max_length=max_length, num_return_sequences=1)
    return results[0]['generated_text']
