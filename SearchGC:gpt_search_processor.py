'''
Handles communication with the OpenAI GPT API for search queries
'''
import openai
class GPTSearchProcessor:
    def __init__(self, api_key_manager):
        self.api_key_manager = api_key_manager
    def query(self, text):
        api_key = self.api_key_manager.get_key()
        if not api_key:
            raise ValueError("API key not set.")
        openai.api_key = api_key
        response = openai.Completion.create(engine="GPT_4_Turbo", prompt=text, max_tokens=1000)
        return response.choices[0].text.strip()
