import ctypes
import time
import argparse
import platform
import sys

# 🧠 Costanti Windows API
ES_CONTINUOUS        = 0x80000000
ES_SYSTEM_REQUIRED   = 0x00000001
ES_DISPLAY_REQUIRED  = 0x00000002
EXECUTION_STATE = ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED

# Virtual-Key codes
VK_F15 = 0x7E  # F15 non ha effetto nei programmi normali
KEYEVENTF_KEYUP = 0x0002

def print_logo(interval):
    logo = r'''
  _______                _            
 |__   __|              (_)           
    | | __ _ _   _ _ __  _ _ __   ___ 
    | |/ _` | | | | '__/| | '_ \ / _ \
    | | (_| | |_| | |   | | | | |  __/
    |_|\__,_|\__,_|_|   |_|_| |_|\___|
    '''
    print(logo)
    print(f"🟢 Sistema sveglio e stato Online attivo. Intervallo: {interval}s (CTRL+C per uscire)\n")

def prevent_sleep():
    """Comunica al sistema operativo di restare sveglio"""
    ctypes.windll.kernel32.SetThreadExecutionState(EXECUTION_STATE)

def simulate_keypress():
    """Simula la pressione di un tasto 'inattivo' (F15)"""
    ctypes.windll.user32.keybd_event(VK_F15, 0, 0, 0)  # KEYDOWN
    ctypes.windll.user32.keybd_event(VK_F15, 0, KEYEVENTF_KEYUP, 0)  # KEYUP

def taurine_boost(interval=60, silent=False):
    print_logo(interval)
    try:
        while True:
            prevent_sleep()
            simulate_keypress()
            if not silent:
                print(f"[{time.strftime('%H:%M:%S')}] Tasto F15 simulato.")
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\n🛑 Terminato manualmente.")
        ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)  # Rilascia blocco standby

def main():
    if platform.system() != "Windows":
        print("❌ Questo script funziona solo su Windows.")
        sys.exit(1)

    parser = argparse.ArgumentParser(description="Taurine: mantiene Windows sveglio in modo sicuro")
    parser.add_argument('-t', '--time', type=int, default=60, help='Intervallo in secondi tra simulazioni (default: 60)')
    parser.add_argument('-s', '--silent', action='store_true', help='Modalità silenziosa, senza stampare ogni ciclo')
    args = parser.parse_args()

    interval = max(1, args.time)  # almeno 1 secondo
    taurine_boost(interval, args.silent)

if __name__ == "__main__":
    main()