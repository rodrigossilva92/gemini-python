from src.settings import Settings
from src.genai.genai import GenAI


if __name__ == "__main__":

    ai = GenAI(Settings().API_TOKEN_GOOGLE_AI_STUDIO)
    model_settings = {
        'temperature': 0.5,         # Controls randomness in the output (creativeness)
        'top_p': 0.9,               # Controls diversity via nucleus sampling
        'top_k': 40,                # Controls diversity via top-k sampling
        'max_output_tokens': 1024,  # Maximum number of tokens in the output
        'response_mime_type': 'text/plain'  # Response format
    }
    ai.set_prompt(
        model_name="gemini-1.5-flash",
        model_settings=model_settings,
        prompt="Liste apenas os nomes dos produtos e ofereça uma breve descrição."
    )
    answer = ai.test(question="Liste três produtos de moda sustentável para ir ao shopping.")
    print(answer)