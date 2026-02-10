import psutil

def detect_activity():
    processes = {p.name().lower() for p in psutil.process_iter(['name'])}

    if "unity" in processes:
        return "Game Development", "Building Virtual Worlds", "icon_game"

    if "studio64" in processes:
        return "Mobile Development", "Building Mobile Applications", "icon_android"

    if "code" in processes or "code-oss" in processes:
        return "Software Development", "Transforming Ideas into Code", "icon_vscode"

    if "java" in processes and any("minecraft" in p for p in processes):
        return "Minecraft Workspace", "Managing Server & Skript", "icon_mc"

    return "System Optimization", "Environment: Arch Linux", "icon_arch"
