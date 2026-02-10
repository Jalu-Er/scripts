import time
from rpc_client import DiscordRPC
from activity_detector import detect_activity
from config import UPDATE_INTERVAL

def log(message):
    ts = time.strftime("%H:%M:%S")
    print(f"[{ts}] {message}", flush=True)

def main():
    rpc = DiscordRPC()
    last_activity = None

    log("Discord RPC started")

    while True:
        try:
            activity = detect_activity()

            if activity != last_activity:
                details, state, icon = activity
                rpc.update(details, state, icon)
                log(f"Activity changed -> {details}")
                last_activity = activity

        except Exception as e:
            log(f"Error: {e}")

        time.sleep(UPDATE_INTERVAL)

if __name__ == "__main__":
    main()
