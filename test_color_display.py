from color_display import show_color_window

def test_show_color_window_runs_without_error():
    try:
        show_color_window("blue")
        assert True
    except Exception:
        assert False
