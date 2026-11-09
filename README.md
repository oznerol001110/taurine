# ⚡ Taurine – Energia pura per il tuo PC

## 🌍 Lingue
- 🇮🇹 Italiano (README.md)
- 🇬🇧 [English](docs/README.en.md)
- 🇪🇸 [Español](docs/README.es.md)
- 🇩🇪 [Deutsch](docs/README.de.md)

**Taurine** è uno script Python leggero e potente che tiene il tuo PC **sempre sveglio**, come se avesse appena bevuto una bevanda energetica.

Blocca standby, screensaver e simula attività dell’utente per mantenere attivo lo stato "Online" su applicazioni come Teams, Zoom, Slack, ecc.

---

## 🐂 Nome ispirato alla **Taurina**

Proprio come una Red Bull per il tuo PC. Resti sveglio, attivo e reattivo... anche se tu non ci sei. 💻⚡

---

## 🧠 Funzionalità

- ⛔ Previene standby, blocco schermo e spegnimento del display
- ⌨️ Simula la pressione del tasto F15 (virtuale e inoffensivo) ogni minuto
- 🧩 Compatibile con qualsiasi app che rileva inattività
- 🐍 Usa solo Python standard e ctypes – zero dipendenze esterne
- 🖥️ Nessuna finestra fastidiosa, gira silenzioso in console

---

## ❤️ Supporta il progetto

Ti piace Taurine? Dona e aiutami a tenere svegli più PC! ☕💻

<p align="center">
  <!-- Buy Me a Coffee -->
  <a href="https://www.buymeacoffee.com/oznerol" style="height: 5rem; width: auto;" target="_blank">
    <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" 
         alt="Buy Me a Coffee" 
         style="height: 5rem; width: auto;">
  </a>
  &nbsp;&nbsp;
  <!-- PayPal -->
  <a href="https://www.paypal.com/donate/?hosted_button_id=L95AXFR3LEZ7Q" style="height: 5rem; width: auto;" target="_blank">
    <img src="https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white" 
         alt="Donate with PayPal" 
         style="height: 5rem; width: auto;">
  </a>
</p>

---

## 🚀 Avvio rapido

### 🔁 Esecuzione manuale

Il modo più semplice per avviare Taurine è eseguire direttamente lo script Python:

```

python taurine.py

```

Opzioni disponibili:

```

python taurine.py -h

```

Mostrerà:

- `-t`, `--time` → Intervallo in secondi tra simulazioni (default: 60)

- `-s`, `--silent` → Modalità silenziosa, senza stampare ogni ciclo

Puoi anche specificare intervallo e modalità silenziosa direttamente:

```

python taurine.py -t 120 -s

```

### 🍎 macOS

Per macOS usa lo script dedicato:

```

python3 taurine_mac.py

```

Le opzioni `-t` / `--time` e `-s` / `--silent` sono le stesse della versione Windows. Lo script usa `caffeinate` per impedire la sospensione e simula F15 tramite AppleScript. Al primo avvio, macOS potrebbe chiedere di autorizzare l'app Terminale in **Impostazioni di Sistema → Privacy e sicurezza → Accessibilità**.

## 🛠 Avvio automatico con Windows

Per far partire Taurine ad ogni accensione:

1. Premi `Win + R`
2. Scrivi `shell:startup` e premi Invio
3. Copia un collegamento a `taurine.py` in quella cartella

   - Esempio target del collegamento:

     ```

     C:\Python311\python.exe "C:\Percorso\taurine.py" -t 120

     ```

---

## 🔧 Requisiti

- **Python 3.7+**
- **Windows** per `taurine.py`; **macOS** per `taurine_mac.py`
- macOS: comandi di sistema `caffeinate` e `osascript`; nessuna dipendenza Python esterna

---

## 📄 Licenza

MIT – Fanne ciò che vuoi!

---

## 💬 Contatti

Creato con 💪 e caffeina 🤭 da oznerol001110

```

lorys09@live.it

```
