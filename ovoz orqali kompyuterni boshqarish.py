import speech_recognition as sr
import pyautogui

# Ovozni tanishish
recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Iltimos, nima qilmoqchisiz?")
    audio = recognizer.listen(source)

try:
    # Ovozni matnga o'girish
    text = recognizer.recognize_google(audio, language="uz-UZ")
    print(f"Sizning ovozingiz: {text}")

    # Ovoz orqali kompyuterni boshqarish
    if "kalkulyator" in text.lower():
        pyautogui.hotkey("win", "r")
        pyautogui.write("calc")
        pyautogui.press("enter")
    elif "paint" in text.lower():
        pyautogui.hotkey("win", "r")
        pyautogui.write("mspaint")
        pyautogui.press("enter")
    elif "Visual Studio Code" in text.lower():
        pyautogui.hotkey("win", "r")
        pyautogui.write("vscode")
        pyautogui.press("enter")
    else:
        print("Bu buyruqni tushunmadim.")
except sr.UnknownValueError:
    print("Ovozni taniy olmadim.")
except sr.RequestError:
    print("Google serveriga so'rovni yuborishda xatolik yuz berdi.")
