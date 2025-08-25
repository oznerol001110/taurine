# ⚡ Taurine – Energía pura para tu PC

## 🌍 Idiomas
- 🇪🇸 Español (README.es.md)
- 🇮🇹 [Italiano](../README.md)
- 🇬🇧 [English](README.en.md)
- 🇩🇪 [Deutsch](README.de.md)

**Taurine** es un script de Python ligero y potente que mantiene tu PC **siempre despierto**, como si acabara de beber una bebida energética.

Evita la suspensión, el salvapantallas y simula actividad del usuario para mantener el estado "Online" en aplicaciones como Teams, Zoom, Slack, etc.

---

## 🐂 Nombre inspirado en la **Taurina**

Igual que un Red Bull para tu PC. Te mantienes despierto, activo y receptivo… incluso si no estás allí. 💻⚡

---

## 🧠 Funcionalidades

- ⛔ Evita suspensión, bloqueo de pantalla y apagado del monitor  
- ⌨️ Simula la pulsación de la tecla F15 (virtual e inofensiva) cada minuto  
- 🧩 Compatible con cualquier aplicación que detecte inactividad  
- 🐍 Usa solo Python estándar y ctypes – cero dependencias externas  
- 🖥️ Sin ventanas molestas, se ejecuta en consola de manera silenciosa  

---

## ❤️ Apoya el proyecto

¿Te gusta Taurine? ¡Dona y ayúdame a mantener más PCs despiertos! ☕💻

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

## 🚀 Inicio rápido

### 🔁 Ejecución manual

La forma más sencilla de ejecutar Taurine es ejecutar directamente el script en Python:

    python taurine.py

Opciones disponibles:

    python taurine.py -h

Mostrará:

- `-t`, `--time` → Intervalo en segundos entre simulaciones (por defecto: 60)  
- `-s`, `--silent` → Modo silencioso, sin imprimir cada ciclo  

También puedes especificar el intervalo y el modo silencioso directamente:

    python taurine.py -t 120 -s

---

## 🛠 Inicio automático en Windows

Para iniciar TaurineBoost en cada arranque:  

1. Pulsa `Win + R`  
2. Escribe `shell:startup` y pulsa Enter  
3. Copia un acceso directo a `taurine.py` en esa carpeta  

Ejemplo de destino del acceso directo:

    C:\Python311\python.exe "C:\Ruta\taurine.py" -t 120

---

## 🔧 Requisitos

- **Python 3.7+**  
- Sistema operativo: **Windows**  
- Dependencias: `pyautogui` (instalada desde `requirements.txt`)  

---

## 📄 Licencia

MIT – ¡Haz lo que quieras!  

---

## 💬 Contacto

Creado con 💪 y cafeína 🤭 por oznerol001110  

```

lorys09@live.it

```
