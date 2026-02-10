import time
from pypresence import Presence
from config import DISCORD_APP_ID, LARGE_IMAGE, LARGE_TEXT, GITHUB_URL

class DiscordRPC:
    def __init__(self):
        self.rpc = Presence(DISCORD_APP_ID)
        self.rpc.connect()
        self.start_time = time.time()

    def update(self, details, state, icon):
        self.rpc.update(
            details=details,
            state=state,
            large_image=LARGE_IMAGE,
            large_text=LARGE_TEXT,
            small_image=icon,
            small_text=details,
            buttons=[{"label": "GitHub", "url": GITHUB_URL}],
            start=self.start_time
        )
