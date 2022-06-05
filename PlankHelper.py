import pyautogui
from win32gui import FindWindow, GetWindowRect
import time
import random
from typing import Optional
from ctypes import windll, create_unicode_buffer
import os

d = {'space': 0,    # Keeps track of global keys pressed
     '1': 0}

window_name = 'Scenario Dependent'
game_name = 'Scenario Dependent'

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


def random_key(i, j):
    """
    :param i: Key to press
    :param j: Key to press
    :return: None
    """
    global d

    rand_int = random.uniform(0.03, 0.12)
    r = random.randint(1, 2)

    if d[i] >= 2:
        pyautogui.press(j)
        d[i] = 0
        d[j] = 0
        time.sleep(rand_int)
    if d[j] >= 1:
        pyautogui.press(i)
        d[i] = 0
        d[j] = 0
        time.sleep(rand_int)

    if r == 1:
        pyautogui.press(i)
        d[i] += 1
    pyautogui.press(j)
    d[j] += 1
    time.sleep(rand_int)

    return


def main():
    window_handle = FindWindow(None, window_name)
    game_region = GetWindowRect(window_handle)
    wd = getForegroundWindowTitle()
    mouse_position = pyautogui.position()

    while 'RuneLite' not in str(wd):
        wd = getForegroundWindowTitle()
        mouse_position = pyautogui.position()
        if mouse_position == (0, 0):
            break

    while mouse_position != (0, 0):
        mouse_position = pyautogui.position()
        if game_name in str(wd):
            for screenshot in os.listdir('resources\\plank_resources'):
                f = os.path.join('resources\\plank_resources', screenshot)
                if os.path.isfile(f):
                    on_screen = pyautogui.locateOnScreen(f, region=(game_region[0], game_region[1],
                                                                    game_region[2] - 529, game_region[3])
                                                         , confidence=0.95, grayscale=True)
                    rand_int = random.uniform(0.05, 0.2)
                    if on_screen:
                        if f == "resources\\plank_resources\\dialogue_bank1.png":
                            time.sleep(rand_int)
                            pyautogui.press('1')
                            time.sleep(rand_int)
                            pyautogui.press('f4')
                        else:
                            print(f)
                            random_key('space', '1')


if __name__ == '__main__':
    main()
