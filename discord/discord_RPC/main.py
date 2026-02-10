import time
from rpc_client import DiscordRPC
from activity_detector import detect_activity
from config import UPDATE_INTERVAL

def main():
    rpc = DiscordRPC()
    while True:
        details, state, icon = detect_activity()
        rpc.update(details, state, icon)
        time.sleep(UPDATE_INTERVAL)

if __name__ == "__main__":
    main()
