from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Number Guessing Game"
    app_version: str = "1.0.0"
    debug: bool = True
    
    # Game settings
    min_number: int = 1
    max_number: int = 100
    max_players: int = 2
    max_attempts: int = 10
    
    # Server settings
    host: str = "0.0.0.0"
    port: int = 8000

    class Config:
        env_file = ".env"


settings = Settings()
