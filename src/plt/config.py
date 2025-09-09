import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()


class Settings:
    """Centralized settings from environment variables."""

    BITBUCKET_USERNAME: str = os.getenv("BITBUCKET_USERNAME", "")
    BITBUCKET_API_TOKEN: str = os.getenv("BITBUCKET_API_TOKEN", "")
    GITHUB_USERNAME: str = os.getenv("GITHUB_USERNAME", "")
    GITHUB_TOKEN: str = os.getenv("GITHUB_TOKEN", "")


settings = Settings()
