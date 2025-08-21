import ctypes
import time

# 🧠 Costanti Windows API
ES_CONTINUOUS        = 0x80000000
ES_SYSTEM_REQUIRED   = 0x00000001
ES_DISPLAY_REQUIRED  = 0x00000002
EXECUTION_STATE = ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED

# Struttura INPUT per SendInput
class INPUT(ctypes.Structure):
    _fields_ = [("type", ctypes.c_uint),
                ("ii", ctypes.c_ulonglong)]

SendInput = ctypes.windll.user32.SendInput

# Virtual-Key codes
VK_F15 = 0x7E  # F15 non ha effetto nei programmi normali
KEYEVENTF_KEYUP = 0x0002

def prevent_sleep():
    """Comunica al sistema operativo di restare sveglio"""
    ctypes.windll.kernel32.SetThreadExecutionState(EXECUTION_STATE)

def simulate_keypress():
    """Simula la pressione di un tasto 'inattivo' (F15)"""
    # KEYDOWN
    ctypes.windll.user32.keybd_event(VK_F15, 0, 0, 0)
    # KEYUP
    ctypes.windll.user32.keybd_event(VK_F15, 0, KEYEVENTF_KEYUP, 0)

def taurine_boost(interval=60):
    print("🟢 Sistema sveglio e stato Online attivo (CTRL+C per uscire)...")
    try:
        while True:
            prevent_sleep()
            simulate_keypress()
            print(f"[{time.strftime('%H:%M:%S')}] Tasto F15 simulato.")
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\n🛑 Terminato manualmente.")
        # Rilascia blocco standby
        ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)

if __name__ == "__main__":
    taurine_boost()
