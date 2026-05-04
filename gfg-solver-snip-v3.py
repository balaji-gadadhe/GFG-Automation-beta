import time
import io
import pyautogui
from PIL import ImageGrab, Image
from google import genai
from google.genai import types

# --- CONFIG ---
# Get your key from https://aistudio.google.com/
API_KEY = "YOUR_API_KEY_HERE"

# gemini-2.5-flash is the stable 2026 'workhorse' for high-volume API tasks
MODEL_ID = "gemini-2.5-flash" 

def solve_universal():
    print("📸 Snipping from clipboard...")
    img = ImageGrab.grabclipboard()
    
    if not isinstance(img, Image.Image):
        print("❌ Error: No image found! Snip the question (Win+Shift+S) first.")
        return

    # Convert image to bytes
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    image_bytes = img_byte_arr.getvalue()

    # INITIALIZE CLIENT: Using the standard v1 production endpoint
    client = genai.Client(
        api_key=API_KEY,
        http_options=types.HttpOptions(api_version="v1")
    )
    
    prompt = """
    This is a GeeksforGeeks problem. 
    1. Identify the programming language from the dropdown in the image.
    2. Write the solution in THAT specific language.
    3. Provide ONLY the code logic inside the function/class.
    4. IMPORTANT: Start every single line at the far left (Zero Indentation). 
    5. Pay close attention to case sensitivity.
    6. Raw code only. No backticks, no comments.
    """

    print(f"🧠 Gemini is solving using {MODEL_ID}...")
    try:
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=[
                types.Part.from_bytes(data=image_bytes, mime_type="image/png"),
                prompt
            ]
        )
        
        raw_code = response.text.strip()
        
        # Clean markdown backticks
        if "```" in raw_code:
            lines = raw_code.splitlines()
            raw_code = "\n".join([l for l in lines if not l.strip().startswith("```")])

        print("⏳ Code ready! Click the GFG editor. Starting in 5 seconds...")
        for i in range(5, 0, -1):
            print(f"{i}...", end="\r")
            time.sleep(1)

        # THE UNIVERSAL TYPING LOOP
        for line in raw_code.split('\n'):
            stripped_line = line.lstrip() 
            
            # Move to a new line and force zero indentation
            pyautogui.press('enter')
            pyautogui.press('home')
            pyautogui.press('home')
            
            if stripped_line:
                pyautogui.write(stripped_line)
            
            time.sleep(0.04) 

        # THE GHOST-BUSTER CLEANUP
        print("🧹 Cleaning ghost brackets...")
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('shift')
        pyautogui.press('end')
        pyautogui.keyUp('shift')
        pyautogui.keyUp('ctrl')
        pyautogui.press('backspace')


        print("\n✅ Success! Solution injected.")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    solve_universal()