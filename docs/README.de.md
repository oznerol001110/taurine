# ⚡ Taurine – Reine Energie für deinen PC

## 🌍 Sprachen
- 🇩🇪 Deutsch (README.de.md)
- 🇮🇹 [Italiano](../README.md)
- 🇬🇧 [English](README.en.md)
- 🇪🇸 [Español](README.es.md)


**Taurine** ist ein leichtes und leistungsstarkes Python-Skript, das deinen PC **immer wach hält**, als hätte er gerade ein Energy-Drink getrunken.

Es blockiert Standby, Bildschirmschoner und simuliert Benutzeraktivität, um den Status "Online" in Apps wie Teams, Zoom, Slack usw. aufrechtzuerhalten.

---

## 🐂 Name inspiriert von **Taurin**

Wie ein Red Bull für deinen PC. Du bleibst wach, aktiv und reaktionsschnell... auch wenn du nicht da bist. 💻⚡

---

## 🧠 Funktionen

- ⛔ Verhindert Standby, Bildschirm-Sperre und Monitorabschaltung  
- ⌨️ Simuliert die Taste F15 (virtuell und ungefährlich) jede Minute  
- 🧩 Kompatibel mit jeder App, die Inaktivität erkennt  
- 🐍 Verwendet nur Standard-Python und ctypes – keine externen Abhängigkeiten  
- 🖥️ Keine störenden Fenster, läuft leise in der Konsole  

---

## ❤️ Unterstütze das Projekt

Gefällt dir Taurine? Spende und hilf mir, mehr PCs wach zu halten ☕💻

<p align="center">
  <a href="https://www.buymeacoffee.com/oznerol" target="_blank">
    <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me a Coffee">
  </a>
  &nbsp;&nbsp;
  <a href="https://www.paypal.com/donate/?hosted_button_id=L95AXFR3LEZ7Q" target="_blank">
    <img src="https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white" alt="Donate with PayPal">
  </a>
</p>

---

## 🚀 Schnellstart

### 🔁 Manuelle Ausführung

Die einfachste Möglichkeit, Taurine zu starten, ist das direkte Ausführen des Python-Skripts:

    python taurine.py

Verfügbare Optionen:

    python taurine.py -h

Es zeigt:

- `-t`, `--time` → Intervall in Sekunden zwischen Simulationen (Standard: 60)  
- `-s`, `--silent` → Leiser Modus, ohne jeden Zyklus auszugeben  

Du kannst Intervall und Still-Modus auch direkt angeben:

    python taurine.py -t 120 -s

---

## 🛠 Automatischer Start unter Windows

Um TaurineBoost bei jedem Start zu starten:  

1. Drücke `Win + R`  
2. Tippe `shell:startup` und drücke Enter  
3. Kopiere eine Verknüpfung zu `taurine.py` in diesen Ordner  

Beispiel-Ziel der Verknüpfung:

    C:\Python311\python.exe "C:\Path\taurine.py" -t 120

---

## 🔧 Anforderungen

- **Python 3.7+**  
- Betriebssystem: **Windows**  
- Abhängigkeiten: `pyautogui` (installiert über `requirements.txt`)  

---

## 📄 Lizenz

MIT – Mach, was du willst!  

---

## 💬 Kontakt

Erstellt mit 💪 und Koffein 🤭 von oznerol001110  

```

lorys09@live.it

```
