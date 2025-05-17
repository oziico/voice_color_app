from speech_handler import recognize_color_from_speech
import pytest
from unittest.mock import patch

@patch("speech_handler.sr.Recognizer.recognize_google")
@patch("speech_handler.sr.Recognizer.listen")
@patch("speech_handler.sr.Microphone")
def test_recognize_color_from_speech(mock_microphone, mock_listen, mock_recognize_google):
    mock_recognize_google.return_value = "green"
    
    color = recognize_color_from_speech()
    
    assert color == "green"
