# Discord Dynamic RPC (Linux)

Dynamic Discord Rich Presence based on active applications running on the system.

This script automatically updates your Discord status depending on detected
development tools or applications such as Unity, Android Studio, VS Code,
or Minecraft.

The Linux version is designed to run as a background user service using systemd,
making it stable and lightweight for long-term usage.

---

## Requirements

- Linux distribution with systemd
- Python 3.9 or newer
- Discord Desktop (must be running)
- Discord Developer Application with uploaded assets

---

## Installation

Navigate to this directory:
```
Scripts/discord/discord_RPC_linux
```
Install required Python dependencies:
```
pip install -r requirements.txt
```
---

## Environment Variable

Set your Discord Application ID as an environment variable.

Example (Linux):
```
export DISCORD_APP_ID=your_application_id
```
The Application ID is public-safe.
Never expose bot tokens or client secrets.

---

## Running Manually (Optional)

You can run the script manually for testing:
```
python main.py
```
If successful, your Discord Rich Presence will update automatically.

---

## Running Automatically (Recommended)

This script is intended to run as a systemd user service.

Copy the service file to your user systemd directory:
```
~/.config/systemd/user/discord-rpc.service
```
Reload systemd and enable the service:
```
systemctl --user daemon-reload
systemctl --user enable discord-rpc.service
systemctl --user start discord-rpc.service
```
The script will now start automatically when you log in.

---

## Logs

To view runtime logs:
```
journalctl --user -u discord-rpc.service -f
```
---

## Notes

- Icons referenced by the script must exist in your Discord Developer Portal assets
- Asset image files in the repository are for documentation purposes only
- The script uses polling with a fixed interval to remain lightweight

---

## License

This project is licensed under the MIT License.
