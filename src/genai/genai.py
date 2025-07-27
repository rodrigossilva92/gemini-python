import google.generativeai as genai

from src.settings import Settings


class GenAI:
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self._configure()

    def __del__(self):
        ...

    def _configure(self):
        genai.configure(api_key=self.api_key)
        self.__available_models = self.get_available_models()

    def _check_chosen_model(self, model_name: str):
        if model_name not in self.__available_models:
            raise ValueError(f"Model {model_name} is not available.")

    def get_available_models(self):
        """
        Returns a list of available models.
        """
        models = list()
        _models = genai.list_models()
        for model in _models:
            model_name = str(model.name).replace('models/','')
            models.append(model_name)

        return models
    
    def set_prompt(self, *, model_name: str, model_settings: dict, prompt: str):
        self._check_chosen_model(model_name)

        self._llm = genai.GenerativeModel(
            model_name=model_name,
            generation_config=model_settings,
            system_instruction=prompt
        )
    
    def test(self, *, question: str) -> str:
        if not hasattr(self, '_llm'):
            raise ValueError("Prompt not set. Please set a prompt before testing.")

        response = self._llm.generate_content(question)
        return response.text

