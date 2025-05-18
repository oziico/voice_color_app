import speech_recognition as sr

def recognize_color_from_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please say a color...")
        audio = recognizer.listen(source)

    try:
        color_name = recognizer.recognize_google(audio)
        print(f"You said: {color_name}")
        return color_name.lower()
    except sr.UnknownValueError:
        print("Speech not understood")
        return None
    except sr.RequestError:
        print("API error.")
        return None
