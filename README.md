# ⚡ Taurine – Energia pura per il tuo PC

**Taurine** è uno script Python leggero e potente che tiene il tuo PC **sempre sveglio**, come se avesse appena bevuto una lattina di taurina pura.

Blocca standby, screensaver e simula attività dell’utente per mantenere attivo lo stato "Online" su applicazioni come Teams, Zoom, Slack, ecc.

---

## 🧠 Funzionalità

- ⛔ Previene standby, blocco schermo e spegnimento del display
- ⌨️ Simula la pressione del tasto F15 (virtuale e inoffensivo) ogni minuto
- 🧩 Compatibile con qualsiasi app che rileva inattività
- 🐍 Usa solo Python standard e ctypes – zero dipendenze esterne
- 🖥️ Nessuna finestra fastidiosa, gira silenzioso in console

---

## 🚀 Avvio rapido

### 🔁 Esecuzione automatica via `taurine.bat`

Il modo più semplice per avviare tutto è eseguire:

taurine.bat

Questo:

- Crea un ambiente virtuale `.venv` (se non esiste)
- Installa le dipendenze da `requirements.txt`
- Lancia automaticamente `taurine.py`

### 🧪 Manuale (alternativa)

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python taurine.py
```

---

## 🛠 Avvio automatico con Windows

Per far partire TaurineBoost ad ogni accensione:

1. Premi `Win + R`
2. Scrivi `shell:startup` e premi Invio
3. Copia un collegamento a `taurine.bat` in quella cartella

---

## 🔧 Requisiti

- **Python 3.7+**
- Sistema operativo: **Windows**
- Dipendenze: `pyautogui` (installata da `requirements.txt`)

---

## 🐂 Nome ispirato alla **Taurina**

Proprio come una Red Bull per il tuo PC. Resti sveglio, attivo e reattivo... anche se tu non ci sei. 💻⚡

---

## 📄 Licenza

MIT – Fanne ciò che vuoi!

---

## 💬 Contatti

Creato con 💪 e caffeina da oznerol001110

```

lorys09@live.it

```
