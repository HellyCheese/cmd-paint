import pyautogui
import time
import os
import keyboard
import mouse

# 156 51 12.308 21.176

i = 0
abama = []
size = 1
transp = {
    0: '▓',
    1: '▒',
    2: '░',
    3: ' ',
    4: ' ',
    5: ' ',
    6: ' '
}
transpnum = 0

print('''[Управление]
    1, 2, 3, 4 — сменить прозрачность символов
    z — рисовать
    x — отчистить всё
    -/+ — размер кисти''')
input()
os.system("cls")

while i != 156 * 50:
    abama.insert(i, ' ')
    i += 1

while True:
    i = 0
    x, y = pyautogui.position()
    xd, yd = int(x // 12.308) + 2, int(y // 21.176) - 3
    symbolbefore = (xd - 1) + yd * 156

    if keyboard.press_and_release('-'):
        if size != 1:
            size -= 1
    if keyboard.press_and_release('+'):
        if size != 4:
            size += 1

    if keyboard.is_pressed('1'):
        transpnum = 0
    if keyboard.is_pressed('2'):
        transpnum = 1
    if keyboard.is_pressed('3'):
        transpnum = 2
    if keyboard.is_pressed('4'):
        transpnum = 3

    if keyboard.is_pressed('z'):
        try:

            if size == 1:

                abama[symbolbefore] = transp[transpnum]
                abama[symbolbefore + 1] = transp[transpnum]

        except IndexError:

            if size == 1:

                abama[symbolbefore] = transp[transpnum]
                abama[symbolbefore + 1] = transp[transpnum]

        os.system("cls")
        print(*abama[0:6552], sep='', flush=True)

    if keyboard.is_pressed('x'):
        os.system("cls")
        while i != 6552:
            abama[i] = ' '
            i += 1

    time.sleep(0.017)
