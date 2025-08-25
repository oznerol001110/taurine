# ⚡ Taurine – Pure Energy for Your PC

## 🌍 Languages
- 🇬🇧 English (README.en.md)
- 🇮🇹 [Italiano](../README.md)
- 🇪🇸 [Español](README.es.md)
- 🇩🇪 [Deutsch](README.de.md)

**Taurine** is a lightweight and powerful Python script that keeps your PC **always awake**, as if it had just drunk an energy drink.

It prevents standby, screensaver, and simulates user activity to maintain the "Online" status in apps like Teams, Zoom, Slack, etc.

---

## 🐂 Name inspired by **Taurine**

Just like a Red Bull for your PC. Stay awake, active, and responsive… even if you’re not there. 💻⚡

---

## 🧠 Features

- ⛔ Prevents standby, lock screen, and display shutdown  
- ⌨️ Simulates pressing the F15 key (virtual and harmless) every minute  
- 🧩 Compatible with any app that detects inactivity  
- 🐍 Uses only standard Python and ctypes – zero external dependencies  
- 🖥️ No annoying windows, runs quietly in the console  

---

## ❤️ Support the project

Do you like Taurine? Donate and help me keep more PCs awake! ☕💻

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

## 🚀 Quick Start

### 🔁 Manual execution

The easiest way to run Taurine is to execute the Python script directly:

```

python taurine.py

```

Available options:

    python taurine.py -h

It will show:

- `-t`, `--time` → Interval in seconds between simulations (default: 60)  
- `-s`, `--silent` → Silent mode, without printing each cycle  

You can also specify interval and silent mode directly:

    python taurine.py -t 120 -s

---

## 🛠 Automatic startup on Windows

To start TaurineBoost at every boot:  

1. Press `Win + R`  
2. Type `shell:startup` and hit Enter  
3. Copy a shortcut to `taurine.py` into that folder  

Example target of the shortcut:

    C:\Python311\python.exe "C:\Path\taurine.py" -t 120

---

## 🔧 Requirements

- **Python 3.7+**  
- Operating system: **Windows**  
- Dependencies: `pyautogui` (installed via `requirements.txt`)  

---

## 📄 License

MIT – Do whatever you want!  

---

## 💬 Contacts

Created with 💪 and caffeine 🤭 by oznerol001110  


```

lorys09@live.it

```
