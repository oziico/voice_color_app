from unittest.mock import patch
import main

@patch("main.show_color_window")  
@patch("main.recognize_color_from_speech")
def test_main_flow(mock_recognize_color, mock_show_color_window):
    mock_recognize_color.return_value = "Yellow"

    main.main()

    mock_show_color_window.assert_called_with("Yellow")
