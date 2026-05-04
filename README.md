# 🚀 GFG Automation Beta

A powerful dual-mode automation suite for GeeksforGeeks (GFG) that uses **Gemini AI** to solve coding problems instantly. This project bypasses common hurdles like "anti-paste" restrictions and aggressive editor auto-indentation by using hardware-level keyboard simulation.

---

## ✨ Features

*   **Mode 1: The Sniper (OCR)** - Uses computer vision to read problem statements and language settings directly from your screen.
*   **Mode 2: The Ghost (Text-to-Code)** - A background listener that solves text copied to your clipboard and triggers via a custom hotkey.
*   **Zero-Indent Injection** - A custom typing engine that forces absolute zero-indentation to prevent the "staircase effect" in web editors.
*   **Ghost-Buster Cleanup** - Automatically cleans up auto-generated brackets (`}`) and phantom indentation after injection.
*   **Multi-Language Support** - Handles Python, Java, C++, and C logic seamlessly.

---

## 🛠️ Installation

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/GFG-Automation-Beta.git](https://github.com/YOUR_USERNAME/GFG-Automation-Beta.git)
    cd GFG-Automation-Beta
    ```

2.  **Install Required Libraries:**
    ```bash
    pip install pyautogui pillow google-genai pyperclip keyboard
    ```

3.  **Configure API Key:**
    *   Generate a free API key at [Google AI Studio](https://aistudio.google.com/).
    *   Open `gfg-solver-snip-v3.py` and `gfg-solver-text-v1.py`.
    *   Replace `"YOUR_API_KEY_HERE"` with your actual key.

---

## 📖 How to Use

### 1. Sniper Mode (`gfg-solver-snip-v3.py`)
*Best for: Visual accuracy and dropdown detection.*

1.  Run the script: `python gfg-solver-snip-v3.py`
2.  Snip the problem using **Win + Shift + S**. Make sure the language dropdown is visible in the snip.
3.  Click your cursor inside the GFG editor.
4.  After the 5-second countdown, the script will automatically type the solution.

### 2. Ghost Mode (`gfg-solver-text-v1.py`)
*Best for: Speed and background automation.*

1.  Run the script: `python gfg-solver-text-v1.py`
2.  Highlight the problem statement text on the GFG page and press **Ctrl + C**.
3.  Click into the GFG editor.
4.  Press **Ctrl + Alt + V** to trigger the solver and auto-typing.

---

## ⚙️ Recommended GFG Settings

To ensure 100% accuracy during the typing phase, it is recommended to adjust the following in the GFG Editor Settings (Gear Icon):
*   **Auto Indent:** OFF
*   **Auto Close Brackets:** OFF

---

## ⚠️ Troubleshooting

*   **429 Resource Exhausted:** You have hit the Gemini API rate limit. Wait 60 seconds for the quota to reset.
*   **404 Not Found:** Ensure you are using the correct `MODEL_ID` (Gemini 1.5 or 2.5 Flash) and that your `google-genai` library is up to date.
*   **Indentation Errors:** If the code is "staircasing," ensure you are using the latest version of the script which includes the `Double Home` logic.

---

## ⚖️ Disclaimer

This tool is created for **educational purposes only**. It is intended to help students understand logic patterns and automate repetitive workflows. Do not use this for competitive programming contests or interviews. Understanding the code Gemini generates is your responsibility!

---
