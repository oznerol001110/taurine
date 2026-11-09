import argparse
import shutil
import subprocess
import sys
import time


F15_KEY_CODE = "113"


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
    print(f"🟢 Mac sveglio e stato Online attivo. Intervallo: {interval}s (CTRL+C per uscire)\n")


def simulate_keypress():
    """Simula F15 tramite macOS System Events."""
    subprocess.run(
        [
            "osascript",
            "-e",
            f'tell application "System Events" to key code {F15_KEY_CODE}',
        ],
        check=True,
        capture_output=True,
        text=True,
    )


def taurine_boost(interval=60, silent=False):
    caffeinate = shutil.which("caffeinate")
    if caffeinate is None:
        raise RuntimeError("Il comando macOS 'caffeinate' non è disponibile.")

    print_logo(interval)
    keep_awake = subprocess.Popen([caffeinate, "-dims"])
    try:
        while True:
            if keep_awake.poll() is not None:
                raise RuntimeError("'caffeinate' è terminato inaspettatamente.")

            simulate_keypress()
            if not silent:
                print(f"[{time.strftime('%H:%M:%S')}] Tasto F15 simulato.")
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\n🛑 Terminato manualmente.")
    finally:
        keep_awake.terminate()
        keep_awake.wait()


def main():
    parser = argparse.ArgumentParser(
        description="Taurine per macOS: mantiene il Mac sveglio e simula F15"
    )
    parser.add_argument(
        "-t",
        "--time",
        type=int,
        default=60,
        help="Intervallo in secondi tra simulazioni (default: 60)",
    )
    parser.add_argument(
        "-s",
        "--silent",
        action="store_true",
        help="Modalità silenziosa, senza stampare ogni ciclo",
    )
    args = parser.parse_args()

    if sys.platform != "darwin":
        parser.error("Questo script funziona solo su macOS.")

    interval = max(1, args.time)
    try:
        taurine_boost(interval, args.silent)
    except FileNotFoundError as error:
        print(f"❌ Comando richiesto non trovato: {error.filename}", file=sys.stderr)
        sys.exit(1)
    except subprocess.CalledProcessError as error:
        detail = error.stderr.strip() or str(error)
        print(
            "❌ Impossibile simulare F15. Concedi a Terminale o al tuo "
            f"terminale i permessi di Accessibilità in macOS. Dettagli: {detail}",
            file=sys.stderr,
        )
        sys.exit(1)
    except RuntimeError as error:
        print(f"❌ {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
