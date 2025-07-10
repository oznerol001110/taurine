import ctypes
import pyautogui
import time

# 🧠 Costanti Windows API
ES_CONTINUOUS        = 0x80000000
ES_SYSTEM_REQUIRED   = 0x00000001
ES_DISPLAY_REQUIRED  = 0x00000002
EXECUTION_STATE = ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED

def prevent_sleep():
    """Comunica al sistema operativo di restare sveglio"""
    ctypes.windll.kernel32.SetThreadExecutionState(EXECUTION_STATE)

def simulate_user_activity():
    """Muove leggermente il mouse per restare 'Online' su Teams"""
    current_pos = pyautogui.position()
    pyautogui.moveRel(1, 0, duration=0.1)
    pyautogui.moveRel(-1, 0, duration=0.1)
    pyautogui.moveTo(current_pos)  # Torna alla posizione originale

def taurine_boost(interval=60):
    print("🟢 Sistema sveglio e stato Online attivo (CTRL+C per uscire)...")
    try:
        while True:
            prevent_sleep()
            simulate_user_activity()
            print(f"[{time.strftime('%H:%M:%S')}] Attività simulata.")
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\n🛑 Terminato manualmente.")
        # Rilascia blocco standby
        ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)

if __name__ == "__main__":
    taurine_boost()
