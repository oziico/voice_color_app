from speech_handler import recognize_color_from_speech
from color_display import show_color_window

def main():
    color = recognize_color_from_speech()
    if color:
        show_color_window(color)

if __name__ == "__main__":
    main()
