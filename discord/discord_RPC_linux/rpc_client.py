import time
import psutil
from pypresence import Presence
from config import DISCORD_APP_ID, LARGE_IMAGE, LARGE_TEXT, GITHUB_URL


class DiscordRPC:
    def __init__(self):
        self.rpc = None
        self.start_time = None

    def _discord_running(self):
        for p in psutil.process_iter(("name",)):
            name = p.info["name"]
            if name and "discord" in name.lower():
                return True
        return False

    def _new_client(self):
        self.rpc = Presence(DISCORD_APP_ID)
        self.rpc.connect()
        self.start_time = time.time()

    def _destroy_client(self):
        try:
            self.rpc.clear()
            self.rpc.close()
        except Exception:
            pass
        self.rpc = None
        self.start_time = None

    def update(self, details, state, icon):
        if not self._discord_running():
            if self.rpc:
                self._destroy_client()
            return

        if self.rpc is None:
            try:
                self._new_client()
            except Exception:
                self.rpc = None
                return

        try:
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
        except Exception:
            self._destroy_client()
