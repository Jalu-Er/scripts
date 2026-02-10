import os

DISCORD_APP_ID = os.getenv("DISCORD_APP_ID")
if not DISCORD_APP_ID:
    raise RuntimeError("DISCORD_APP_ID not set")

UPDATE_INTERVAL = 30

LARGE_IMAGE = "logo_utama"
LARGE_TEXT = "RaivelXV | Workspace"

GITHUB_URL = "https://github.com/Jalu-Er"
