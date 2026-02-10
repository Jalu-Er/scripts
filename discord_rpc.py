from pypresence import Presence
import time
import psutil

# Gunakan Application ID dari aplikasi bernama 'Workspace'
client_id = '1470683622804557855' 
RPC = Presence(client_id)
RPC.connect()

def get_activity():
    # Mengambil list nama proses yang berjalan
    procs = [p.name() for p in psutil.process_iter(['name'])]
    
    # 1. Game Development (Unity Editor)
    if 'Unity' in procs:
        return {
            "details": "Game Development", 
            "state": "Building Virtual Worlds", 
            "icon": "icon_game"
        }
    
    # 2. Android Development (Android Studio)
    if 'studio64' in procs:
        return {
            "details": "Mobile Development", 
            "state": "Building Mobile Applications", 
            "icon": "icon_android"
        }

    # 3. Software Craftsmanship (VSCode / Code-OSS)
    if 'code-oss' in procs or 'code' in procs:
        return {
            "details": "Software Development", 
            "state": "Transforming Ideas into Code", 
            "icon": "icon_vscode"
        }

    # 4. Minecraft Infrastructure
    if 'java' in procs and any('minecraft' in p.name().lower() for p in psutil.process_iter(['name'])):
        return {
            "details": "Minecraft Workspace", 
            "state": "Managing Server & Skript", 
            "icon": "icon_mc"
        }

    # 5. Default / Idle: System Optimization
    return {
        "details": "System Optimization", 
        "state": "Environment: Arch Linux", 
        "icon": "icon_arch"
    }

print("Workspace Dynamic RPC Aktif...")

while True:
    try:
        activity = get_activity()
        RPC.update(
            details=activity["details"],
            state=activity["state"],
            large_image="logo_utama",
            large_text="RaivelXV | Workspace",
            small_image=activity["icon"],
            small_text=activity["details"],
            buttons=[{"label": "GitHub", "url": "https://github.com/Jalu-Er"}],
            start=time.time()
        )
    except Exception as e:
        print(f"Error: {e}")
    
    time.sleep(30)