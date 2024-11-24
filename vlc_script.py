import subprocess
import time

import pyautogui


def vlc_launch():
    """
    Launch VLC media player and press Ctrl+1 to open the first playlist
    """
    try:
        # Launch VLC Media Player
        subprocess.Popen(["vlc"])

        # Wait for VLC to start up
        time.sleep(3)

        # Press Ctrl+1
        pyautogui.hotkey("ctrl", "1")

        print("VLC launched and Ctrl+1 pressed successfully")

    except Exception as e:
        print(f"Error occurred: {str(e)}")


if __name__ == "__main__":
    vlc_launch()
