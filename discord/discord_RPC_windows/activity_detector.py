import psutil

RULES = [
    {
        "process": "unity",
        "details": "Game Development",
        "state": "Building Virtual Worlds",
        "icon": "icon_game",
    },
    {
        "process": "studio64",
        "details": "Mobile Development",
        "state": "Building Mobile Applications",
        "icon": "icon_android",
    },
    {
        "process": "code",
        "details": "Software Development",
        "state": "Transforming Ideas into Code",
        "icon": "icon_vscode",
    },
    {
        "process": "code-oss",
        "details": "Software Development",
        "state": "Transforming Ideas into Code",
        "icon": "icon_vscode",
    },
]

DEFAULT_ACTIVITY = {
    "details": "System Optimization",
    "state": "Environment: Arch Linux",
    "icon": "icon_arch",
}

def detect_activity():
    processes = {p.name().lower() for p in psutil.process_iter(['name'])}

    for rule in RULES:
        if rule["process"] in processes:
            return rule["details"], rule["state"], rule["icon"]

    if "java" in processes and any("minecraft" in p for p in processes):
        return "Minecraft Workspace", "Managing Server & Skript", "icon_mc"

    return DEFAULT_ACTIVITY["details"], DEFAULT_ACTIVITY["state"], DEFAULT_ACTIVITY["icon"]
