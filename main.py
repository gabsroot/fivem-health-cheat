import pyMeow as pm
import psutil, re

offsets = {
    "FiveM_b1604_GTAProcess.exe": {
        "world": 0x247F840
    },
    "FiveM_b2060_GTAProcess.exe": {
        "world": 0x24C8858
    },
    "FiveM_b2189_GTAProcess.exe": {
        "world": 0x24E6D90
    },
    "FiveM_b2372_GTAProcess.exe": {
        "world": 0x252DCD8
    },
    "FiveM_b2545_GTAProcess.exe": {
        "world": 0x25667E8
    },
    "FiveM_b2612_GTAProcess.exe": {
        "world": 0x2567DB0
    },
    "FiveM_b2699_GTAProcess.exe": {
        "world": 0x26684D8
    },
    "FiveM_b2802_GTAProcess.exe": {
        "world": 0x254D448
    },
    "FiveM_b3095_GTAProcess.exe": {
        "world": 0x2593320
    }
}

# localplayer: 0x8
# localplayerhealth: 0x280

health = float(input("amount of health: "))

process_name = next((process.info["name"] for process in psutil.process_iter(["name"]) if re.search(r"^FiveM_b\d+_GTAProcess\.exe$", process.info.get("name", ""))), None)
process = pm.open_process(process_name)
module = pm.get_module(process, process_name)["base"]

world = pm.r_int64(process, module + offsets[process_name]["world"])
local_player = pm.r_int64(process, world + 0x8)
pm.w_float(process, local_player + 0x280, health)