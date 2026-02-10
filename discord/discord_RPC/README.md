
# Discord Dynamic RPC

Dynamic Discord Rich Presence based on active applications running on the system.

This script updates your Discord status automatically depending on detected
development tools or applications such as Unity, Android Studio, VS Code, or Minecraft.

---

## Requirements

- Python 3.9 or newer
- Discord Desktop (must be running)
- Discord Developer Application with uploaded assets

---

## Installation

Install required Python dependencies:

```bash
pip install -r requirements.txt
````

---

## Environment Variable

Set your Discord Application ID using an environment variable.

Example (Linux):

```bash
export DISCORD_APP_ID=your_application_id
```

The Application ID is **public-safe**, but tokens or secrets must never be committed.

---

## Running the Script

From inside the `discord_RPC` directory:

```bash
python main.py
```

If successful, your Discord Rich Presence will update automatically.

---

## Notes

* Icons referenced in the script must exist in your Discord Developer Portal assets.
* Asset image files in the repository are for documentation purposes only.
* This script uses polling with a fixed interval to remain lightweight.

---

## License

This project is licensed under the MIT License.
