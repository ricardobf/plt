import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

class Settings:
  """Centralized settings from environment variables."""

  BITBUCKET_CLIENT_ID: str = os.getenv("BITBUCKET_CLIENT_ID", "")
  BITBUCKET_CLIENT_SECRET: str = os.getenv("BITBUCKET_CLIENT_SECRET", "")
  GITHUB_USERNAME: str = os.getenv("GITHUB_USERNAME", "")
  GITHUB_TOKEN: str = os.getenv("GITHUB_TOKEN", "")

settings = Settings()
