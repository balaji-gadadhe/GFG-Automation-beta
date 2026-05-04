import time
import io
import pyautogui
import pyperclip
import keyboard # install with: pip install keyboard
from PIL import ImageGrab, Image
from google import genai
from google.genai import types

# --- CONFIG ---
API_KEY = "YOUR_API_KEY_HERE"
MODEL_ID = "gemini-1.5-flash" # Use 1.5 for higher free-tier limits

def get_gemini_solution(text_content):
    client = genai.Client(api_key=API_KEY, http_options={'api_version': 'v1'})
    
    # Prompt optimized for text-based copying
    prompt = f"""
    The following is a GeeksforGeeks coding problem.
    PROBLEM: {text_content}
    
    1. Identify the likely language (Python/Java/C++).
    2. Provide ONLY the code body. 
    3. Start EVERY line at the far left (Zero Indentation).
    4. No markdown, no backticks, no comments.
    """

    try:
        response = client.models.generate_content(model=MODEL_ID, contents=prompt)
        return response.text.strip()
    except Exception as e:
        print(f"❌ Gemini Error: {e}")
        return None

def main():
    print("👻 GHOST MODE ACTIVE")
    print("1. Copy a question from GFG.")
    print("2. Click where you want to paste.")
    print("3. Press 'Ctrl+Alt+V' to trigger the auto-type.")
    
    while True:
        # Wait for the specific hotkey so it doesn't type randomly
        if keyboard.is_pressed('ctrl+alt+v'):
            clipboard_text = pyperclip.paste()
            
            if len(clipboard_text) < 10:
                print("⚠️ Clipboard too short. Copy the question first!")
                continue

            print("🧠 Solving and preparing to type...")
            code = get_gemini_solution(clipboard_text)
            
            if code:
                # Remove backticks if Gemini added them
                if "```" in code:
                    code = "\n".join([l for l in code.splitlines() if not l.strip().startswith("```")])
                
                print("⏳ Clicking back to GFG? Typing in 3 seconds...")
                time.sleep(3)
                
                # Universal Typing & Cleaning Logic
                for line in code.split('\n'):
                    stripped = line.lstrip()
                    pyautogui.press('enter')
                    pyautogui.press('home')
                    pyautogui.press('home')
                    if stripped:
                        pyautogui.write(stripped, interval=0.01)
                
                # Ghost Buster Cleanup
                pyautogui.keyDown('ctrl'); pyautogui.keyDown('shift'); pyautogui.press('end')
                pyautogui.keyUp('shift'); pyautogui.keyUp('ctrl'); pyautogui.press('backspace')
                
                print("✅ Done! Ghost Mode still active...")
            
            time.sleep(1) # Prevent double-triggering

if __name__ == "__main__":
    main()