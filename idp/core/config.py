from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    app_name: str = "IDP API"
    version: str = "1.0.0"
    port: int = 8000
    debug: bool = False
    database_url: str
    kubeconfig_path: str = "~/.kube/config"


settings = Settings()

