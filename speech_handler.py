import speech_recognition as sr

def recognize_color_from_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Bir renk söyleyin...")
        audio = recognizer.listen(source)

    try:
        color_name = recognizer.recognize_google(audio)
        print(f"Söylenen renk: {color_name}")
        return color_name.lower()
    except sr.UnknownValueError:
        print("Ses anlaşılamadı.")
        return None
    except sr.RequestError:
        print("API hatası.")
        return None
