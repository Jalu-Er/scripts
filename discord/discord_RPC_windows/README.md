# Discord Dynamic RPC (Windows)

Dynamic Discord Rich Presence based on active applications running on the system.

This script automatically updates your Discord status depending on detected
development tools or applications such as VS Code, Unity, Android Studio,
or Minecraft.

This Windows version is designed to be simple, editable, and user-friendly.

---

## Requirements

- Windows 10 or newer
- Python 3.9 or newer
- Discord Desktop (must be running)
- Discord Developer Application with uploaded assets

---

## Installation

1. Install Python from https://www.python.org  
   Make sure to enable "Add Python to PATH" during installation.

2. Download this repository from GitHub and extract it.

3. Open Command Prompt and navigate to:

Scripts\discord\discord_RPC_windows

4. Install required dependencies:

pip install -r requirements.txt

---

## Environment Variable

Set your Discord Application ID as an environment variable.

Temporary (for testing):

set DISCORD_APP_ID=your_application_id
python main.py

Permanent (recommended):

- Open Environment Variables
- Add a new User Variable:
  Name  : DISCORD_APP_ID
  Value : your_application_id

Restart Command Prompt after setting it.

---

## Running the Script

To run manually:

python main.py

If successful, logs will appear in the terminal and
your Discord Rich Presence will update automatically.

---

## Auto Start on Windows

This folder includes a helper script:

start-discord-rpc.bat

This file starts the RPC script using the correct working directory.

### Enable Auto Start

1. Press Win + R
2. Type:

shell:startup

3. Press Enter
4. Create a shortcut to start-discord-rpc.bat and place it in this folder

The script will now start automatically when you log in to Windows.

---

## Notes

- Icons referenced by the script must exist in your Discord Developer Portal assets
- Local image files are not used directly by the script
- Source code remains fully editable

---

## License

This project is licensed under the MIT License.
