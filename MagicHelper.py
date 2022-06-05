import pyautogui
import time
import random
from typing import Optional
from ctypes import windll, create_unicode_buffer

window_name = 'SCENARIO DEPENDENT'

"""
I created these scripts to automate repetitive, tedious tasks in a game that has an advanced antiban system.
Through testing, I discovered it's antiban is heavily dependent on mouse movement. Therefore the scripts made
require human mouse input but automate the rest.

Some information has been obfuscated in this script so that it is not abused.
"""


def getForegroundWindowTitle() -> Optional[str]:
    """
    Helper function to get the active foreground window, thanks to
    https://stackoverflow.com/questions/10266281/obtain-active-window-using-python
    :return: Returns active window as string
    """
    hWnd = windll.user32.GetForegroundWindow()
    length = windll.user32.GetWindowTextLengthW(hWnd)
    buf = create_unicode_buffer(length + 1)
    windll.user32.GetWindowTextW(hWnd, buf, length + 1)

    # 1-liner alternative: return buf.value if buf.value else None
    if buf.value:
        return buf.value
    else:
        return None


def main():
    wd = getForegroundWindowTitle()
    mouse_position = pyautogui.position()
    get_alch_position = True
    alch_pos = None

    while str(wd) != window_name:
        wd = getForegroundWindowTitle()
        mouse_position = pyautogui.position()
        if mouse_position == (0, 0):
            break

    while mouse_position != (0, 0) and str(wd) == window_name:
        if get_alch_position:
            while alch_pos is None:
                alch_pos = pyautogui.locateCenterOnScreen('resources\\alch.png', grayscale=True, confidence=0.8)
            get_alch_position = False

        rand = random.randint(1, 6)
        if rand != 5 and alch_pos is not None:
            mouse_position = pyautogui.position()
            pyautogui.click()
            r = random.uniform(0.9, 1.45)
            print(r)
            time.sleep(r)
        else:
            if alch_pos is not None:
                mouse_position = pyautogui.position()
                print(alch_pos)
                r1 = random.randint(alch_pos[0] - 6, alch_pos[0])
                r2 = random.randint(alch_pos[1] - 6, alch_pos[1])
                r3 = random.uniform(0.2, 0.5)
                pyautogui.moveTo(r1, r2, r3)
                pyautogui.click()
                r = random.uniform(1, 1.6)
                print(r)
                time.sleep(r)


if __name__ == '__main__':
    main()
