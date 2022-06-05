import pyautogui
import time
import random
from typing import Optional
from ctypes import windll, create_unicode_buffer

d = {'1': 0,  # Keeps track of global keys pressed
     '4': 0}

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


def random_key(i, j):
    """
    :param i: Key to press
    :param j: Key to press
    :return: None
    """
    global d

    rand_int = random.uniform(0.1, 0.5)
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
    wd = getForegroundWindowTitle()
    mouse_position = pyautogui.position()
    rect = (909, 1097, 1329, 1109)  # Hard coded window

    while str(wd) != window_name:
        wd = getForegroundWindowTitle()
        mouse_position = pyautogui.position()
        if mouse_position == (0, 0):  # Fail safe
            break

    while mouse_position != (0, 0) and str(wd) == window_name:
        mouse_position = pyautogui.position()
        wander_int = random.randint(1, 6)
        if (rect[0] <= mouse_position[0] <= rect[2]) and (rect[1] <= mouse_position[1] <= rect[3]):
            if wander_int == 6:
                r1 = random.randint(mouse_position[0] - 10, mouse_position[0] + 10)
                r2 = random.randint(rect[1], rect[3])
                r3 = random.uniform(0.05, 0.11)
                if rect[0] <= r1 <= rect[2]:
                    pyautogui.moveTo(r1, r2, r3)
            rand_int = random.uniform(0.051, 0.068)
            pyautogui.rightClick()
            time.sleep(rand_int)
            pyautogui.leftClick()
            rand_int2 = random.uniform(0.12, 0.7)
            time.sleep(rand_int2)
            for i in range(random.randint(2, 5)):
                pyautogui.press('1')
                time.sleep(random.uniform(0, 0.24))
            for i in range(random.randint(2, 5)):
                pyautogui.press('4')
                time.sleep(random.uniform(0, 0.23))
            rand_int3 = random.uniform(0.65, 0.81)
            time.sleep(rand_int3)


if __name__ == '__main__':
    main()
