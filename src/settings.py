from pydantic_settings import BaseSettings, SettingsConfigDict

from src import paths


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=paths.FILE_DOTENV,
        env_file_encoding="utf-8",
    )

    API_TOKEN_GOOGLE_AI_STUDIO: str
