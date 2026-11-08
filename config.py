import os
from dataclasses import dataclass
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class Settings:
    discord_token: str = os.getenv("DISCORD_TOKEN", "")
    bot_prefix: str = os.getenv("BOT_PREFIX", "..")
    database_path: str = os.getenv("DATABASE_PATH", "data/horizon.sqlite3")

settings = Settings()
Path(settings.database_path).parent.mkdir(parents=True, exist_ok=True)
